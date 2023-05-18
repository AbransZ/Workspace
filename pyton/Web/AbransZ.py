from flask import Flask

app - flask(__name__)

@app.@app.route('/')
def home():
    return'hola mundo'

if __name__=='__main':
    app.run()
    