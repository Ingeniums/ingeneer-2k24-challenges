import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def search_roommates():
    data = request.form.copy()
    address = data.pop("address")

    if "--" in address  or "/*" in address or "#" in address:
        return render_template("hmmm.html")
    
    query = f"SELECT * FROM users LIMIT 5" if address == '' else f"SELECT * FROM users WHERE address = '{address}' LIMIT 5"
    try:
        conn = sqlite3.connect('file:db.sqlite?mode=ro', uri=True)
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
    except:
        return render_template("error.html")
    finally:
        cursor.close()
        
    return render_template("results.html", users = result, name = query)
    


