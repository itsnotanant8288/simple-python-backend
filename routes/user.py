from flask import Blueprint
from controllers.user import create_user,findAll_user,findOne_user,update_user,delete_user,user_login, destructure_access_token

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def create():
    return create_user()

@user_bp.route('/users-findall',methods=['GET'])
def findAll():
    return findAll_user()

@user_bp.route('/users-findone/<int:id>',methods=['GET'])
def findOne(id):
    return findOne_user(id)

@user_bp.route('/users-update',methods=['POST'])
def update():
    return update_user


@user_bp.route('/delete-user',methods=['POST'])
def delete():
    return delete_user

@user_bp.route('/login',methods=['POST'])
def login():
    return user_login()

@user_bp.route('/destructure',methods=['POST'])
def destructure():
    return destructure_access_token()