from google.adk.agents.llm_agent import Agent
from .sub_agents.joke_agent import joke_agent
from .sub_agents.song_agent import song_agent 
from .sub_agents.story_agent import story_agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='entertainment_agent',
    instruction="""
    You are a entertainer which uses other available agents to write stories, songs or jokes. 
        Instructions: 
        - Please greet the user and offer the services you provide and ask for thier choice 
        - Based on user preference use of the sub agents to get the output and present to the user
    """,
    description='A versatile entertainment agent that can create jokes, stories, and songs',
    sub_agents=[song_agent, story_agent, joke_agent]
)
