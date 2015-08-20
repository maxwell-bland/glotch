from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!, Your port number is, you guessed it, %s" % port

def ftoc(ftemp):
    return (ftemp-32.0)*(5.0/9.0)

@app.route('/ftoc/<ftempString>')
def convertFtoC(ftempString):
    ftemp = 0.0
    try:
        ftemp = float(ftempString)
        ctemp = ftoc(ftemp)
        return "In Farenheit: " + ftempString + " In Celsius: " + str(ctemp)
    except ValueError:
        return "Sorry. Could not convert your temperature into Celcius"

if __name__ == "__main__":
    port = 6969
    app.run(port=port)
