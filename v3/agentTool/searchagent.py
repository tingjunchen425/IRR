from google.adk import agents

from google.adk.tools import google_search

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