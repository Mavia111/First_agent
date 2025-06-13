import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api


load_dotenv()


gemini_api_key = os.getenv("APIKEY")
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gemini-2.0-flash")
while True:
    u_input = input("You: ")
    if u_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Chat ended.")
        break

    result = Runner.run_sync(agent, u_input)
    print("Assistant:", result.final_output)

