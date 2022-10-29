from flask import Flask, request, render_template
from flask_cors import CORS
from jinja2 import Environment, FileSystemLoader
import json
import os
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/data", methods=["GET"])
def database_data():
    conn = sqlite3.connect('./database/product.db')
    data = conn.execute("SELECT ProductName FROM Products")
    name = []

    for row in data:
        databaseData =''
        for char in row:
            if char != '(' or char != ')' or char != "'":
                databaseData += char
        name.append(databaseData)

    data = conn.execute("SELECT Price FROM Products")
    price = []

    for row in data:
        databaseData =''
        for char in row:
            if char != '(' or char != ')' or char != "'":
                databaseData += char
        price.append(databaseData)

    data = conn.execute("SELECT Description FROM Products")
    description = []

    for row in data:
        databaseData =''
        for char in row:
            if char != '(' or char != ')' or char != "'":
                databaseData += char
        description.append(databaseData)

    productName1 = name[0],
    productName2 = name[1],
    productName3 = name[2],
    price1 = price[0],
    price2 = price[1],
    price3 = price[2],
    description1 = description[0],
    description2 = description[1],
    description3 = description[2]

    return {'productName1' : productName1,
    'productName2' : productName2,
    'productName3' : productName3,
    'price1' : price1,
    'price2' : price2,
    'price3' : price3,
    'description1' : description1,
    'description2' : description2,
    'description3' : description3, }

if __name__=="__main__":
    app.run(debug=True)