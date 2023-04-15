import wikipedia

def wikipedia_search(query):
    try:
        # Set the language of the search results to English
        wikipedia.set_lang("en")

        # Search for the query on Wikipedia
        page = wikipedia.page(query)

        # Return the summary of the page
        return page.summary

    except:
        # If there's an error, return an error message
        return "Sorry, I couldn't find any information on that topic."
