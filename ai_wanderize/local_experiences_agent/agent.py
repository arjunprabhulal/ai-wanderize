'''
Find local experiences in Barcelona for 2 adults, traveling September 10-15, 2025. 
Interested in authentic local dining, neighborhood cafés where locals go, hidden 
tapas bars, and cultural immersion with local artists. Budget €30-80 per experience. 
Want high authenticity - avoid tourist areas. English-speaking guides preferred.
'''

"""Local experiences agent and sub-agents, handling authentic local discovery, cultural immersion, and community connections."""

from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.load_memory_tool import load_memory_tool
from ai_wanderize.config import DEFAULT_MODEL, DEFAULT_GENERATION_CONFIG
from google.adk.tools.load_memory_tool import load_memory_tool
from .prompt import (
    LOCAL_PLANNER_INSTR,
    LOCAL_SEARCHER_INSTR,
    LOCAL_ADVISOR_INSTR,
    LOCAL_BOOKING_AGENT_INSTR
)

from ai_wanderize.tools import toolset

# ============================================================================
# LOCAL EXPERIENCES SUB-AGENTS
# ============================================================================

local_planner = Agent(
    model=DEFAULT_MODEL,
    name="local_planner",
    description="Create detailed authentic local experience search plans from user requests.",
    instruction=LOCAL_PLANNER_INSTR,
)

local_searcher = LlmAgent(
    model=DEFAULT_MODEL, 
    name="local_searcher",
    description="Execute searches for authentic local experiences, hidden gems, and cultural immersion opportunities.",
    instruction=LOCAL_SEARCHER_INSTR,
    tools=[toolset],
)

local_advisor = Agent(
    model=DEFAULT_MODEL,
    name="local_advisor", 
    description="Provide authentic local experience recommendations and cultural immersion guidance.",
    instruction=LOCAL_ADVISOR_INSTR,
)

# ============================================================================
# MAIN LOCAL EXPERIENCES AGENT
# ============================================================================

local_experiences_system = Agent(
    model=DEFAULT_MODEL,
    name="local_experiences_system",
    description="Complete local experiences coordination handling authentic discovery, cultural immersion planning, and community connections.",
    instruction=LOCAL_BOOKING_AGENT_INSTR,
    tools=[
        AgentTool(agent=local_planner),
        AgentTool(agent=local_searcher),
        AgentTool(agent=local_advisor),
        load_memory_tool
    ],
    generate_content_config=DEFAULT_GENERATION_CONFIG
)