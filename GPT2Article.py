""" 
Article Generator using GPT2 model
"""

# Import Libraries
from crypt import methods
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from flask import Flask, request, jsonify

# initializing App
app = Flask(__name__)


# setting up model
def set_model(TEXT):

    model = GPT2LMHeadModel.from_pretrained('jordan-m-young/buzz-article-gpt-2')
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    input_ids = tokenizer.encode(TEXT, return_tensors='pt')

    # Seed for result reproducibility, change to change outputs
    torch.manual_seed(10)

    sample_output = model.generate(
        input_ids, 
        do_sample=True, 
        max_length=300, 
        top_k=0,
        temperature=0.3
    )
    
    output = tokenizer.decode(sample_output[0], skip_special_tokens=False)
    return output.strip()

# the route point
@app.route('/', methods=['GET', 'POST'])
def route():
    return jsonify({"Greetings": "Welcome to Article Generator by Fahad Mahmood"})


# the output endpoint
@app.route('/generate', methods=['GET', 'POST'])
def generate():
    auth = request.headers['KEY']
    if auth == 'Fahad43':

        TextToCheckWith = request.form['text']
        output = set_model(TextToCheckWith)

        return jsonify({"Generated Article": output})
    else:
        return jsonify({"user-headers": "unauthorized"})


if __name__=="__main__":
    app.run(debug=True)
