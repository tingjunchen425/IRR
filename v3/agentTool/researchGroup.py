import asyncio
from google.adk.runners import Runner
from google.adk import agents
from google.adk.sessions import Session, InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
import dotenv
import uuid
from pydantic import BaseModel, Field
import json
import sys
import os
import time

dotenv.load_dotenv()

session_stateful_service = InMemorySessionService()
APP_NAME = "sub_agent_researcher"
SESSION_ID = str(uuid.uuid4())
INITIONAL_STATE = {
    "app_name": APP_NAME,
    "session_id": SESSION_ID,
    "TASKS": "Let agents handle research tasks in parallel.",
}

class finding(BaseModel):
    info: str = Field(description="Key findings from the study.")
    source: str = Field(description="The source URL or reference for the information.")

class output(BaseModel):
    agent_name: str = Field(description="Name of the agent that produced the findings.")
    findings: list[finding] = Field(description="List of findings from the research tasks.")
    summary: str = Field(description="A brief summary of the finding.")

async def create_session():
    service = await session_stateful_service.create_session(
        app_name=APP_NAME,
        user_id="lead_agent",
        state=INITIONAL_STATE,
        session_id=SESSION_ID,
    )
    return service

# Construct the absolute path to prompt.md
prompt_path = os.path.join(os.path.dirname(__file__), "prompt.md")
with open(prompt_path, "r", encoding="utf-8") as f:
    subAgent_prompt = f.read()
print(subAgent_prompt)

def generate_sub_agents(tasks: list[str]) -> list[agents.Agent]:
    sub_agents = []
    for task in tasks:
        safe_task_name = task['name']
        safe_task_name = safe_task_name.replace(" ", "_").replace("-", "_")
        sub_agent = agents.Agent(
            name=f"subAgent_{safe_task_name}",
            description=f"Sub-agent to handle the task: {task['name']}",
            model="gemini-2.5-flash",
            instruction=f"""
            current date: {time.strftime("%Y-%m-%d")}
            Please conduct research based on {task['prompt']}.
            {subAgent_prompt}
            After using the google_search tool, you must format your final response as a JSON object that conforms to the following structure:
            {{
                "agent_name": "{f"subAgent_{safe_task_name}"}",
                "findings": [{{ "info": "Key finding from the study.", "source": "The source URL." }}],
                "summary": "A brief summary of the findings."
            }}
            """,
            tools=[google_search],
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
        )
        sub_agents.append(sub_agent)
    subagents = generate_Parallel(sub_agents)
    return subagents

def generate_Parallel(agentlist: list[agents.Agent]) -> agents.ParallelAgent:
    researchSubAgent = agents.ParallelAgent(
        name = "researchSubAgent",
        description = "Parallel agent to handle multiple research tasks.",
        sub_agents=agentlist
    )
    return researchSubAgent

class expertOutput(BaseModel):
    summary: str = Field(description="Summary of the research findings.")
    insights: str = Field(description="Insights based on the collected data.")

def create_expert_agent(prompt) -> agents.Agent:
    expertAgent = agents.Agent(
        name="expertAgent",
        description="Supervisor agent to oversee the research process.",
        model="gemini-2.5-pro",
        instruction=f"""
        You will be provided with a list of JSON objects from various research agents. Each JSON object contains 'findings' and a 'summary'.
        Your task is to aggregate all the information and generate a comprehensive final report.
        Based on the provided data, {prompt}
        """,
        output_schema=expertOutput,
    )
    return expertAgent

async def run_agent_tasks(runner, researchData):
    """Helper function to run agent tasks and collect data."""
    new_message = types.Content(
        role="model",
        parts=[types.Part(text="Starting research tasks with sub-agents.")],
    )
    for event in runner.run(
        user_id="lead_agent",
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response:
            text = event.content.parts[0].text
            try:
                # The output from ParallelAgent is a list of JSON strings
                data = json.loads(text)
                if isinstance(data, list):
                    researchData.extend(data)
                else:
                    researchData.append(data)
            except json.JSONDecodeError:
                # Handle cases where the output is not a valid JSON string
                print(f"Warning: Could not decode JSON from agent response: {text}")
                researchData.append({"raw_output": text}) # Store raw output
            print(type(text))
            print(text)
            print('*' * 20)

async def main(tasks: list[str], summary_prompt: str = "Please summarize the research findings and provide insights."):
    # agents.init()  # Initialize the agent framework
    researchData = []
    # Example usage
    sub_agents = generate_sub_agents(tasks)
    print(f"Generated sub-agents for tasks: {[task['name'] for task in tasks]}")
    expertAgent = create_expert_agent(summary_prompt)
    agentGroup = agents.SequentialAgent(
        name="researchGroup",
        description="Group of agents to handle research tasks in parallel.",
        sub_agents=[sub_agents],
    )
    print("-" * 20)
    await create_session()
    
    runner = Runner(
        app_name= APP_NAME,
        agent=agentGroup,
        session_service= session_stateful_service,
    )

    await asyncio.gather(run_agent_tasks(runner, researchData))
    
    print("-" * 20)
    print("Research tasks completed.")
    researchResult = researchData
    # print("Research Results:"'\n', researchResult)
    return researchResult

async def researchGroup(tasks: list[str],summary_prompt: str = "Please summarize the research findings and provide insights."):
    """
    Function to initiate the research group process with given tasks.
    Args:
        tasks (list[str]): List of research tasks dictionaries to be handled by sub-agents.
        summary_prompt (str): Prompt for the expert agent to summarize findings and provide insights.
    """
    result = await main(tasks,summary_prompt)
    return result

if __name__ == "__main__":
    result = asyncio.run(researchGroup([{"name": "research AI", "prompt": "Research the latest advancements in AI."},
                    {"name": "research LLM", "prompt": "Research the latest advancements in LLM."},
                    {"name": "research Machine Learning", "prompt": "Research the latest advancements in Machine Learning."}]))
    with open('research_results.json', 'w', encoding='utf-8') as f:
        js = json.dumps(result, indent=4, ensure_ascii=False)
        f.write(js)

