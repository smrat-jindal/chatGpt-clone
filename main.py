from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
import openai



load_dotenv()

openai.api_key = os.getenv("OPEN_AI_KEY")

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URL")
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    # print(myChats)
    # print("nnnn", myChats[0]["question"])  testing the backend and db connection
    return render_template("index.html", param2 = myChats ) # supplying the data to the front end for display


@app.route("/api", methods= ("GET", "POST"))
def qa():
    if request.method == "POST":
        print(request.json)
        question= request.json.get("question")
        chat =mongo.db.chats.find_one({"question": question}) # searching question in db
        # chat ={"question": 'hey', "answer" : 'answer'} # searching question in db
        print(question,"  question")
        print(chat ,"  chat")
        if chat:
            data = {"question": question,"answer": f"{chat['answer']}"}  # need to understand this
            return  jsonify(data)
        else:
            response = openai.Completion.create(
              model="text-davinci-003",
              prompt= question,
              temperature=1,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
              )
            print(response)
            data = {"question": question, "answer": response["choices"][0]["text"]}  # getting data from open ai
            mongo.db.chats.insert_one({"question": question, "answer": response["choices"][0]["text"]}) # saving the data in db
            return  jsonify(data)
   
    data = {"result":"Hey"}
    return  jsonify(data)
app.run(debug=True)