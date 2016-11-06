# -*- coding: utf-8 -*-

from flask import Flask, render_template
import dataset

db = dataset.connect('mysql://root@192.168.33.21/kaitai')

app = Flask(__name__)

@app.route("/tokyo.html")
def tokyo():

    table = db['kaitai']
    result = table.find_one(city='tokyo')
    return render_template('tokyo.html', result=result)

@app.route("/seirei.html")
def seirei():

    table = db['kaitai']
    results = table.find(city='*')
    for seirei in results:

      return render_template('seirei.html', results=seirei)

if __name__ == "__main__":
    app.run(host='0.0.0.0')



