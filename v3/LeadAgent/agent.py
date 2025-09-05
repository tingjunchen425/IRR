import sys
import os
import time

# Add the project root directory to the Python path
# This allows for absolute imports from the 'v3' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from google.adk import agents
from agentTool.taskagent import run_taskagents
from agentTool.searchagent import search_agent
from google.adk.tools.agent_tool import AgentTool
from agentTool.reflectAgent import reflectAgent


# Construct the absolute path to prompt_zh.md
prompt_path = os.path.join(os.path.dirname(__file__), "prompt_zh.md")
with open(prompt_path, "r", encoding="utf-8") as f:
    system_prompt = f.read()
print(system_prompt)

lead_agent_instruction = f"""
current date: {time.strftime("%Y-%m-%d")}
You are a top-tier AI Research Manager. Your core mission is to manage sub-agents to deliver a complete and reliable report. You must follow the user's instructions and the core principles provided at the start of the conversation.
system prompt: {system_prompt}
"""

def compile_report(report_name, report_content):
    """
    Compiles the research report into a Markdown file.
    Args:
        report_name (str): The name of the report file (without extension).
        report_content (str): The content of the report.
    """
    os.makedirs("reports", exist_ok=True)
    with open(f"reports/{report_name}.md", "w") as f:
        f.write(report_content)

lead_agent = agents.Agent(
    name="leadAgent",
    description="lead agent to handle research tasks.",
    model="gemini-2.5-flash",
    instruction=f"""
    {lead_agent_instruction}
    """,
    tools=[run_taskagents,AgentTool(reflectAgent)],
)

