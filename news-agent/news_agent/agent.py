from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Look for all the latest news on the web and provide a crisp summary on the topic to the user.',
    instruction='An agent that uses Google search to find the latest news on the web and provides a crisp summary on the topic to the user.',
    tools=[google_search]
)
