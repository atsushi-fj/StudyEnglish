from flask import render_template, url_for, redirect, session, flash, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint
from study_english.models import WordBook, Word
from study_english import db
from study_english.wordbook.forms import WordBookForm, WordForm
from study_english.wordbook.image_handler import add_featured_image


wordbook = Blueprint("wordbook", __name__)

@wordbook.route("/<int:user_id>/my_wordbooks")
@login_required
def my_wordbooks(user_id):
    page = request.args.get("page", 1, type=int)
    wordbooks = WordBook.query.filter_by(user_id=user_id).order_by(
        WordBook.id.desc()).paginate(page, per_page=10)
    return render_template("wordbook/my_wordbooks.html", wordbooks=wordbooks)


@wordbook.route("/<int:user_id>/create_wordbook", methods=["GET", "POST"])
@login_required
def create_wordbook(user_id):
    form = WordBookForm()
    if form.validate_on_submit():
        if form.picture.data:
            pic = add_featured_image(form.picture.data)
        else:
            pic = ""
        wordbook = WordBook(title=form.title.data, featured_image=pic, 
                            user_id=user_id)
        db.session.add(wordbook)
        db.session.commit()
        flash("新しい英単語帳を作成しました")
        return redirect(url_for("wordbook.my_wordbooks", user_id=current_user.id))
    return render_template("wordbook/create_wordbook.html", form=form)


@wordbook.route("/<int:wordbook_id>/my_words")
@login_required
def my_words(wordbook_id):
    page = request.args.get("page", 1, type=int)
    words = Word.query.filter_by(book_id=wordbook_id).order_by(
        Word.id.desc()).paginate(page, per_page=10)
    return render_template("wordbook/my_words.html", words=words)


@wordbook.route("/<int:wordbook_id>/create_word", methods=["GET", "POST"])
@login_required
def create_word(wordbook_id):
    form = WordForm()
    if form.validate_on_submit():
        word = Word(english=form.english.data,
                    japanese=form.japanese.data,
                    book_id=wordbook_id)
        db.session.add(word)
        db.session.commit()
        flash("新しい英単語を保存しました")
        return redirect(url_for("wordbook.my_wordbooks", user_id=current_user.id))
    return render_template("wordbook/create_word.html", form=form)
        