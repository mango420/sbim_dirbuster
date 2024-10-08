from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'password123':
            return redirect(url_for('index'))
        else:
            return render_template('admin_error.html')

    return render_template('admin.html')

@app.route('/config')
def config():
    return "<h1>/config</h1>"

@app.route('/hidden')
def hidden():
    return "<h1>/hidden</h1>"

@app.route('/private')
def private():
    return "<h1>/private</h1>"

@app.route('/secret')
def secret():
    return "<h1>/secret</h1>"

@app.route('/backup')
def backup():
    return "<h1>/backup</h1>"

@app.route('/.config/.backup')
def deep_backup():
    return "<h1>/.config/.backup</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
