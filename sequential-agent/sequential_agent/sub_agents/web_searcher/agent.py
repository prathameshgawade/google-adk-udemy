from google.adk import Agent
from google.adk.tools import google_search

web_searcher = Agent(
    model='gemini-2.5-flash',
    name='web_searcher',
    description="An agent who checks in internet and gathers the latest news ",
    instruction="""You are a news researcher. When given a topic, search the web using the tools provided and return the results..""",
    tools=[google_search],
    output_key="news_content",
)
    