from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "<p>Hello, Flask!</p>"

@app.route('/username/<string:name>')
def hello_user(name):
    return f"<p>{name} is learning flask!</p>"

#Can you use the following code and analyze it?
#Sample code:

@app.route('/cal/<int:num>')
def show_square(num):
    return f"The square of {num} is {num**2}"

#Week 12 - Activity 2 - Develop an initial Web APP

#Develop a Web Application to have Hyper link and load an image (from end user input) using Flask.

@app.route('/get-image', methods=['GET'])
def get_image():
    return '''
        <img src="https://via.placeholder.com/150" alt="Placeholder Image" width="150" height="150">
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)