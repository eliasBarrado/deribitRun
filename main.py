from flask import Flask, request
from flask_socketio import SocketIO
import configparser
import DeribitWS



app = Flask(__name__)
socketio = SocketIO(app)

config = configparser.ConfigParser()
config.read('config.txt')
    
client_id = config['deribit-test']['ClientID']
client_secret = config['deribit-test']['ClientSecret']

ws = DeribitWS.DeribitWS(client_id=client_id, client_secret=client_secret, live=False)


@app.route('/market_order', methods=['POST'])
def market_order():

    params = request.get_json()

    print(params)

    instrument_name = params['instrument_name']
    quantity        = params['quantity']
    side            = params['side']

    resp = ws.market_order(instrument_name, quantity, side)
    return resp

@app.route('/get_index_price', methods=['POST'])
def get_index_price():

    params = request.get_json()

    index_name = params['index_name']

    resp = ws.get_index_price(index_name)
    return resp


@app.route('/get_positions', methods=['POST'])
def get_positions():

    params = request.get_json()

    currency = params['currency']
    kind     = params['kind']

    resp = ws.get_positions(currency, kind)

    return resp

@app.route('/test', methods=['GET','POST'])
def test():

    resp = ws.get_index_price('btc_usd')
    return str(resp['result']['index_price'])

"""
if __name__ == '__main__':

    
    socketio.run(app, host='0.0.0.0', port=8080, debug=False)
"""