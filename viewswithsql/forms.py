from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Pupy')
    submit = SubmitField("add puppy")

class DelForm(FlaskForm):
    id = IntegerField('Id Number of pupy to remove')
    submit = SubmitField("kill dog")