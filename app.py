from flask import Flask, render_template, request, jsonify
import pickle
from some_module import TextToNum  # Ensure you have the correct module

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        msg = request.form.get("message")
    else:  # Handle GET requests
        msg = request.args.get("tweet")  

    if not msg:
        return jsonify({"error": "No message provided"}), 400  # Return error if no input

    # Text Processing
    ob = TextToNum(msg)
    ob.cleaner()
    ob.token()
    ob.removeStop()
    st = ob.stemme()
    stem_vector = " ".join(st)

    # Load Vectorizer
    try:
        with open("vectorizer.pickle", "rb") as vc:
            vectorizer = pickle.load(vc)
        vcdata = vectorizer.transform([stem_vector]).toarray()
    except Exception as e:
        return jsonify({"error": f"Vectorizer Error: {str(e)}"}), 500

    # Load Model & Predict
    try:
        with open("model.pickle", "rb") as mc:
            model = pickle.load(mc)
        pred = model.predict(vcdata)
    except Exception as e:
        return jsonify({"error": f"Model Error: {str(e)}"}), 500

    return jsonify({"prediction": int(pred[0])})  # Return prediction as JSON

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

app=Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")
@app.route("/predict",methods=["POST","GET"])

def predict():
    if request.method=="POST":
        msg=request.form.get("message")
        print(msg)
        ob=TextToNum(msg)
        ob.cleaner()
        ob.token()
        ob.removeStop()
        st=ob.stemme()
        stem_vector=" ".join(st)

        with open("vectorizer.pickle","rb") as vc:
            vectorizer=pickle.load(vc)
        vcdata=vectorizer.transform([stem_vector]).toarray()
        print(vcdata)
        
        with open("model.pickle","rb") as mc:
            model=pickle.load(mc)

        pred=model.predict(vcdata)
        print(pred)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5050)
    
