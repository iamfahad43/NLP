"""
This will provide you an api that takes a sentence in json form as input and return an article of 200 words
"""

# Import Libraries
from crypt import methods
from transformers import pipeline
from flask import Flask, jsonify, request

app = Flask(__name__)

# function that setup GPT-Neo 125M model
def set_model(InputText, ModelName):
    generator = pipeline('text-generation', model=ModelName)
    generated_text = generator(InputText, do_sample=True, max_length=200)

    returnable = ""
    for i in generated_text:
        returnable = returnable + i['generated_text'].strip()
        print(i['generated_text'])
    
    return returnable.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({"Greetings": "Welcome to Article Generator @author=='Fahad Mahmood'"})

@app.route('/article-generator', methods=['POST'])
def article_generator():
    auth = request.headers['key']
    if auth == 'Fahad43':
        TextToCheckWith = request.form['text']
        output = set_model(TextToCheckWith, 'EleutherAI/gpt-neo-125M')
        return jsonify({"Output Article": output})
    else:
        return jsonify({"user-header": "unauthorized"})


if __name__=="__main__":
    app.run(debug=True)

