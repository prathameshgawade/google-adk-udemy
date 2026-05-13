from google.adk.agents.llm_agent import Agent
from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import ScrapeWebsiteTool

# Define the tools that the agent can use
scrape_news_tool = CrewaiTool(
    name='scrape_bbc_news',
    description='Scrape news articles from the BBC website.',
    tool = ScrapeWebsiteTool("https://www.bbc.com/news")
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful news assistant to get news from the BBC website.',
    instruction='Provide the latest news articles from the BBC website when asked using the tools provided.',
    tools=[scrape_news_tool]
)
