# 🚀 Production AI Agent Chatbot (LangGraph + Groq + FastAPI + PostgreSQL + Streamlit)

A production-ready full-stack AI agent chatbot built using LangGraph,
Groq LLM, FastAPI, PostgreSQL, and Streamlit. This system supports
persistent chat memory, multi-session conversations, and scalable
deployment architecture.

------------------------------------------------------------------------

 ## Features

-    Production-ready AI agent using LangGraph
-    Ultra-fast inference using Groq API (Llama 3)
-    Persistent chat memory using PostgreSQL
-    Multi-session conversation support
-    FastAPI backend with REST API
-    Interactive Streamlit frontend
-    Tool-enabled agent (time, calculator)
-    Modular and scalable architecture
-    Deployment-ready structure

------------------------------------------------------------------------

##  Architecture

Frontend (Streamlit) → FastAPI Backend → LangGraph Agent → Groq LLM →
PostgreSQL

------------------------------------------------------------------------

##  Project Structure

ai-agent/ │ ├── backend/ │ ├── main.py │ ├── agent.py │ ├── db.py │ ├──
models.py │ ├── memory.py │ ├── tools.py │ ├── config.py │ └──
requirements.txt │ ├── frontend/ │ ├── app.py │ └── requirements.txt │
├── .env └── README.md

------------------------------------------------------------------------

##  Tech Stack

AI / LLM: - LangGraph - Groq API (Llama 3)

Backend: - FastAPI - Python - SQLAlchemy

Frontend: - Streamlit

Database: - PostgreSQL

Deployment: - Docker - Render / Streamlit Cloud

------------------------------------------------------------------------

##  Installation & Setup

1.  Clone Repository
2.  Create virtual environment
3.  Install backend requirements
4.  Setup PostgreSQL database
5.  Configure environment variables
6.  Create database tables
7.  Run FastAPI backend
8.  Run Streamlit frontend

------------------------------------------------------------------------

##  API Endpoint

POST /chat

Request: { "session_id": "123", "message": "Hello" }

Response: { "response": "Hello! How can I help you?" }

------------------------------------------------------------------------

##  Database Schema

Table: chat_messages

Columns: - id - session_id - role - content - created_at

------------------------------------------------------------------------

GitHub:

Repo : 
