# Описание проекта

Проект представляет собой простое веб-приложение для управления пользователями с использованием Flask. Целью приложения является предоставление интерфейса для регистрации новых пользователей, входа в систему, просмотра и управления списком пользователей.

## Скриншот
![](https://github.com/Ryota77777/blob/main/photo_2024-08-10_03-07-38.jpg?raw=true)

## Структура проекта

Структура проекта включает следующие основные компоненты:

- `app.py`: Основной файл приложения Flask, который инициализирует и настраивает приложение, включая подключение к базе данных.
- `config.py`: Файл конфигурации, где задаются настройки Flask и SQLAlchemy.
- `user_management/`: Пакет, содержащий модели и вспомогательные функции для управления пользователями.
  - `models.py`: Описывает модель данных для пользователей.
  - `__init__.py`: Инициализирует и объединяет компоненты приложения.
- `templates/`: Каталог с шаблонами HTML-страниц для представления пользовательского интерфейса.

## Технологии и библиотеки

Проект использует следующие технологии и библиотеки:

- **Flask**: Веб-фреймворк для Python, используемый для создания веб-приложений.
- **SQLAlchemy**: ORM (Object-Relational Mapping) для работы с базой данных SQL в Python.
- **Werkzeug**: Библиотека для безопасного хранения паролей и других утилит для работы с HTTP.
- **Bootstrap**: Фреймворк для разработки адаптивных и стильных пользовательских интерфейсов.

## Установка и запуск

### Установка зависимостей

Установите необходимые зависимости с помощью менеджера пакетов `pip`:

```bash
pip install -r requirements.txt

### Настройка конфигурации
Настройте конфигурацию в файле config.py, если это необходимо. Укажите параметры подключения к базе данных и другие настройки Flask.

Запуск приложения
Запустите приложение с помощью следующей команды:
python app.py

Приложение будет доступно по адресу http://localhost:5000/.

API и эндпоинты
Эндпоинты
POST /register: Регистрация нового пользователя.
POST /login: Вход в систему с проверкой имени пользователя и пароля.
GET /users: Получение списка всех зарегистрированных пользователей.
POST /user/add: Добавление нового пользователя в систему.
POST /user/<int:id>/update: Обновление данных пользователя по его идентификатору.
POST /user/<int:id>/delete: Удаление пользователя по его идентификатору.
Форматы запросов и ответов
Все эндпоинты работают с данными в формате JSON. Примеры запросов и ответов представлены в документации к API.

База данных
Структура базы данных
База данных содержит одну таблицу User с полями:

id: Целочисленный идентификатор пользователя (первичный ключ).
username: Имя пользователя (уникальное).
password: Хешированный пароль пользователя.

Импорт базы данных
Выполните следующие шаги:

Создайте новую базу данных в своем экземпляре PostgreSQL.
Создайте новую роль (пользователя) с правами на эту базу данных, если необходимо.
Импортируйте SQL-файл в новую базу данных.

Пример команды для импорта:
psql -U <new_user> -d <new_database> -f path_to_your_backup_file.sql
Где:

<new_user> — это новый пользователь (роль) на стороне работодателя.
<new_database> — это новая база данных, созданная для импорта.
path_to_your_backup_file.sql — это путь к вашему файлу резервной копии.


