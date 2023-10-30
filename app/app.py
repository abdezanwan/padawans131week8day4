from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_pyfile('config.py')  # Update the path to your configuration file if needed
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Import your models here (models.py)
from app.models import User, Book

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle user registration here (create User model and store in the database)
        username = request.form.get('username')
        password = request.form.get('password')
        # Add logic to create a user and save it to the database
        return redirect(url_for('login'))
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle user login here (validate credentials and generate JWT)
        username = request.form.get('username')
        password = request.form.get('password')
        # Add logic to validate user credentials and generate JWT
        access_token = create_access_token(identity=username)
        return jsonify(message='Login successful', access_token=access_token)
    return render_template('login.html')

# Reading list route
@app.route('/reading-list')
@jwt_required
def reading_list():
    # Fetch the user's reading list from the database
    user = User.query.filter_by(username=get_jwt_identity()).first()
    if user:
        reading_list = user.books.all()
    else:
        reading_list = []
    return render_template('index.html', reading_list=reading_list)

# Add book route
@app.route('/add-book', methods=['POST'])
@jwt_required
def add_book():
    # Handle adding a book to the reading list (create Book model and associate with the user)
    title = request.form.get('title')
    author = request.form.get('author')
    user = User.query.filter_by(username=get_jwt_identity()).first()
    if user:
        book = Book(title=title, author=author, user=user)
        db.session.add(book)
        db.session.commit()
        return jsonify(message='Book added to your reading list')
    else:
        return jsonify(message='User not found')

# Logout route
@app.route('/logout')
@jwt_required
def logout():
    # Handle user logout (if using JWT, it could involve token invalidation)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
