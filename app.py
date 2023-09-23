from flask import Flask, redirect
from jinja2 import Template
from flask import request
from json import dumps
from database import Database
import smtplib
from asyncio import run
from threading import Thread
from os import listdir

app = Flask(__name__)
def template(file):
    with open(f'HTML/{file}.html', 'r') as f: return f.read()

@app.route("/News")
async def news():
    files   = ['0.10.11', '0.10.10', '0.10.9', 'Signalis-HD', '0.10.8b', '0.10.8', '0.10.7', '0.10.6']
    updates = [template(f'updates/{file}'.replace('.html', '')) for file in files]
    return Template(template('main')).render(updates=updates)

@app.route("/")
async def main():
    return redirect("/News", code=302)

if __name__ == '__main__': app.run()