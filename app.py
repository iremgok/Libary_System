from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL Bağlantı Bilgileri (Burayı kendi veritabanınla değiştir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kullanici:1803@localhost:5432/LibarySystem'

db = SQLAlchemy(app)

CORS(app) # Tarayıcı engelini kaldırmak için

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Şimdilik basit bir kontrol yapalım, sonra veritabanına bağlarız
    if username == "irem" and password == "123":
        return jsonify({"status": "success", "message": "Hoş geldin!"})
    else:
        return jsonify({"status": "error", "message": "Kullanıcı adı veya şifre hatalı!"})

if __name__ == '__main__':
    app.run(debug=True)