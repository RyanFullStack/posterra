from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class CommentForm(FlaskForm):
    created_by = IntegerField('created_by', validators=[DataRequired()])
    post_id = IntegerField('post_id', validators=[DataRequired()])
    comment_body = StringField('comment_body', validators=[DataRequired(), Length(max=255)])
