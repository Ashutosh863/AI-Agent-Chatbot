from typing import TypedDict, List

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langgraph.graph import StateGraph, START, END

from tools import get_time, calculate
from memory import load_messages, save_messages
from config import GROQ_API_KEY


# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0
)

tools = [get_time, calculate]

llm_with_tools = llm.bind_tools(tools)


# Define state
class AgentState(TypedDict):
    session_id: str
    messages: List[BaseMessage]


# Agent node
def agent_node(state: AgentState):

    response = llm_with_tools.invoke(state["messages"])

    new_messages = state["messages"] + [response]

    return {
        "session_id": state["session_id"],
        "messages": new_messages
    }


# Create graph
graph = StateGraph(AgentState)

# Add node
graph.add_node("agent", agent_node)

# FIX: Add START edge
graph.add_edge(START, "agent")

# Add END edge
graph.add_edge("agent", END)

# Compile graph
agent_executor = graph.compile()


# Run agent function
def run_agent(session_id: str, message: str):

    history = load_messages(session_id)

    messages = []

    for msg in history:

        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))

        else:
            messages.append(AIMessage(content=msg["content"]))

    # add new message
    messages.append(HumanMessage(content=message))

    result = agent_executor.invoke({
        "session_id": session_id,
        "messages": messages
    })

    response = result["messages"][-1].content

    # save to postgres
    save_messages(session_id, "user", message)
    save_messages(session_id, "assistant", response)

    return response
