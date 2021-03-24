from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed, FileRequired
from wtforms.fields import TextAreaField, SelectField
from wtforms.validators import DataRequired
from wtforms import TextField

class AddPropertyForm(FlaskForm):
    title = TextField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired()])
    no_rooms = TextField('No.of.Rooms', validators=[DataRequired()])
    no_bathrooms = TextField('No.of.Bathrooms', validators=[DataRequired()])
    price = TextField('Price', validators=[DataRequired()])
    Type = SelectField('Property Type', choices=[("None","Select Type of Property"),("House","House"),("Apartment", "Apartment")], validators=[DataRequired()])
    location = TextField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png','Images only!'])])

