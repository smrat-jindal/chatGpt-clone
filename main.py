from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods= ("GET", "POST"))
def qa():
    if request.method == "POST":
        print(request.json)
        question= request.json.get("param1")
        data = {"result":f"Answer of {question}"}
        return  jsonify(data)
    # return render_template("index1.html")
    data = {"result":"Hey"}
    return  jsonify(data)
app.run(debug=True)