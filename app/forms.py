from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):

    author = StringField('Post author',validators=[DataRequired()])
    category = TextAreaField('Post category', validators=[DataRequired()])
    content = TextAreaField('Post content', validators=[DataRequired()])
    submit = SubmitField('Submit')