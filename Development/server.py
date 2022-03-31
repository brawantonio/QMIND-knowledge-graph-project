from flask import Flask, render_template, send_file, request, json

# import scripts
from scripts.test import processText
from searchengine import search

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/styles.css")
def styles():
    return send_file("css/styles.css", mimetype="text/css")

@app.route("/logo_transparent.png")
def logo():
    return send_file("imgs/logo_transparent.png", mimetype="image/webp")

@app.route("/javascript.js")
def js():
    return send_file("scripts/javascript.js", mimetype="text/js")

@app.route("/test")
def test():
    
    text = request.args.get('text')

    data = processText(text)
    
    response = app.response_class(
            response=data,
            status=200,
            mimetype='application/text'
    )
    
    return response

@app.route("/searchengine")
def search_result_return():
    text = request.args.get('text')

    data = search(text)
    
    response = app.response_class(
            response=data,
            status=200,
            mimetype='application/text'
    )
    
    return response

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=True)