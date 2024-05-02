from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database (replace this with a real user database)
users = {
    "john": "password",
    "emma": "password123",
    "brian": "tycoon",
    "kipkosgei": "kipkosgei123"
}

# Login route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        return f"Welcome, {username}! Login successful"
    else:
        return "Invalid username or password. Please try again."
#POST

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')   
    if username in users:
        return "Username already exists. Please try again."
    else:
        users[username] = password
        return users #redirect(url_for('home')) 
    
    


if __name__ == '__main__':
    app.run(debug=True)