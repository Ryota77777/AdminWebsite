from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from user_management.models import User
from urls import urls_blueprint
from user_management.init import db

# Создаем приложение Flask с указанием папки для шаблонов
app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
app.config['JSON_AS_ASCII'] = False

# Инициализируем SQLAlchemy с использованием настроек из объекта конфигурации
db.init_app(app)

# Регистрируем Blueprint для управления URL
app.register_blueprint(urls_blueprint, url_prefix='/urls')


# Обработчик для перенаправления на главную страницу
@app.route('/')
def index():
    return redirect(url_for('urls.index'))


# Обработчик регистрации нового пользователя
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Валидация длины пароля (минимум 8 символов)
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
        return redirect(url_for('urls.index'))

    return render_template('register.html')


# Обработчик входа пользователя
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return render_template('login.html', message='Ошибка входа. Пожалуйста проверьте ваш никнейм и пароль.')

        # Перенаправление на страницу пользователей после успешного входа
        return redirect(url_for('get_users'))

    return render_template('login.html')


# Обработчик вывода списка пользователей
@app.route('/users')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)


# Обработчик добавления нового пользователя
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('add_user.html', message='Такое имя пользователя уже существует!')

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return render_template('add_user.html', message='Пользователь успешно добавлен!')

    return render_template('add_user.html')


# Обработчик обновления информации о пользователе
@app.route('/user/<int:user_id>/update', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return render_template('update_user.html', message='Пользователь не найден.')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user.username = username
        user.password = generate_password_hash(password)

        db.session.commit()

        return render_template('update_user.html', user=user, message='Данные пользователя успешно обновлены!')

    return render_template('update_user.html', user=user)


# Обработчик удаления пользователя
@app.route('/user/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return render_template('users.html', message='Пользователь не найден.')

    db.session.delete(user)
    db.session.commit()

    users = User.query.all()
    return render_template('users.html', users=users, message='Пользователь удален!')


# Если скрипт запускается напрямую, а не импортируется как модуль
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание всех таблиц, если они еще не существуют в базе данных
    app.run(debug=True)  # Запуск приложения в режиме отладки
