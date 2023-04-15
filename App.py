import streamlit as st
import wikipedia
import datetime as dt
from Body.SpeakUI import streamspeak
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Features.WeatherApp import get_weather_data, print_weather_data
from Features.MoviePicker import get_random_movie_or_tv_show
from Features.Wikipedia import wikipedia_search
from Features.Poem_generator import generate_text
from Main import MainTaskExecution
import requests
import string
from bs4 import BeautifulSoup
from PIL import Image

# Define a function to handle user input
def handle_input(input_text):
    # Replace any periods in the input
    input_text = input_text.replace(".", "")

    # Call the MainTaskExecution function to handle the input
    ValueReturn = MainTaskExecution(input_text)

    # Check if ValueReturn is True or the input length is less than 3 characters
    if len(input_text) < 3:
        pass

    # Check if the input is a weather-related query
    elif "weather" in input_text:
        city = "Bangalore"  # Hardcoded for example
        data = get_weather_data(city)
        print_weather_data(data)

    # Check if the input is a music-related query
    elif "music" in input_text:
        from Features import playmusic
        playmusic()

    # Check if the input is a TV-related query
    elif "turn on the tv" in input_text:
        streamspeak("Ok..Turning On The Android TV")

    # Check if the input is a question
    elif "what is" in input_text or "where is" in input_text or "question" in input_text or "answer" in input_text:
        Reply = QuestionsAnswer(input_text)
        streamspeak(Reply)

    # Check if the input is a movie-related query
    elif "Moviepicker" in input_text:
        random_movie_or_tv_show = get_random_movie_or_tv_show()
        streamspeak(f"here's a good one: {random_movie_or_tv_show}")

    # Check if the input is a Wikipedia-related query
    elif "wikipedia" in input_text:
        query = input_text.replace("wikipedia", "").strip()

        # Get the Wikipedia summary for the query
        try:
            summary = wikipedia.summary(query, sentences=20)
        except wikipedia.exceptions.PageError:
            summary = "Sorry, no Wikipedia page was found for that query."
        except wikipedia.exceptions.DisambiguationError:
            summary = "Sorry, that query may refer to multiple pages. Please be more specific."
        # Print the summary in a separate text box
        st.text_area("Jarvis: Here is what I found on Wikipedia:", value=summary, height=400, max_chars=None)
        # Save the search in the sidebar
        st.sidebar.write(query)

    elif "generate letter" in input_text or "generate poem" in input_text:
            # Generate the text using the GPT-3 model
            generated_text = generate_text(input_text)
            # Display the generated text to the user
            st.text_area("Jarvis :", value=generated_text, height=500, max_chars=None)

    # Otherwise, use the ReplyBrain to generate a response
    else:
        Reply = ReplyBrain(input_text)
        streamspeak(Reply)

# Define the Streamlit app
def app():

    # Set the app webicon
    st.set_page_config(page_title="Jarvis", page_icon=":brain:")

    # Set the app title and icon
    col1, col2 = st.columns([0.5, 3])
    with col1:
        st.image("Data\\Jarvis.png", use_column_width=True)
    with col2:
        st.title("Jarvis")

    # Define the sidebar
    st.sidebar.title("Options 🧭")

    # Add a dropdown menu to categorize past searches
    categories = ["All 📚", "Entertainment 🎬", "Science 🚀", "Technology 💻", "Sports 🏀", "Literature 📖"]
    selected_category = st.sidebar.selectbox("Select a category", categories)

    # Add a search box for past queries
    past_queries = ["query 1", "query 2", "query 3"]
    selected_query = st.sidebar.selectbox("Select a past query", past_queries)

    # Add a suggestion panel to the sidebar
    st.sidebar.title("Suggestions 💡")
    st.sidebar.markdown("* Try asking me about the weather")
    st.sidebar.markdown("* Ask me a question")
    st.sidebar.markdown("* Try a movie recommendation")
    st.sidebar.markdown("* Search for something on Wikipedia")
    st.sidebar.markdown("* Ask me to write a poem")

    # Create a text input for the user to enter messages
    user_input = st.text_input("You:", key="input")

    # Check if the user has submitted any input
    if st.button("Send"):
        # Display the user's input in the chat
        st.text_area("You :", value=user_input, height=20, max_chars=None)

        # Call the handle_input function to handle the user's input
        handle_input(user_input)

        # Save the query to the appropriate category in the sidebar
        if selected_category != "All":
            st.sidebar.subheader(selected_category)
            st.sidebar.write(selected_query)



# Run the app
if __name__ == "__main__":
    app()