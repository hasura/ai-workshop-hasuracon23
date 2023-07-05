import query_llm
import event
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, request, jsonify

app = Flask("handlers")

@app.route('/query_llm', methods=['POST'])
def query_llm_handler():
    return jsonify(query_llm.query_llm(request.get_json(), request.headers))

@app.route('/handle_event', methods=['POST'])
def event_trigger_handler():
    return jsonify(event.handle_event(request.get_json()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8400)