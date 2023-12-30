from flask import Flask, redirect, url_for, render_template, request
import requests

app=Flask(__name__)

@app.route('/')
def index():
  return 'hello world 2'

@app.route('/forward')
def forward():
  return requests.get(f'{os.getenv("FORWARD_TO_POD_1")}').content

if __name__ == "__main__":
  app.run(debug=True)
