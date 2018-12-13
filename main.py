from flask import Flask, redirect, url_for, request
import en_core_web_sm
import spacy
import re
import json

	
nlp = spacy.load('en_core_web_sm')
app = Flask(__name__)


        
@app.route("/", methods=['POST'])
def parse_text():

    print('hello')
    
    input = request.get_json()
    print(input)
    sentence = json.dumps(input)
    
    

    doc = nlp(sentence)    
    sentence = doc.text

    spacyEnts = ['PERSON', 'ORG', 'CARDINAL','DATE', 'NUM']

    for ent in doc.ents:
            if ent.label_ in spacyEnts:
                sentence = re.sub(ent.text, '**PII**', sentence)
                sentence = re.sub(r'[^@\s]+@[^@\s]+\.[^@\s]+', '**PII**', sentence)

   
    return sentence


if __name__ == "__main__":
    app.debug = True
    app.run()