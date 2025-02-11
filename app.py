from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        msg = request.form.get("message")
        print("Received Message:", msg)
        return "Message received: " + msg  # Example response (Modify as needed)
    
    # If GET request, show predict.html
    return render_template("predict.html")

if __name__ == "__main__":  # Fixed the typo
    app.run(host="0.0.0.0", port=5050, debug=True)
