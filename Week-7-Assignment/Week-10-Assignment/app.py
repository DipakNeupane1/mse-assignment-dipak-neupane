from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "<p>Hello, Flask!</p>"


#Can you use the following code and analyze it? 
 
#Sample code:
@app.route('/cal/<int:num>')
def show_square(num):
    return f"The square of {num} is {num**2}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)