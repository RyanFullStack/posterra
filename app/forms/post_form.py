from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    created_by = IntegerField('created_by', validators=[DataRequired()])
    community_id = IntegerField('community_id', validators=[DataRequired()])
    post_title = StringField('post_title', validators=[DataRequired(), Length(min=10, max=255)])
    post_body = StringField('post_body', validators=[Length(max=1000)])
    ext_url = StringField('ext_url')
