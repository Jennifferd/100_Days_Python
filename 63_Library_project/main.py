from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# Create Database
class Base(DeclarativeBase):
    pass


# Create extension
db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
app.config['SECRET_KEY'] = "any-string-you-want-just-keep-it-secret"
Bootstrap5(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class BookForm(FlaskForm):
    title = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    add = SubmitField('Add Book')


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Create table schema in database
with app.app_context():
    db.create_all()


all_books1 = []


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        with app.app_context():
            db.create_all()
            new_book = Book(title=request.form["title"],
                            author=request.form["title"],
                            rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

