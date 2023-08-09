from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class CommunityForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    created_by = IntegerField('created_by', validators=[DataRequired()])
    description = StringField('description')
    logo_pic = StringField('logo_pic')
    banner_pic = StringField('banner_pic')
