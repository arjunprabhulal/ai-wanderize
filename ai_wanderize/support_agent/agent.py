"""
I need immediate travel support assistance in Johns Creek, Atlanta area. I'm staying here without a car and need help finding essential local services. Specifically, I need to locate a pharmacy for medications, a grocery store for food supplies, and a laundromat for washing clothes. I also need to buy a phone charger urgently. Please provide directions, operating hours, and transportation options to reach these places using public transit or walking. This is practical travel assistance I need for my stay.
"""

"""Travel support agent and sub-agents, handling navigation, emergency assistance, local support, and language help."""

from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.load_memory_tool import load_memory_tool
from ai_wanderize.config import DEFAULT_MODEL, DEFAULT_GENERATION_CONFIG
from google.adk.tools.load_memory_tool import load_memory_tool
from .prompt import (
    NAVIGATION_AGENT_INSTR,
    EMERGENCY_SUPPORT_INSTR,
    LOCAL_ASSISTANCE_INSTR,
    LANGUAGE_SUPPORT_INSTR,
    SUPPORT_COORDINATOR_INSTR
)
from ai_wanderize.tools import toolset

# ============================================================================
# SUPPORT SUB-AGENTS
# ============================================================================

navigation_agent = Agent(
    model=DEFAULT_MODEL,
    name="navigation_agent",
    description="Provide real-time navigation assistance and routing guidance.",
    instruction=NAVIGATION_AGENT_INSTR,
)

emergency_support_agent = LlmAgent(
    model=DEFAULT_MODEL, 
    name="emergency_support_agent",
    description="Provide 24/7 emergency assistance and crisis support for travelers.",
    instruction=EMERGENCY_SUPPORT_INSTR,
    tools=[toolset],
)

local_assistance_agent = LlmAgent(
    model=DEFAULT_MODEL,
    name="local_assistance_agent", 
    description="Provide on-ground local support and practical travel assistance.",
    instruction=LOCAL_ASSISTANCE_INSTR,
    tools=[toolset],
)

language_support_agent = Agent(
    model=DEFAULT_MODEL,
    name="language_support_agent", 
    description="Provide translation assistance and communication support.",
    instruction=LANGUAGE_SUPPORT_INSTR,
)

# ============================================================================
# MAIN SUPPORT COORDINATOR AGENT
# ============================================================================

support_coordinator_system = Agent(
    model=DEFAULT_MODEL,
    name="support_coordinator_system",
    description="Complete travel support coordination handling navigation, emergency assistance, local support, and language help.",
    instruction=SUPPORT_COORDINATOR_INSTR,
    tools=[
        AgentTool(agent=navigation_agent),
        AgentTool(agent=emergency_support_agent),
        AgentTool(agent=local_assistance_agent),
        AgentTool(agent=language_support_agent),
        load_memory_tool
    ],
    generate_content_config=DEFAULT_GENERATION_CONFIG
)