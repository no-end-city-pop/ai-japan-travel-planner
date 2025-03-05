import streamlit as st
import openai
import os

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_itinerary(destination, days, interests, budget):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI travel planner specializing in unique Japan travel experiences."},
            {"role": "user", "content": f"Plan a {days}-day itinerary for {destination} in Japan for travelers interested in {interests}. Budget level: {budget}."}
        ]
    )
    return response["choices"][0]["message"]["content"]

# Streamlit Web App
st.set_page_config(page_title="AI Japan Travel Planner", page_icon="🇯🇵", layout="wide")
st.title("AI Japan Travel Planner 🇯🇵")
st.write("Tailored travel itineraries for experienced Japan travelers looking for unique experiences.")

destination = st.text_input("Enter your destination (e.g., Kyoto, Tokyo, Fukuoka)")
days = st.slider("Select number of days", 1, 14, 5)
interests = st.text_area("Enter your travel interests (e.g., hidden temples, local izakayas, scenic hikes)")
budget = st.selectbox("Select your budget level", ["Budget", "Mid-range", "Luxury"])

if st.button("Generate Itinerary"):
    if not openai.api_key:
        st.error("OpenAI API key is missing. Please set the API key.")
    else:
        itinerary = generate_itinerary(destination, days, interests, budget)
        st.write("### Your Personalized Japan Travel Plan:")
        st.write(itinerary)
