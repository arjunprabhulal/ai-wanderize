"""Hotel booking agent and sub-agents, handling hotel search, planning, and advisory."""

from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.load_memory_tool import load_memory_tool
from ai_wanderize.config import DEFAULT_MODEL, DEFAULT_GENERATION_CONFIG
from ai_wanderize.tools import toolset
from .prompt import (
    HOTEL_PLANNER_INSTR,
    HOTEL_SEARCHER_INSTR,
    HOTEL_ADVISOR_INSTR,
    HOTEL_BOOKING_AGENT_INSTR
)



# ============================================================================
# HOTEL SUB-AGENTS
# ============================================================================

hotel_planner = Agent(
    model=DEFAULT_MODEL,
    name="hotel_planner",
    description="Create detailed hotel search plans from user requests.",
    instruction=HOTEL_PLANNER_INSTR,
)

hotel_searcher = LlmAgent(
    model=DEFAULT_MODEL, 
    name="hotel_searcher",
    description="Execute hotel searches using web tools to find actual hotels.",
    instruction=HOTEL_SEARCHER_INSTR,
    tools=[toolset],
)

hotel_advisor = Agent(
    model=DEFAULT_MODEL,
    name="hotel_advisor", 
    description="Provide personalized hotel recommendations and location guides.",
    instruction=HOTEL_ADVISOR_INSTR,
)

# ============================================================================
# MAIN HOTEL BOOKING AGENT
# ============================================================================

hotel_booking_system = Agent(
    model=DEFAULT_MODEL,
    name="hotel_booking_system",
    description="Complete hotel booking coordination handling planning, searching, and advisory services.",
    instruction=HOTEL_BOOKING_AGENT_INSTR,
    tools=[
        AgentTool(agent=hotel_planner),
        AgentTool(agent=hotel_searcher),
        AgentTool(agent=hotel_advisor),
        load_memory_tool
    ],
    generate_content_config=DEFAULT_GENERATION_CONFIG
)