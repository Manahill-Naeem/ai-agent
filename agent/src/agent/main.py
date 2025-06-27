from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import os

def firstagent():
    load_dotenv()
    set_tracing_disabled(True)
    provider = AsyncOpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash-exp",
        openai_client=provider
    )
    Agent1 = Agent(
        name="Assistant",
        instructions="you are helpful assistant that solves basic math problem.",
        model=model
    )
    response = Runner.run_sync(
    starting_agent=Agent1,
    # input="What is 5 + 10?",
    input="Hello how are you?",
    )
    print(response.final_output)