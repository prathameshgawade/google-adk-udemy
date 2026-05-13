from google.adk.agents.llm_agent import Agent

story_agent = Agent(
    name="story_agent",
    model="gemini-2.5-flash",
    instruction="""
        Choose a random topic and write a 10 lines story.
        Return the control to entertainment agent after writing the story.
    """,
    description="An agent which is good at writing small stories",
)
