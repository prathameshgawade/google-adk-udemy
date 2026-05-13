from google.adk.agents.llm_agent import Agent

def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction='Perform add and multiply operations on two numbers. Use the tools provided to perform the calculations. If no input is provided, ask the user for two numbers and the operation to perform.',
    description='An agent that can perform addition and multiplication on two numbers.',
    tools={
        add_numbers, multiply_numbers
    }
)
