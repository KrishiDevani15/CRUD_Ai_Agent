# agent/agent.py
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from app.agents.tools import (
    add_stock_tool,
    read_stock_tool,
    delete_stock_tool,
    get_all_stock_tool,
)

llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o"
)

agent = initialize_agent(
    tools=[add_stock_tool, read_stock_tool,get_all_stock_tool,delete_stock_tool],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)
