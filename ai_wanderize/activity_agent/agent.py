"""Activity booking agent and sub-agents, handling activity search, planning, and advisory."""

from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.load_memory_tool import load_memory_tool
from ai_wanderize.config import DEFAULT_MODEL, DEFAULT_GENERATION_CONFIG
from ai_wanderize.tools import toolset
from google.adk.tools.load_memory_tool import load_memory_tool
from .prompt import (
    ACTIVITY_PLANNER_INSTR,
    ACTIVITY_SEARCHER_INSTR,
    ACTIVITY_ADVISOR_INSTR,
    ACTIVITY_BOOKING_AGENT_INSTR
)   



# ============================================================================
# ACTIVITY SUB-AGENTS
# ============================================================================

activity_planner = Agent(
    model=DEFAULT_MODEL,
    name="activity_planner",
    description="Create detailed activity search plans from user requests.",
    instruction=ACTIVITY_PLANNER_INSTR,
)

activity_searcher = LlmAgent(
    model=DEFAULT_MODEL, 
    name="activity_searcher",
    description="Execute activity searches using web tools to find actual activities and experiences.",
    instruction=ACTIVITY_SEARCHER_INSTR,
    tools=[toolset],
)

activity_advisor = Agent(
    model=DEFAULT_MODEL,
    name="activity_advisor", 
    description="Provide personalized activity recommendations and itinerary guidance.",
    instruction=ACTIVITY_ADVISOR_INSTR,
)

# ============================================================================
# MAIN ACTIVITY BOOKING AGENT
# ============================================================================

activity_booking_system = Agent(
    model=DEFAULT_MODEL,
    name="activity_booking_system",
    description="Complete activity booking coordination handling planning, searching, and advisory services.",
    instruction=ACTIVITY_BOOKING_AGENT_INSTR,
    tools=[
        AgentTool(agent=activity_planner),
        AgentTool(agent=activity_searcher),
        AgentTool(agent=activity_advisor),
        load_memory_tool
    ],
    generate_content_config=DEFAULT_GENERATION_CONFIG
)