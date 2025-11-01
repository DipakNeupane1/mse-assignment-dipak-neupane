from google import genai
from google.genai import types

API_KEY = "AIzaSyABRDSCRZH8kDtntGNL7N71g4rOxUWl91I"

def generate_itinerary(city, days, age, interests, budget):
    """Generate a structured travel itinerary using optimized prompt."""
    client = genai.Client(api_key=API_KEY)

    # Optimized prompt for Activity 2
    prompt = f"""
    You are a professional travel planner with global experience.
    Generate a {days}-day travel itinerary for {city}.
    Traveler details:
      - Age: {age}
      - Interests: {interests}
      - Budget: {budget}

    Output format:
    Day 1:
    - Activity 1: [Name, Address, Short description]
    - Activity 2: [Name, Address, Short description]
    - Activity 3: [Name, Address, Short description]

    Repeat for each day.
    Conclude with a recommendation for local cuisine or cultural experience.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a friendly, expert travel assistant.",
            temperature=0.7,
        ),
        contents=prompt,
    )

    return response.text


def main():
    print("\nWelcome to AI Travel Itinerary Generator\n")
    city = input("Enter destination city: ")
    days = input("Number of days: ")
    age = input("Your age: ")
    interests = input("Your interests (e.g., food, culture, adventure): ")
    budget = input("Budget level (low, medium, high): ")

    itinerary = generate_itinerary(city, days, age, interests, budget)

    print("\nHey!, Your Personalized Itinerary:\n")
    print(itinerary)


if __name__ == "__main__":
    main()