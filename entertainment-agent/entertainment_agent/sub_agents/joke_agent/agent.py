from google.adk.agents.llm_agent import Agent

joke_agent = Agent(
    name="joke_agent",
    model="gemini-2.5-flash",        
    instruction="""
        Tell a joke when asked.
        Return the control to entertainment agent after telling the joke.
    """,
    description="An agent which create jokes",
)
