from flask import request, jsonify
from models.user import User
from config.db import db
# from flask_jwt_extended import create_access_token, decode_token
import bcrypt
import jwt

def create_user():
    data = request.get_json()
    password = data['password']
    password_bytes = password.encode('utf-8')  # Encode the password as bytes
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    utf_decoded_hashed_password = hashed_password.decode('utf-8')
    new_user = User(user_name=data['user_name'], phone_number=data['phone_number'], email=data['email'],age=data['age'], password=utf_decoded_hashed_password)
    db.session.add(new_user)
    db.session.commit()
    updated_user_data = {"id": new_user.id, "user_name": new_user.user_name, "password":new_user.password ,"phone_number": new_user.phone_number, "email": new_user.email,"age": new_user.age}
    return jsonify({"message": "User created successfully!","user":updated_user_data}), 200

def findAll_user():
    allUsers = User.query.all()
    result = [{"id": allUserz.id, "user_name": allUserz.user_name, "phone_number": allUserz.phone_number, "email": allUserz.email} for allUserz in allUsers]
    return jsonify(result),200

def findOne_user(id):
     fetchOneUser = User.query.get(id)
     if fetchOneUser:
        # Create an access token with the user's ID as additional data
        # access_token = create_access_token(identity=str(fetchOneUser.id))
        
        # Include the access token in the response
        response_data = {
            "id": fetchOneUser.id,
            "user_name": fetchOneUser.user_name,
            "phone_number": fetchOneUser.phone_number,
            "email": fetchOneUser.email,
            "access_token": "access_token"  # Include the token here
        }
        
        return jsonify(response_data), 200
     else:
        return jsonify({"message": "User not found"}), 404
    
def update_user(id):
    fetchUser = User.query.get(id)
    if not fetchUser:
        return jsonify({"message":"User not found"}),404
    
    data = request.get_json()
    fetchUser.user_name = data['user_name']  
    fetchUser.email = data['email']
    db.session.commit()

    updated_user_data = {"id": fetchUser.id, "user_name": fetchUser.user_name, "phone_number": fetchUser.phone_number, "email": fetchUser.email}
    return jsonify({"message":"User update successfully","User":updated_user_data}),200 

def delete_user(id):
    deleteUser = User.query.get(id)
    if not deleteUser:
        return jsonify({"message":"User not found"}),404
    
    db.session.delete(deleteUser)
    db.session.commit()
    return jsonify({"message":"user deleted successfully"})

def user_login():
    # data = request.get_json()
    # password = data['password']
    # # Fetch the user by ID
    # fetchOneUser = User.query.get(data['id'])

    # if fetchOneUser:
    #     # Get the stored hashed password as bytes
    #     stored_password = fetchOneUser.password.encode('utf-8')  # Encode as bytes

    #     # Hash the fetched password using the same salt
    #     password_bytes = password.encode('utf-8')
        
    #     if bcrypt.checkpw(password_bytes, stored_password):
    #         # Passwords match; create an access token
    #         token = jwt.encode({
    #         'id': fetchOneUser.id,
    #         'user_name' : fetchOneUser.user_name 
    #          }, 'SECRET_KEY')
    #         # access_token = create_access_token(identity=identity_str)

    #         # Include the access token in the response
    #         response_data = {
    #             "id": fetchOneUser.id,
    #             "user_name": fetchOneUser.user_name,
    #             "phone_number": fetchOneUser.phone_number,
    #             "email": fetchOneUser.email,
    #             "access_token": token
    #         }
    #         return jsonify(response_data), 200
    #     else:
    #         return jsonify({"message": "Incorrect password"}), 401
    # else:
    payload = {"user_id": 123, "username": "example"}
    secret_key = "your-secret-key"
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    print(token)
    print(payload)
    # Decode a token
    decoded_payload = jwt.decode(token, secret_key, algorithms=["HS256"])
    print(decoded_payload)
    return jsonify({"message": "User not found"}), 404

def destructure_access_token():
    data = request.get_json()
    access_token = data['access_token']

    if not access_token:
        return jsonify({"message": "Access token not provided"}), 400

    try:
        # Decode the access token to get the payload
        decoded_token = decode_token(access_token)

        # Extract user details from the payload
        user_id = decoded_token['identity']
        # You can extract other user-related details as needed
        user_name = decoded_token.get('user_name', None)
        email = decoded_token.get('email', None)

        return jsonify({
            "user_id": user_id,
            "user_name": user_name,
            "email": email
        }), 200
    except Exception as e:
        # Handle any exceptions that may occur during decoding
        print(f"Error decoding access token: {str(e)}")
        return jsonify({"message": "Failed to decode access token"}), 500

