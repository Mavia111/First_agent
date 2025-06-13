import os
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

load_dotenv()
gemini_api_key = os.getenv("APIKEY")

print("Agentic Level")
client = AsyncOpenAI(
   api_key=gemini_api_key,
   base_url="https://generativelanguage.googleapis.com/v1beta/openai/"

)
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)

set_tracing_disabled(disabled=True)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )

    result = await Runner.run(
        agent,
        "write a easy on my self",
    ) 
    print(result)


if __name__ == "__main__":
    asyncio.run(main())