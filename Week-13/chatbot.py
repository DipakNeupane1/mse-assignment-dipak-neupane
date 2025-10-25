from google import genai
from google.genai import types


API_KEY = "AIzaSyBLwA681HtHN11OEtgTYYgtBqovqdafGto"

def generate_itinerary(city, days, age, interests, budget):
    # Pass API key when creating the gen AI client
    client = genai.Client(api_key=API_KEY)

    prompt = f"""
    You are a professional travel planner.
    Create a detailed {days}-day travel itinerary for {city}.
    Traveler is {age} years old with interests in {interests} and a {budget} budget.
    Include 3 activities per day with names, addresses, and short descriptions.
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
    print("\nWelcome to AI Travel Itinerary Generator \n")
    city = input("Enter destination city: ")
    days = input("Number of days: ")
    age = input("Your age: ")
    interests = input("Your interests (e.g., food, culture, adventure): ")
    budget = input("Budget level (low, medium, high): ")

    itinerary = generate_itinerary(city, days, age, interests, budget)

    print("\nYour Personalized Itinerary:\n")
    print(itinerary)


if __name__ == "__main__":
    main()