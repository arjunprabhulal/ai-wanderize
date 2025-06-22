"""Booking coordinator agent and sub-agents, handling payment processing, confirmations, and booking management."""

from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.load_memory_tool import load_memory_tool
from ai_wanderize.tools import toolset
from ai_wanderize.config import DEFAULT_MODEL, DEFAULT_GENERATION_CONFIG
from .prompt import (
    PAYMENT_PROCESSING_INSTR,
    CONFIRMATION_AGENT_INSTR,
    MODIFICATION_AGENT_INSTR,
    BOOKING_COORDINATOR_INSTR
)


payment_processing_agent = Agent(
    model=DEFAULT_MODEL,
    name="payment_processing_agent",
    description="Provide mock payment processing demonstrations and security education.",
    instruction=PAYMENT_PROCESSING_INSTR,
)

confirmation_agent = LlmAgent(
    model=DEFAULT_MODEL, 
    name="confirmation_agent",
    description="Provide booking confirmation management and verification assistance.",
    instruction=CONFIRMATION_AGENT_INSTR,
    tools=[toolset],
)

modification_agent = LlmAgent(
    model=DEFAULT_MODEL,
    name="modification_agent", 
    description="Provide booking modification, cancellation, and change management assistance.",
    instruction=MODIFICATION_AGENT_INSTR,
    tools=[toolset],
)

# ============================================================================
# MAIN BOOKING COORDINATOR AGENT
# ============================================================================

booking_coordinator_system = Agent(
    model=DEFAULT_MODEL,
    name="booking_coordinator_system",
    description="Complete booking coordination handling payment processing, confirmations, and modifications.",
    instruction=BOOKING_COORDINATOR_INSTR,
    tools=[
        AgentTool(agent=payment_processing_agent),
        AgentTool(agent=confirmation_agent),
        AgentTool(agent=modification_agent),
        load_memory_tool
    ],
    generate_content_config=DEFAULT_GENERATION_CONFIG
)