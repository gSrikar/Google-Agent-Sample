from google.adk import Runner
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search

# Create a session Service
session_service = InMemorySessionService()

APP_NAME = "search_assistant"

root_agent = Agent(
    name=APP_NAME,
    model="gemini-2.0-flash-exp",
    instruction="You are a helpful assistant. Answer user questions using Google Search when needed.",
    description="An assistant that can search the web.",
    tools=[google_search]
)

runner = Runner(
    agent=root_agent,  # The agent we want to run
    app_name=APP_NAME,  # Associates runs with our app
    session_service=session_service  # Uses our session manager
)
