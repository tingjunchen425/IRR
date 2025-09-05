import sys
import os
import time
import re

# Add the project root directory to the Python path
# This allows for absolute imports from the 'v4' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
from google.adk.runners import Runner
from google.adk import agents
from google.adk.sessions import Session, InMemorySessionService
from google.adk.tools import google_search, LongRunningFunctionTool
from google.adk.tools.agent_tool import AgentTool
from google.genai import types
import dotenv
import uuid
from pydantic import BaseModel, Field
import os
import time
from agentTool.searchagent import search_agent
from agentTool.paperAgent import paper_agent
from agentTool.api_tool import arxiv_tool


dotenv.load_dotenv()

# Construct the absolute path to taskagent_prompt.md
prompt_path = os.path.join(os.path.dirname(__file__), "taskagent_prompt.md")
with open(prompt_path, "r", encoding="utf-8") as f:
    subAgent_prompt = f.read()


search_agent = agents.Agent(
    name="searchAgent",
    description="search agent to search information for the user.",
    model="gemini-2.5-flash",
    instruction="""
    You are a search agent,
    use google search to give information about the user's research topic.
    """,
    tools=[google_search]
)

APP_NAME = "taskagent"
SESSION_SERVICE = InMemorySessionService()

async def create_session():
    SESSION_ID = str(uuid.uuid4())
    INITIONAL_STATE = {
        "app_name": APP_NAME,
        "session_id": SESSION_ID,
        "TASKS": "Let agents handle research tasks in parallel.",
    }
    service = await SESSION_SERVICE.create_session(
        app_name=APP_NAME,
        user_id="lead_agent",
        state=INITIONAL_STATE,
        session_id=SESSION_ID,
    )
    return SESSION_SERVICE, SESSION_ID

def sanitize_agent_name(name: str) -> str:
    # 只允許字母、數字、底線，其他都換成_
    name = re.sub(r'\W', '_', name)
    # 如果第一個字元不是字母或底線，前面補底線
    if not re.match(r'^[a-zA-Z_]', name):
        name = '_' + name
    return name

def generate_agent(name:str, task:str, tool: str) -> agents.Agent:
    safe_task_name = sanitize_agent_name(name)
    sub_agent = agents.Agent(
        name=f"subAgent_{safe_task_name}",
        description=f"Sub-agent to handle the task: {name}",
        model="gemini-2.5-flash",
        instruction=f"""
        current date: {time.strftime("%Y-%m-%d")}
        {subAgent_prompt}
        Task: {task}
        """,
    )
    if tool == "arxiv_tool":
        sub_agent.tools = [AgentTool(paper_agent)]
    else:
        sub_agent.tools = [google_search]
    return sub_agent

def group_agent(tasks: list[dict]) -> agents.Agent:
    group_agents = []
    for task in tasks:
        sub_agent = generate_agent(task["name"], task["prompt"], task["tool"])
        group_agents.append(sub_agent)
        time.sleep(6)
    
    parallel_agent = agents.ParallelAgent(
        name="research_group_agent",
        description="An agent that runs multiple research agents in parallel.",
        sub_agents=group_agents
    )
    return parallel_agent

async def run_taskagents(tasks: list[dict]) -> list[str]:
    """
    Run a set of tasks using a group agent.
    example input: [{"name": "research AI", "prompt": "Research the latest advancements in AI.", "tool": 'arxiv_tool'}]
    tool: The tool to be used for the task.Only can choose from: arxiv_tool, google_search
    """
    group = group_agent(tasks)

    runner = Runner(
        app_name=APP_NAME,
        agent=group,
        session_service=SESSION_SERVICE,
    )
    results = await run(runner)
    return results

async def run(runner) -> list[str]:
    new_message = types.Content(
        role="model",
        parts=[types.Part(text="Starting research tasks with sub-agents.")],
    )
    session, session_id = await create_session()
    results = []
    async for event in runner.run_async(
        user_id="lead_agent",
        session_id=session_id,
        new_message=new_message,
    ):
        if event.is_final_response:
            # 安全檢查 event.content 與 parts
            if event.content and hasattr(event.content, "parts") and event.content.parts:
                text = event.content.parts[0].text
                print(f"Final response from sub-agent: {text}")
                results.append(text)
            else:
                print("Warning: event.content 為 None 或沒有 parts，略過此回應。")
    return results


if __name__ == "__main__":
    tasks_to_run = [
        {"name": "research AI", "prompt": "Research the latest advancements in AI.", "tool": 'arxiv_tool'},
        {"name": "research car", "prompt": "Research the latest advancements in car.", "tool": 'arxiv_tool'},
        {"name": "research structure", "prompt": "Research the latest advancements in structure.", "tool": 'arxiv_tool'}
    ]
    # The main execution block needs to use asyncio.run if called directly
    final_results = asyncio.run(run_taskagents(tasks_to_run))
    print("\n--- All tasks completed. Final results: ---")
    for result in final_results:
        print(result)

