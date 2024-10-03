from flask import Flask, request, jsonify
import openai
from key import key

app = Flask(__name__)

openai.api_key = key

@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    data = request.json
    response = openai.ChatCompletion.create(
        model=data['model'],
        messages=data['messages']
    )
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000) 

