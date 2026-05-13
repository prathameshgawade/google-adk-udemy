from google.adk.agents.llm_agent import Agent


summarizer = Agent(
    model='gemini-2.5-flash',
    name='summarizer',
    instruction="""Summarize the content {{news_content}} shared by the previous agent and provide a summary in maximum 300 words""",
    description="An agent which is good at summarizing content shared with it",
)
