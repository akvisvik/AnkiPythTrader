import websocket
import json

SOCKET_ENDPOINT = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    message_object = json.loads(message)
    msg_formatted_str = json.dumps(message_object,indent=2)
    print(msg_formatted_str)

    candle = message_object['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("Candle closed at {}".format(close))

ws = websocket.WebSocketApp(SOCKET_ENDPOINT, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
