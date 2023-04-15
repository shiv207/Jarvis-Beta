import openai

# Api Key
fileopen = open("Data\\Api.txt","r")
API = fileopen.read()
fileopen.close()

# Define a function to generate literature and poetry
def generate_text(prompt):
    # Use the OpenAI API to generate text
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Get the generated text from the API response
    generated_text = response.choices[0].text

    return generated_text