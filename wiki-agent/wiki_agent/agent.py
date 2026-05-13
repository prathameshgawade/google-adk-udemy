from google.adk.agents.llm_agent import Agent
from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


root_agent = Agent(
    model='gemini-2.5-flash',
    name='wiki_agent',
    description='A helpful assistant for answers users questions using Wikipedia.',
    instruction="""
    You are a helpful assistant for answers users questions using Wikipedia. 
    Use the WikipediaQueryRun tool available to you to find the information you need to get answer for user's question
    and always provide a concise and accurate answer.
    """, 
    tools=[
        LangchainTool(
            name='WikipediaQueryRun',
            description='Use this tool to query Wikipedia for information.',
            tool=WikipediaQueryRun(
                api_wrapper=WikipediaAPIWrapper()
            )
        )
    ]
)
