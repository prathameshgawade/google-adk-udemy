from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions. When asked about a specific topic, summarize the answer in bullet points, and provide a five lines crisp summary at the end.',
    instruction='Answer user questions to the best of your knowledge',
)
