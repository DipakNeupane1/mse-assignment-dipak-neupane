from flask import Flask, request

app = Flask(__name__)


#Week 12 - Activity 3-  Develop a web APP - Temperature Converter (Celsius , Fahrenheit ,  Kelvin )
#Develop a web- APP to convert the temperature using the following table. (\frac{5}{9} => 5/9)
#Conversion	Formula
#Celsius -> Fahrenheit
#( F = (C × 9/5) + 32 )
#Fahrenheit -> Celsius
#( C = (F - 32) × \frac{5}{9} )
#Celsius -> Kelvin
#( K = C + 273.15 )
#Kelvin -> Celsius
#( C = K - 273.15 )
#Fahrenheit -> Kelvin
#( K = (F - 32) × 5/9 + 273.15 )
#Kelvin -> Fahrenheit
#( F = (K - 273.15) × 9/5 + 32 )

# Home route to show the Basic HTML form to take input from user
@app.route("/", methods=["GET"])
def home_page():
    return '''
        <body style="background-color: lightblue; text-align: center; padding-top: 100px; font-family: Arial;">
        <h2>Temperature Converter</h2>
        <form action="/convert" method="POST" style="color: blue;">
            <label for="temperature">Enter temperature to convert:</label>
            <input type="number" step="any" name="temperature" required>
            <select name="unit" required>
                <option value="celsius_to_fahrenheit">Celsius To Fahrenheit</option>
                <option value="fahrenheit_to_celsius">Fahrenheit To Celsius</option>
                <option value="celsius_to_kelvin">Celsius To Kelvin</option>
                <option value="kelvin_to_celsius">Kelvin To Celsius</option>
                <option value="fahrenheit_to_kelvin">Fahrenheit To Kelvin</option>
                <option value="kelvin_to_fahrenheit">Kelvin To Fahrenheit</option>
            </select>
            <button type="submit" style="color: blue;">Convert</button>
        </form>
        </body>
    '''

# Route to handle form submission
@app.route("/convert", methods=["POST"])
def convert_temperature():
    try:
        temperature = float(request.form["temperature"])
        unit = request.form["unit"]
    except (KeyError, ValueError):
        return "<p>Invalid input. Please enter a valid number.</p>"

    if unit == "celsius_to_fahrenheit":
        fahrenheit = (temperature * 9 / 5) + 32
        return f'''
        <body style="background-color: lightblue; text-align: center; padding-top: 100px; font-family: Arial;">
        <h2>Conversion Result</h2>
        <body style="color: blue;">
        <p>{temperature}°C is {fahrenheit:.2f}°F</p>
        </body>
        <a href="/">Convert another temperature</a>
         '''
    elif unit == "fahrenheit_to_celsius":
        celsius = (temperature - 32) * 5 / 9
        return f'''
        <body style="background-color: lightblue; text-align: center; padding-top: 100px; font-family: Arial;">
        <h2>Conversion Result</h2>
        <body style="color: blue;">
        <p>{temperature}°F is {celsius:.2f}°C</p>
        </body>
        <a href="/">Convert another temperature</a>
         '''
    elif unit == "celsius_to_kelvin":
        kelvin = temperature + 273.15
        return f'''
        <body style="background-color: lightblue; text-align: center; padding-top: 100px; font-family: Arial;">
        <h2>Conversion Result</h2>
        <body style="color: blue;">
        <p>{temperature}°C is {kelvin:.2f}K</p>
        </body>
        <a href="/">Convert another temperature</a>
         '''
    elif unit == "kelvin_to_celsius":
        celsius = temperature - 273.15
        return f'''
        <body style="background-color: lightblue; text-align: center; padding-top: 100px; font-family: Arial;">
        <h2>Conversion Result</h2>
        <body style="color: blue;">
        <p>{temperature}K is {celsius:.2f}°C</p>
        </body>
        <a href="/">Convert another temperature</a>
         '''
    elif unit == "fahrenheit_to_kelvin":
        kelvin = (temperature - 32) * 5 / 9 + 273.15
        return f'''
        <body style="background-color: lightblue; text-align: center; padding-top: 100px; font-family: Arial;">
        <h2>Conversion Result</h2>
        <body style="color: blue;">
        <p>{temperature}°F is {kelvin:.2f}K</p>
        </body>
        <a href="/">Convert another temperature</a>
         '''
    elif unit == "kelvin_to_fahrenheit":
        fahrenheit = (temperature - 273.15) * 9 / 5 + 32
        return f'''
        <body style="background-color: lightblue; text-align: center; padding-top: 100px; font-family: Arial;">
        <h2>Conversion Result</h2>
        <body style="color: blue;">
        <p>{temperature}K is {fahrenheit:.2f}°F</p>
        </body>
        <a href="/">Convert another temperature</a>
         '''
    else:
        return "<p>Invalid unit. Please select a valid unit.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)