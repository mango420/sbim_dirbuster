from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'batman':
            return render_template('index.html')
        else:
            return render_template('admin_error.html')

    return render_template('admin.html')


@app.route('/private')
def private():
    return "<h1>/private</h1>"

@app.route('/backup')
def backup():
    return "<h1>/backup</h1>"

@app.route('/secret', methods=['GET', 'POST'])
def secret():
    user_input = None
    if request.method == 'POST':
        user_input = request.form.get('user_input')
    return render_template('vulnerable.html', user_input=user_input)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
