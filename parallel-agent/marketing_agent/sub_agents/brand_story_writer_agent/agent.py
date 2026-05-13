from google.adk.agents.llm_agent import Agent

brand_story_writer_agent = Agent(
    model='gemini-2.5-flash',
    name='brand_story_writer_agent',
    description="""
        You are an experinced marketing professional. 
        You are tasked with writing a compelling brand story based on the provided product in user input. 
    """,
    instruction="""
        Write a compelling brand story for the product provided in the user input.
        The brand story should be engaging, concise, and highlight the unique selling points of the product.
    """
)
