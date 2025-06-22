"""Root travel assistant agent following Google ADK pattern."""

from google.adk.agents import Agent
from ai_wanderize.flight_agent.agent import flight_booking_system
from ai_wanderize.hotel_agent.agent import hotel_booking_system
from ai_wanderize.activity_agent.agent import activity_booking_system
from ai_wanderize.local_experiences_agent.agent import local_experiences_system
from ai_wanderize.dining_agent.agent import dining_coordinator_system
from ai_wanderize.support_agent.agent import support_coordinator_system
from ai_wanderize.booking_agent.agent import booking_coordinator_system
from ai_wanderize.logistics_agent.agent import logistics_coordinator_system
from .prompt import WANDERIZE_TRAVEL_ASSISTANT_INSTR
from .config import DEFAULT_MODEL
from google.adk.tools.load_memory_tool import load_memory_tool

# Main travel assistant that coordinates travel-related requests
root_agent = Agent(
    name="wanderize_travel_assistant",
    model=DEFAULT_MODEL,
    description="Travel planning assistant specializing in flight, hotel, activity, local experience, dining, travel support, booking, and logistics coordination",
    instruction=WANDERIZE_TRAVEL_ASSISTANT_INSTR,
    sub_agents=[flight_booking_system, 
                hotel_booking_system,
                activity_booking_system,
                local_experiences_system,
                dining_coordinator_system,
                support_coordinator_system,
                booking_coordinator_system,
                logistics_coordinator_system
                ],
    tools=[load_memory_tool]
)
