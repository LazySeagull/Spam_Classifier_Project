from flask import Flask , request , render_template, redirect
import os
import joblib

Base_dir  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(Base_dir , "templates")
model_path = os.path.join(Base_dir , "models" , "spam_classifier_pipeline.pkl")


app = Flask(__name__ , template_folder=template_path)
model = joblib.load(model_path)

@app.route('/' , methods = ["GET" , "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":
        text = request.form["spam-text"]
        prediction = model.predict([text])[0]
        
        return render_template("result.html" , result=prediction , text=text)
        


if __name__ == "__main__":
    app.run(debug=False)