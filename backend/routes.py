from flask import current_app as app, render_template,request,send_file
from flask_security import auth_required,verify_password,hash_password
from flask import request, jsonify
from backend.models import db
from datetime import datetime
from backend.celery.tasks import add,create_csv
from celery.result import AsyncResult

datastore = app.security.datastore
cache = app.cache


@app.route('/',methods=['GET'])
def home():
        return render_template('index.html') #rendering the index.html file from the frontend folder


@app.get('/cache')
@cache.cached(timeout = 5)
def get_cache():  
    return {'time':str(datetime.now())}


@app.get('/celery')
def celery():
        task = add.delay(10,20)
        return {'task_id':task.id}

@app.get('/get-celery-data/<id>')
def getData(id):
        try:
            result = AsyncResult(id)
            if result.ready():
                return {'result': result.result}, 200
            else:
                return {'message':'task not ready', 'status': 'processing'}, 202
        except Exception as e:
            return {'error': 'Invalid task ID'}, 400
        
@auth_required('token')
@app.get('/create-csv')
def createCSV():
        task=create_csv.delay()
        return {'task_id':task.id},200
        
@app.get('/get-csv/<id>')
def getCSV(id):
    result = AsyncResult(id)

    if result.ready():
        return send_file(f'./backend/celery/user-downloads/{result.result}'), 200
    else:
        return {'message' : 'task not ready'}, 405


@app.route('/protected',methods=['GET'])
@auth_required('token') #specifies that this route requires authentication using a token
def protected():
        return "<h1>Hello, Protected Page! Only accessible by authenticate user</h1>"

@app.route('/login',methods=['POST'])
def login(): 
        data  = request.get_json()
        
        email = data.get('email') #we get error in this format data['email']
        password = data.get('password')
        username = data.get('username')
        if not email or not password or not username:
                return jsonify({"error":"Invalid Inputs"}), 404
        user=datastore.find_user(email=email,username=username)
        if not user:
                user=datastore.find_user(email=email)
                if not user:
                        user=datastore.find_user(username=username)
        if not user:
                return jsonify({"error":"User not found"}), 404     
        if verify_password(password, user.password):
                return jsonify({"token": user.get_auth_token(),'username':user.username,'email':user.email,'role':user.roles[0].name,'id':user.id}), 200
        return jsonify({"error":"Invalid password"}), 401 
@app.route('/register',methods=['POST'])        
def register():
        data = request.get_json()
        email = data.get('email')
        roles = data.get('roles')
        password = data.get('password')
        
        if not email or not password or roles not in ['admin', 'user']:
                return jsonify({"error":"Invalid Inputs"}), 404
                
        user = datastore.find_user(email=email)
        if user:
                return jsonify({"error":"User already exists"}), 404
                
        try:
                # Generate username from email (part before @)
                username = email.split('@')[0]
                # If username exists, append a number
                base_username = username
                counter = 1
                while datastore.find_user(username=username):
                    username = f"{base_username}{counter}"
                    counter += 1
                
                user_role = datastore.find_or_create_role(name=roles)
                user = datastore.create_user(
                    email=email,
                    username=username,  # Add generated username
                    password=hash_password(password),
                    roles=[user_role],
                    active=True
                )
                db.session.commit()
                return jsonify({"message": "User created successfully", "username": username}), 200
        except Exception as e:
                db.session.rollback()
                print(f"Registration error: {str(e)}")
                return jsonify({"error": str(e)}), 500