from google.adk.agents.llm_agent import Agent

hashtag_generator_agent = Agent(
    model='gemini-2.5-flash',
    name='hashtag_generator_agent',
    description='A helpful assistant for generating hashtags for product marketing.',
    instruction="""
        Generate relevant and engaging hashtags for the provided product. 
        The hashtags should be trending and relevant to the product and its target audience.
    """
)
