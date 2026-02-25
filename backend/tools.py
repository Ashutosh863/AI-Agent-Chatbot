from langchain_core.tools import tool
import datetime

@tool
def get_time():
    """Get current time"""
    return str(datetime.datetime.now())


@tool
def calculate(expression: str):
    """Calculate math expression"""
    return str(eval(expression))
