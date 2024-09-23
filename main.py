from flask import Flask, render_template, request, jsonify
import os
import openai

app = Flask(__name__)


openai.api_key = "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"

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)

def get_Chat_response(text):
    for step in range(5):
       
        system_message = "You are a helpful assistant."
        user_message = text

        messages = [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]

       
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100,
            temperature=0.7,
        )

        response_text = response["choices"][0]["message"]["content"]
        return response_text

if __name__ == '__main__':
    app.run()

    