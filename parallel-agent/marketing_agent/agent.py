from google.adk.agents import ParallelAgent
from .sub_agents.brand_story_writer_agent import brand_story_writer_agent
from .sub_agents.hashtag_generator_agent import hashtag_generator_agent

root_agent = ParallelAgent(
    #model='gemini-2.5-flash',
    name='marketing_agent',
    description="""
        You are an experinced marketing professional. 
        You run multiple parallel agents to generate a brand story and hashtags for a product based on user input. 
    """,
    sub_agents=[brand_story_writer_agent, hashtag_generator_agent]
)
