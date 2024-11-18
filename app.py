from flask import Flask, request, jsonify
from flask_cors import CORS
import socket

app = Flask(__name__)

#cors allow all
CORS(app)



@app.route('/hostname', methods=['GET'])
def get_computer_name():
    client_ip = request.remote_addr
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    try:
        hostname, _, _ = socket.gethostbyaddr(client_ip)
        return jsonify({'client_ip': client_ip, 'hostname': hostname, 'found': True})
    except socket.herror:
        return jsonify({'client_ip': client_ip, 'error': 'Hostname not found', 'found': False}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8820)
