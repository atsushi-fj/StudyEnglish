from flask import request, send_file, current_app, send_from_directory
from flask_restful import Resource
from study_english.models import WordBook, Word
from study_english.image_handler import add_featured_image
from gtts import gTTS
from study_english import db
from sqlalchemy import func, and_
import os
import io


class CreateBookApi(Resource):
    
    def put(self, user_id):
        try:
            title = request.form.get("title")
            picture = request.files["picture"]
            if picture:
                pic = add_featured_image(picture)
            else:
                pic = ""
            wordbook = WordBook(title=title, featured_image=pic,
                                user_id=user_id)
            db.session.add(wordbook)
            db.session.commit()
            return {"status": "Create successful"}
        except:
            return {"status": "FAIL"}


class WordBookApi(Resource):
    
    def get(self, wordbook_id):
        try:
            wordbook = WordBook.query.get(wordbook_id)
            return {"is_public": wordbook.is_public}
        except:
            return {"status": "ERROR"}
        

class WordBooksApi(Resource):
    
    def get(self, user_id):
        try:
            page = int(request.args.get("page", 1))
            per_page = int(request.args.get("per_page", 10))
            wordbooks = WordBook.query.filter_by(user_id=user_id).order_by(
                WordBook.id.asc()).paginate(page, per_page, False)
            return {
                "total": wordbooks.total,
                "pages": wordbooks.pages,
                "current_page": wordbooks.page,
                "per_page": wordbooks.per_page,
                "wordbooks": [wordbook.to_dict() for wordbook in wordbooks.items],
            }
        except:
            return {"status": "ERROR"}
        
    def delete(self, user_id):
        try:
            data = request.get_json()
            book = WordBook.query.get(data["book_id"])
            db.session.delete(book)
            db.session.commit()
            return {"status": "SUCCESS"}
        except:
            return {"status": "ERROR"}
    
    def patch(self, user_id):
        try:
            data = request.get_json()
            book = WordBook.query.get(data["book_id"])
            book.is_public = not book.is_public
            db.session.commit()
            return {"is_public": str(book.is_public)}
        except:
            return {"status": "ERROR"}


class PublicWordBooksApi(Resource):
    
    def get(self):
        try:
            keyword = request.args.get("q", "")
            page = int(request.args.get("page", 1))
            per_page = int(request.args.get("per_page", 10))
            if keyword == "":
                wordbooks = WordBook.query.filter_by(is_public=True).order_by(
                    WordBook.id.desc()).paginate(page, per_page, False)
            else:
                wordbooks = WordBook.query.filter(and_(
                    WordBook.is_public == True,
                    WordBook.title.ilike(f'%{keyword}%'))).order_by(
                    WordBook.id.desc()).paginate(page, per_page, False)
                
            return {
                "total": wordbooks.total,
                "pages": wordbooks.pages,
                "current_page": wordbooks.page,
                "per_page": wordbooks.per_page,
                "wordbooks": [wordbook.to_dict() for wordbook in wordbooks.items],
            }
        except:
            return {"status": "ERROR"}


class ImageApi(Resource):
    
    def get(self, filename):
        try:
            folder = os.path.join(current_app.root_path, r"static/featured_image")
            return send_from_directory(folder, filename)
        except:
            return {"status": "ERROR"}


class WordsApi(Resource):
    
    def get(self, wordbook_id):
        try:
            page = int(request.args.get("page", 1))
            per_page = int(request.args.get("per_page", 10))
            num_words = Word.query.filter_by(book_id=wordbook_id).count()
            wordbook = WordBook.query.filter_by(id=wordbook_id).first()
            user_id = wordbook.user_id
            if request.args.get("sort_option") == "random":
                words = Word.query.filter_by(book_id=wordbook_id).order_by(
                    func.random()).distinct().paginate(page, per_page, False)
            elif request.args.get("sort_option") == "asc":
                words = Word.query.filter_by(book_id=wordbook_id).order_by(
                    Word.id.asc()).paginate(page, per_page, False)
            else:
                words = Word.query.filter_by(book_id=wordbook_id).order_by(
                    Word.id.desc()).paginate(page, per_page, False)
            return {
                "user_id": str(user_id),
                "num_words": num_words,
                "total": words.total,
                "pages": words.pages,
                "current_page": words.page,
                "per_page": words.per_page,
                "words": [word.to_dict() for word in words.items],
            }
        except:
            return {"status": "ERROR"}


class AllWordsApi(Resource):
    
    def get(self, wordbook_id):
        try:
            words = Word.query.filter_by(book_id=wordbook_id).order_by(Word.id.desc())
            return {"words": [word.to_dict() for word in words]}
        except:
            return {"status": "ERROR"}


class WordApi(Resource):
    
    def put(self, wordbook_id):
        try:
            data = request.get_json()
            if Word.query.filter_by(book_id=wordbook_id, english=data["english"]).first():
                return {"status": "English FAIL"}
            word = Word(japanese=data["japanese"], english=data["english"], book_id=wordbook_id)
            db.session.add(word)
            db.session.commit()
            return {"status": "Create successful"}
        except:
            return {"status": "FAIL"}
        
    def delete(self, wordbook_id):
        try:
            data = request.get_json()
            word = Word.query.get(data["word_id"])
            db.session.delete(word)
            db.session.commit()
            return {"status": "SUCCESS"}
        except:
            return {"status": "ERROR"}


class SpeakApi(Resource):
    
    def post(self):
        try:
            data = request.get_json()
            tts = gTTS(data["text"], lang="en")
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            return send_file(mp3_fp, mimetype="audio/mp3")
        except:
            return {"status": "ERROR"}