'''
"Plan my entire 5-day Rome trip: create detailed itinerary, coordinate all transportation, 
set up reminders, and optimize everything together"

'''

"""Logistics coordinator agent and sub-agents, handling itinerary creation, transportation coordination, reminders, and cross-service coordination."""

from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.load_memory_tool import load_memory_tool
from ai_wanderize.config import DEFAULT_MODEL, DEFAULT_GENERATION_CONFIG
from google.adk.tools.load_memory_tool import load_memory_tool
from .prompt import (
    ITINERARY_BUILDER_INSTR,
    TRANSPORTATION_AGENT_INSTR,
    REMINDER_AGENT_INSTR,
    COORDINATION_AGENT_INSTR,
    LOGISTICS_COORDINATOR_INSTR
)
from ai_wanderize.tools import toolset


# ============================================================================
# LOGISTICS SUB-AGENTS
# ============================================================================

itinerary_builder_agent = Agent(
    model=DEFAULT_MODEL,
    name="itinerary_builder_agent",
    description="Create comprehensive travel itineraries with day-by-day planning and optimization.",
    instruction=ITINERARY_BUILDER_INSTR,
)

transportation_agent = LlmAgent(
    model=DEFAULT_MODEL, 
    name="transportation_agent",
    description="Coordinate comprehensive transportation solutions for entire trips.",
    instruction=TRANSPORTATION_AGENT_INSTR,
    tools=[toolset],
)

reminder_agent = Agent(
    model=DEFAULT_MODEL,
    name="reminder_agent", 
    description="Provide comprehensive travel reminder and notification systems.",
    instruction=REMINDER_AGENT_INSTR,
)

coordination_agent = Agent(
    model=DEFAULT_MODEL,
    name="coordination_agent", 
    description="Provide cross-service coordination and trip optimization.",
    instruction=COORDINATION_AGENT_INSTR,
)

# ============================================================================
# MAIN LOGISTICS COORDINATOR AGENT
# ============================================================================

logistics_coordinator_system = Agent(
    model=DEFAULT_MODEL,
    name="logistics_coordinator_system",
    description="Complete logistics coordination handling itinerary creation, transportation planning, reminder systems, and cross-service coordination.",
    instruction=LOGISTICS_COORDINATOR_INSTR,
    tools=[
        AgentTool(agent=itinerary_builder_agent),
        AgentTool(agent=transportation_agent),
        AgentTool(agent=reminder_agent),
        AgentTool(agent=coordination_agent),  
        load_memory_tool
    ],
    generate_content_config=DEFAULT_GENERATION_CONFIG
)