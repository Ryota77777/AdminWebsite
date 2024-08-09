from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from user_management.init import db
from user_management.models import User

urls_blueprint = Blueprint('urls', __name__, template_folder='templates')


@urls_blueprint.route('/')
def index():
    return render_template('index.html')


@urls_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if len(password) < 8:
            flash('Пароль должен содержать, как минимум 8 символов', 'danger')
            return render_template('register.html')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Такое имя пользователя уже существует!', 'danger')
            return render_template('register.html')

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Регистрация пользователя успешна!', 'success')

        # Очистка полей формы регистрации
        return render_template('register.html')

    return render_template('register.html')


@urls_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return render_template('login.html', message='Ошибка входа. Пожалуйста проверьте ваш никнейм и пароль.')

        return redirect(url_for('urls.get_users'))

    return render_template('login.html')


@urls_blueprint.route('/users')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)
