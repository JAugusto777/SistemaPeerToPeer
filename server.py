import os
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Estrutura para armazenar usuários e seus arquivos
connected_users = {}
shared_files = {}

# Diretório onde os arquivos serão salvos
SHARE_DIR = 'shareLists'

# Cria o diretório de compartilhamento caso não exista
if not os.path.exists(SHARE_DIR):
    os.makedirs(SHARE_DIR)

# Carregar arquivos compartilhados salvos
def load_shared_files():
    if os.path.exists('shared_files.json'):
        with open('shared_files.json', 'r') as f:
            return json.load(f)
    return {}

# Salvar arquivos compartilhados em um arquivo JSON
def save_shared_files():
    with open('shared_files.json', 'w') as f:
        json.dump(shared_files, f)

shared_files = load_shared_files()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    user_id = data.get('user_id')
    address = data.get('address')
    
    # Armazena o usuário
    connected_users[user_id] = address
    return jsonify({"status": "registered", "user_id": user_id}), 200

@app.route('/share', methods=['POST'])
def share_file():
    data = request.json
    user_id = data.get('user_id')
    file_name = data.get('file_name')

    if user_id in connected_users:
        # Salva a informação do arquivo compartilhado
        if file_name not in shared_files:
            shared_files[file_name] = []
        shared_files[file_name].append(user_id)
        save_shared_files()
        return jsonify({"status": "file_shared", "file_name": file_name}), 200
    return jsonify({"error": "User not registered"}), 400

@app.route('/files', methods=['GET'])
def get_files():
    return jsonify(shared_files), 200

@app.route('/download/<file_name>', methods=['GET'])
def download_file(file_name):
    # Verifica se o arquivo está na pasta shareLists
    file_path = os.path.join(SHARE_DIR, file_name)
    if os.path.exists(file_path):
        return send_from_directory(SHARE_DIR, file_name)
    return jsonify({"error": "File not found"}), 404

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
