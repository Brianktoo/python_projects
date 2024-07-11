from flask import Blueprint, request, jsonify, render_template
from app.models import User

user_bp = Blueprint("user_bp", __name__)


# Dummy user database (replace this with a real user database)


# Login route
@user_bp.route('/')
def home():
    return render_template('index.html')

@user_bp.route('/register')
def regr():
    return render_template('register.html')
#dashboard route
@user_bp.route('/dashboard')
def dashboard():
    #check if user is logged in if 
    return render_template('dashboard.html')

@user_bp.route('/login_user', methods=['POST'])
def login():
    user = User()
    data = request.get_json()
    print(data)
    username = data.get('username')
    password = data.get('password')
    
    result = user.login_user(username, password)
    if result:
        return jsonify({"message": "Login successful", "status": 200})
    
    else:
        return jsonify({"message": "Invalid username or password", "status": 401}) # Invalid username or password
   
@user_bp.route('/register_user', methods=['POST'])
def register():
    user = User()
    print(f"user info: {user}")
       # Get data from the rsequest object
    data = request.get_json()
    username = data.get('username')
    password = data.get('password') 
    #add confirm password 
    new_record =user.register_user(username, password)
    if new_record==False: 
        return jsonify({"message": "Username already exists", "status": 400})  # User already exists in the database
    return jsonify({"message": "User created successfully", "status": 200}) # User created successfullys
@user_bp.route('/update_user_password', methods=['PATCH'])
def update_user_password():
     data =request.get_json()
     username =data.get('username')
     password =data.get('password')
     update_user = User().update_password_By_username(username, password)
     if update_user:
         return jsonify({"message": "password updated successfully", "status": 201})
     else:
          return jsonify({"message": "password not successfully udated", "status": 401})
         
   
    

    
         
       