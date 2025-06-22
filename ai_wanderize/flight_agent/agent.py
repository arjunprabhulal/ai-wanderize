"""Flight booking agent and sub-agents for handling flight search, planning, and advisory services.

This module provides a comprehensive flight booking system with specialized agents:
- Flight planner: Creates detailed search plans
- Flight searcher: Executes web-based flight searches  
- Flight advisor: Provides recommendations and destination guides
- Flight booking system: Coordinates the complete workflow
"""

from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.load_memory_tool import load_memory_tool
from ai_wanderize.config import DEFAULT_MODEL, DEFAULT_GENERATION_CONFIG
from ai_wanderize.tools import toolset
from .prompt import (
    FLIGHT_PLANNER_INSTR,
    FLIGHT_SEARCHER_INSTR,
    FLIGHT_ADVISOR_INSTR,
    FLIGHT_BOOKING_AGENT_INSTR
)


# Specialized flight agents
flight_planner = Agent(
    model=DEFAULT_MODEL,
    name="flight_planner",
    description="Create detailed flight search plans from user requests.",
    instruction=FLIGHT_PLANNER_INSTR,
)

flight_searcher = LlmAgent(
    model=DEFAULT_MODEL, 
    name="flight_searcher",
    description="Execute flight searches using web tools to find actual flights.",
    instruction=FLIGHT_SEARCHER_INSTR,
    tools=[toolset],
)

flight_advisor = Agent(
    model=DEFAULT_MODEL,
    name="flight_advisor", 
    description="Provide personalized flight recommendations and destination guides.",
    instruction=FLIGHT_ADVISOR_INSTR,
)

# Main coordinating agent
flight_booking_system = Agent(
    model=DEFAULT_MODEL,
    name="flight_booking_system",
    description="Complete flight booking coordination handling planning, searching, and advisory services.",
    instruction=FLIGHT_BOOKING_AGENT_INSTR,
    tools=[
        AgentTool(agent=flight_planner),
        AgentTool(agent=flight_searcher),
        AgentTool(agent=flight_advisor),
        load_memory_tool
    ],
    generate_content_config=DEFAULT_GENERATION_CONFIG
)