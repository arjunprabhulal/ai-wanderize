'''
Find dining options in Johns Creek for 3 adults, September 5-12, 2025. Interested in traditional Indian and vegetarian-friendly restaurants. One special birthday dinner, budget $50-200 per person. Need help with reservations.
'''

"""Dining agent and sub-agents, handling restaurant discovery, culinary experiences, and dining reservations."""

from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.load_memory_tool import load_memory_tool
from ai_wanderize.config import DEFAULT_MODEL, DEFAULT_GENERATION_CONFIG
from google.adk.tools.load_memory_tool import load_memory_tool
from .prompt import (
    RESTAURANT_DISCOVERY_INSTR,
    RESTAURANT_SEARCHER_INSTR,
    CUISINE_EXPERIENCE_INSTR,
    DINING_RESERVATION_INSTR,
    DINING_COORDINATOR_INSTR
)
from ai_wanderize.tools import toolset



# ============================================================================
# DINING SUB-AGENTS
# ============================================================================

restaurant_discovery_agent = Agent(
    model=DEFAULT_MODEL,
    name="restaurant_discovery_agent",
    description="Create detailed restaurant search plans from user dining requests.",
    instruction=RESTAURANT_DISCOVERY_INSTR,
)

restaurant_searcher = LlmAgent(
    model=DEFAULT_MODEL, 
    name="restaurant_searcher",
    description="Execute restaurant searches using web tools to find actual restaurants and dining options.",
    instruction=RESTAURANT_SEARCHER_INSTR,
    tools=[toolset],
)

cuisine_experience_agent = Agent(
    model=DEFAULT_MODEL,
    name="cuisine_experience_agent", 
    description="Provide culinary experience recommendations and dining strategy guidance.",
    instruction=CUISINE_EXPERIENCE_INSTR,
)

dining_reservation_agent = Agent(
    model=DEFAULT_MODEL,
    name="dining_reservation_agent", 
    description="Provide restaurant booking guidance and reservation coordination.",
    instruction=DINING_RESERVATION_INSTR,
)

# ============================================================================
# MAIN DINING COORDINATOR AGENT
# ============================================================================

dining_coordinator_system = Agent(
    model=DEFAULT_MODEL,
    name="dining_coordinator_system",
    description="Complete dining coordination handling restaurant discovery, culinary experiences, and reservation management.",
    instruction=DINING_COORDINATOR_INSTR,
    tools=[
        AgentTool(agent=restaurant_discovery_agent),
        AgentTool(agent=restaurant_searcher),
        AgentTool(agent=cuisine_experience_agent),
        AgentTool(agent=dining_reservation_agent),
        load_memory_tool
    ],
    generate_content_config=DEFAULT_GENERATION_CONFIG
)