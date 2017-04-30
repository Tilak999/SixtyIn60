from flask import Flask
import dbHelper as db
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    news = db.getLast(60)
    news = news.reverse() # reverse list required by the App
    json_str = json.dumps(news, indent=2)
    return json_str

if __name__ == '__main__':
    app.run()