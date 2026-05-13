from google.adk.agents import SequentialAgent
from .sub_agents.web_searcher import web_searcher
from .sub_agents.summarizer import summarizer

root_agent = SequentialAgent(
    #model='gemini-2.5-flash',
    name='news_summarizer_agent',
    description="An agent that searches for and summarizes news on a given topic.",
    sub_agents=[web_searcher,summarizer],
)
