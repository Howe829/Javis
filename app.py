import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET",))
def index():
    words = request.args.get("w")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(words),
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    print(response.choices)
    return response.choices[0].text


# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.
#
# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )

def generate_prompt(animal):
    return """
    Human: Hello, who are you?
    Javis: I am an AI created by OpenAI. How can I help you today?
    Human: {}
    """.format(animal)
