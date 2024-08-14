from flask import render_template, url_for, redirect, session, flash, request, abort
from flask_login import login_required, current_user
from flask import Blueprint
from study_english.models import WordBook, Word
from study_english import db
from study_english.wordbook.forms import WordBookForm, WordForm
from study_english.wordbook.image_handler import add_featured_image


wordbook = Blueprint("wordbook", __name__)

# @wordbook.route("/<int:user_id>/my_wordbooks")
# @login_required
# def my_wordbooks(user_id):
#     page = request.args.get("page", 1, type=int)
#     wordbooks = WordBook.query.filter_by(user_id=user_id).order_by(
#         WordBook.id.desc()).paginate(page, per_page=10)
#     return render_template("wordbook/my_wordbooks.html", wordbooks=wordbooks)


# @wordbook.route("/<int:user_id>/create_wordbook", methods=["GET", "POST"])
# @login_required
# def create_wordbook(user_id):
#     form = WordBookForm()
#     if form.validate_on_submit():
#         if form.picture.data:
#             pic = add_featured_image(form.picture.data)
#         else:
#             pic = ""
#         wordbook = WordBook(title=form.title.data, featured_image=pic, 
#                             user_id=user_id)
#         db.session.add(wordbook)
#         db.session.commit()
#         flash("新しい英単語帳を作成しました")
#         return redirect(url_for("wordbook.my_wordbooks", user_id=current_user.id))
#     return render_template("wordbook/create_wordbook.html", form=form)


# @wordbook.route("/<int:wordbook_id>/my_words")
# @login_required 
# def my_words(wordbook_id):
#     wordbook = WordBook.query.get_or_404(wordbook_id)
#     if wordbook.user_id != current_user.id:
#         abort(403)
#     page = request.args.get("page", 1, type=int)
#     words = Word.query.filter_by(book_id=wordbook_id).order_by(
#         Word.id.desc()).paginate(page, per_page=10)
#     return render_template("wordbook/my_words.html", words=words, wordbook_id=wordbook_id)


# @wordbook.route("/<int:wordbook_id>/create_word", methods=["GET", "POST"])
# @login_required
# def create_word(wordbook_id):
#     wordbook = WordBook.query.get_or_404(wordbook_id)
#     if wordbook.user_id != current_user.id:
#         abort(403)
#     form = WordForm()
#     if form.validate_on_submit():
#         word = Word(english=form.english.data,
#                     japanese=form.japanese.data,
#                     book_id=wordbook_id)
#         db.session.add(word)
#         db.session.commit()
#         flash("新しい英単語を保存しました")
#         return redirect(url_for("wordbook.my_wordbooks", user_id=current_user.id))
#     return render_template("wordbook/create_word.html", form=form)


# @wordbook.route("/<int:word_id>/delete_word", methods=["GET", "POST"])
# @login_required
# def delete_word(word_id):
#     word = Word.query.get_or_404(word_id)
#     book_id = word.book_id
#     db.session.delete(word)
#     db.session.commit()
#     return redirect(url_for("wordbook/my_words.html", wordbook_id=book_id), )


# @wordbook.route("/<int:word_id>/update_word", methods=["GET", "POST"])
# def update_word(word_id):
#     word = Word.query.get_or_404(word_id)
#     form = WordForm()
#     if form.validate_on_submit():
#         word.english = form.english.data
#         word.japanese = form.japanese.data
#         db.session.commit()
#         flash("英単語が更新されました")
#         return redirect(url_for("wordbook.my_words", user_id=current_user.id, wordbook_id=word.book_id))
#     elif request.method == "GET":
#         form.english.data = word.english
#         form.japanese.data = word.japanese
#     return render_template("wordbook/update_word.html", form=form)




    
        