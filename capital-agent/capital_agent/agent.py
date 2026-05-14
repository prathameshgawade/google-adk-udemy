from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field

class CountrySchema(BaseModel):
    """
        Schema for country information to be used as a input to the agent.
    """
    country : str = Field(description="The name of the country to get the capital of.")

class CapitalSchema(BaseModel):
    """
        Schema for capital information to be used as a output from the agent.
    """
    capital : str = Field(description="The capital city of the country user asked for.")

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant that answers with country capital.',
    instruction="""
        You are an agent which returns the capital of a country 
        when the country name provided in json format {"country": "Canada"}. 
        If the format is not maintained by user, suggest to use the json format. 
        When answering capital information, respond ONLY with a JSON object matching this exact schema: {json.dumps(CapitalSchema.model_json_schema(), indent=2)}Yo
    """,
    input_schema=CountrySchema,
    output_schema=CapitalSchema
)