from flask import render_template
from flask_jwt_extended import jwt_required
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('admin.html')


@jwt_required
@app.route('/project-list')
def project_list():
    return render_template('project-list.html')


@jwt_required
@app.route('/project')
def project():
    return render_template('project.html')


@jwt_required
@app.route('/lead-list')
def lead_list():
    return render_template('lead-list.html')


@jwt_required
@app.route('/email-list')
def email_list():
    return render_template('email-list.html')


@jwt_required
@app.route('/email')
def email():
    return render_template('email.html')
