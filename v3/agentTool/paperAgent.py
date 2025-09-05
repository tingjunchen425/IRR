from google.adk import agents
from .api_tool import arxiv_tool

paper_agent = agents.Agent(
    name="paperAgent",
    description="Agent to search and parse research papers.",
    model="gemini-2.5-flash",
    instruction="""
    You are a research paper assistant.
    Your task is to search for relevant papers on arXiv and extract their content.
    You should also summarize the key findings of the papers you read.
    """,
    tools=[arxiv_tool],
)
