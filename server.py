from flask import Flask, request, render_template
from jinja2 import Environment, FileSystemLoader
import os
import sqlite3

app = Flask(__name__)

@app.route("/product")
def update_table():
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('catalog.js')

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


    filename = os.path.join(root, '../Frontend/src/components/pages/', 'catalog.js')
    with open(filename, 'w') as fh:
        fh.write(template.render(
            productName1 = name[0],
            productName2 = name[1],
            productName3 = name[2],
            price1 = price[0],
            price2 = price[1],
            price3 = price[2],
            description1 = description[0],
            description2 = description[1],
            description3 = description[2],
        ))
    return render_template("catalog.js")


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

    return(productName1,productName2,productName3,price1,price2,price3,description1,description2,description3)


if __name__=="__main__":
    app.run(debug=True)