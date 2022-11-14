import websocket

SOCKET_ENDPOINT = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    print('received msg')

ws = websocket.WebSocketApp(SOCKET_ENDPOINT, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
