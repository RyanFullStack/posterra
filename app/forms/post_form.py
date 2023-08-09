from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    created_by = IntegerField('created_by', validators=[DataRequired()])
    community_id = IntegerField('community_id', validators=[DataRequired()])
    post_title = StringField('post_title', validators=[DataRequired()])
    post_body = StringField('post_body')
    ext_url = StringField('ext_url')
