from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the main page!"

@app.route('/admin')
def admin():
    return "Admin panel is hidden!"

@app.route('/login')
def login():
    return "Login page is hidden!"

@app.route('/config')
def config():
    return "Configuration settings are hidden!"

@app.route('/hidden')
def hidden():
    return "You found the hidden directory!"

@app.route('/private')
def private():
    return "Private information is hidden here."

@app.route('/secret')
def secret():
    return "You found the secret route!"

@app.route('/backup')
def backup():
    return "This is a backup route!"

@app.route('/.config/.backup')
def deep_backup():
    return "Deeply hidden backup!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
