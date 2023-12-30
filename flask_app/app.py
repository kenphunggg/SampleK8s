from flask import Flask, redirect, url_for, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app=Flask(__name__)

@app.route('/')
def index():
  return f'hi, {os.getenv("SECRET_NAME")}'

@app.route('/forward')
def forward():
  return requests.get(f'{os.getenv("FORWARD_TO_POD_2")}').content

if __name__ == "__main__":
  app.run(debug=True)
