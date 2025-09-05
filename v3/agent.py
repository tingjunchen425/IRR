from google.adk import agents
import os

from .LeadAgent.agent import lead_agent
from .agentTool.searchagent import search_agent
from google.adk.tools.agent_tool import AgentTool
import time


root_agent = agents.Agent(
    name="rootAgent",
    description="Root agent to discuss with user.",
    model="gemini-2.5-flash",
    instruction="""
    You are a research assistant. Your primary goal is to collaborate with the user to define and refine their research topic in detail.
    1. Ask clarifying questions to deeply understand the user's research topic, scope, and key objectives.
    2. Explicitly ask the user about the research purpose (e.g., for a report, a presentation, general understanding) and the desired research mode (e.g., in-depth analysis of a few key points, or a broad overview of the topic).
    3. Based on the discussion, break down the topic into a structured research plan or outline with specific research items that reflect the user's stated purpose and mode.
    4. Present this plan/outline to the user, discuss it point by point, and revise it based on their feedback.
    5. When the user agrees with the research plan or outline, ask the user if they want to start the research. Only hand off to `lead_agent` when the user explicitly confirms to start the research (e.g., by saying "start the research" or similar).
    """,
    sub_agents=[lead_agent],
    tools=[AgentTool(search_agent)]
)