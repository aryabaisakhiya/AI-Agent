# app.py

from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set Groq credentials (loaded from .env)
os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"

# Simple tool for mood-based suggestion
def mood_checker(query: str) -> str:
    if "anxious" in query.lower():
        return "Consider doing breathing exercises, journaling, or talking to a therapist."
    elif "depressed" in query.lower():
        return "Try light physical activity, reach out to friends, or consult a professional."
    else:
        return "Stay strong. I recommend mindfulness, good sleep, and healthy routines."

tools = [
    Tool(
        name="Mood Checker",
        func=mood_checker,
        description="Gives mental health suggestions based on the user's mood."
    )
]

# LLM model from Groq
llm = ChatOpenAI(model="llama3-8b-8192", temperature=0.7)

# Create agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye. Take care of your mental health 💚")
        break
    response = agent.run(user_input)
    print("AI:", response)
