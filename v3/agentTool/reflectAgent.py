
from google.adk.runners import Runner
from google.adk import agents
from google.adk.tools import google_search
import dotenv
import uuid
import time
import os

dotenv.load_dotenv()

prompt_path = os.path.join(os.path.dirname(__file__), "reflectAgent_prompt.md")
with open(prompt_path, "r", encoding="utf-8") as f:
    prompt = f.read()

reflectAgent = agents.Agent(
        name=f"reflectAgent",
        description=f"Sub-agent to reflect the draft",
        model="gemini-2.5-flash",
        instruction=f"""
        current date: {time.strftime("%Y-%m-%d")}
        {prompt}
        """,
        tools=[google_search]
    )