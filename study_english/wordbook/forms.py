from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class WordBookForm(FlaskForm):
    title = StringField("タイトル", validators=[DataRequired()])
    picture = FileField("アイキャッチ画像", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    submit = SubmitField("作成")
        
        
class WordForm(FlaskForm):
    english = StringField("英語", validators=[DataRequired()])
    japanese = StringField("日本語", validators=[DataRequired()])
    submit = SubmitField("保存")


class UpdateWordForm(FlaskForm):
    english = StringField("英語", validators=[DataRequired()])
    japanese = StringField("日本語", validators=[DataRequired()])
    submit = SubmitField("更新")
    
    def __init__(self, word_id, *args, **kwargs):
        super(UpdateWordForm, self).__init__(*args, **kwargs)
        self.id = word_id
        
    
    
    
    
    