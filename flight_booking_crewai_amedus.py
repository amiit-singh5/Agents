# flight_agent.py

import os
import json
from dotenv import load_dotenv
from amadeus import Client, ResponseError
from config import CONFIG, traveler,tools
from transformers import pipeline
import re

# ------- Tool: Get Credentials -------
def get_credentials():
    return {
        "API_KEY": os.getenv("AMADEUS_CLIENT_ID"),
        "API_SECRET": os.getenv("AMADEUS_CLIENT_SECRET")
    }

# ------- Tool: Initialize Amadeus Client -------
def init_amadeus():
    load_dotenv()  # Load from .env file
    return Client(
        client_id=os.getenv("AMADEUS_API_KEY"),
        client_secret=os.getenv("AMADEUS_API_SECRET")
    )


# ------- Tool: Search Flights -------
def search_flights(amadeus):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode="BLR",
            destinationLocationCode="JFK",
            departureDate="2025-06-15",
            adults=1,
            max=5
        )
        return response.data
    except Exception as e:
        print("Search error:", e)
        return []


# ------- Tool: Compare Flights -------
def compare_flights(offers):
    return min(offers, key=lambda x: float(x['price']['total'])) if offers else None

# ------- Tool: Book Flight -------
def book_flight(amadeus, offer):
    
    try:
        response = amadeus.booking.flight_orders.post(
            [offer],
            [traveler]
        )
        return response.data
    except Exception as e:
        print("Booking error:", e)
        return None

# ------- Use Open-Source LLM to Interpret Task -------
from transformers import pipeline

def summarize_ticket(ticket):
    offers = ticket.get('flightOffers', [])
    if not offers:
        return "No flight offers found in ticket."

    offer = offers[0]
    itinerary = offer['itineraries'][0]
    segments = itinerary['segments']
    details = []
    for seg in segments:
        dep = seg['departure']
        arr = seg['arrival']
        details.append(f"{dep['iataCode']} -> {arr['iataCode']} at {dep['at']} by {seg['carrierCode']} flight {seg['number']}")
    price = offer['price']['total']
    currency = offer['price']['currency']
    summary = "Flight segments:\n" + "\n".join(details) + f"\nTotal price: {price} {currency}"
    return summary

FUNCTION_REGISTRY = {
    "get_credentials": get_credentials,
    "search_flights": search_flights,
    "compare_flights": compare_flights,
    "book_flight": book_flight
}

def llm_task_executor(task_description):
   

    generator = pipeline("text2text-generation", model="google/flan-t5-small")

    prompt = """
You are an AI assistant. Your job is to provide a **comma-separated list** of functions needed to    complete the task.
You MUST ONLY choose from the following functions:
[get_credentials, search_flights, compare_flights, book_flight]

Task: Book the cheapest available flight from BLR to JFK.
Response:
"""

    result = generator(prompt, max_length=50, do_sample=False)[0]['generated_text']
    

    raw = result.strip()
    # Remove brackets if present
    cleaned = re.sub(r"[\[\]']", "", raw)
    actions = [a.strip() for a in cleaned.split(",")]

    print("LLM raw output:", repr(result))
   
    context = {"amadeus": init_amadeus()}
    for each in context:
        print("context : ",each)
    for action in actions:
        tool_conf = tools.get(action)
        if not tool_conf:
           print(f"⚠️ Unknown tool: {action}")
           continue

        func = FUNCTION_REGISTRY.get(action)
        if not func:
           print(f"⚠️ Function not registered: {action}")
           continue

        args = [context[arg] for arg in tool_conf["args"] if arg in context]

        if len(args) != len(tool_conf["args"]):
           print(f"⚠️ Skipping {action} due to missing inputs.")
           continue

        print(f"🔧 Executing tool: {action}")
        result = func(*args)

        if tool_conf["output"] and result is not None:
           context[tool_conf["output"]] = result
    """
    for action in actions:
        #tool = TOOLS.get(action)
        tool = TOOLS
        print(TOOLS)
        if not tool:
           print(f"⚠️ Unknown tool: {action}")
           continue

        func = tool["func"]
        args = [context[arg] for arg in tool["args"] if arg in context]
    
        # Guard against missing input
        if len(args) != len(tool["args"]):
           print(f"⚠️ Skipping {action} due to missing inputs.")
           continue

        print(f"🔧 Executing tool: {action}")
        result = func(*args)

        # Store result if output key is defined
        if tool["output"] and result is not None:
           context[tool["output"]] = result
    """

    if 'ticket' in context:
       ticket_summary = summarize_ticket(context['ticket'])
       print("\n🎫 Booked Ticket Details:")
       print(ticket_summary)
       return ticket_summary

    return None  # Add this for all other cases



if __name__ == "__main__":
    # Load config.json
    with open("config.json") as f:
        config_data = json.load(f)

    task_description = config_data.get("task", {}).get("description", "")
    result = llm_task_executor(task_description)
    print("LLM Response:", result)

