# Copy of http://stackoverflow.com/a/20104705
from flask import Flask, render_template
from flask_sockets import Sockets
import sqlite3

app = Flask(__name__)
app.debug = True

sockets = Sockets(app)

myCon = sqlite3.connect("products.db",check_same_thread=False)
myCon.row_factory = sqlite3.Row
#myCursor = myCon.cursor()
#myCursor.execute("CREATE TABLE IF NOT EXISTS RESULTADOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,SUMANDO01 INTEGER NOT NULL,SUMANDO02 INTEGER NOT NULL, RESULTADO INTEGER)")

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message[::-1])

@app.route('/', methods=['POST', 'GET'])
def hello():
    return 'Hello World!'

@app.route('/products/')
def products():
    cur = myCon.cursor()
    cur.execute("SELECT * FROM PRODUCTS")
    rows = cur.fetchall()
    print(rows)
    #return 'Hello World!'

    text = """
    <form action='/' method='post'>
         <script src='https://static-content-qas.vnforapps.com/v2/js/checkout.js?qa=true'
         data-sessiontoken='b49505643c07a28eb0cd23d4738ac9ecab01426da0120188ac7b1bc47d3dea90'
         data-channel='web'
         data-merchantid='456879852'
        
         data-merchantlogo= 'https://www.manualweb.net/img/logos/html.png'
         data-formbuttoncolor='#D80000'
         data-purchasenumber='123'
         data-amount='20'
         data-expirationminutes='5'
         data-timeouturl = 'timeout.html'
         ></script>
        </form>
    """

    #return text
    return render_template("list.html",rows = rows, text = text)

@app.route('/echo_test', methods=['GET'])
def echo_test():
    return render_template('echo_test.html')

if __name__ == '__main__':
    app.run()