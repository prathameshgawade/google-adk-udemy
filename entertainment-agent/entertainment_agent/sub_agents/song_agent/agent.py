from google.adk.agents.llm_agent import Agent

song_agent = Agent(
    name="song_agent",
    model="gemini-2.5-flash",
    instruction="""
        Choose a random topic and write a 4 lines song.
        Return the control to entertainment agent after writing the song.""",
    description="An agent which is good at writing small songs",
)
