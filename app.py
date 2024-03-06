from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    # Here you can add code to store the registration details in a database
    return f"Registration successful! Username: {username}, Password: {password}"

if __name__ == '__main__':
    app.run(debug=True)
