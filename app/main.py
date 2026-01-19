from flask import Flask , request , render_template 
import os


Base_dir  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(Base_dir , "templates")

app = Flask(__name__ , template_folder=template_path)

@app.route('/' , methods = ["GET" , "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":
        text = request.form["spam-text"]
        return render_template("result.html" , text= text)



if __name__ == "__main__":
    app.run(debug=True)