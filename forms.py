from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, IntegerField
from wtforms.validators import DataRequired, InputRequired

class InputForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    experinence = IntegerField('Experience', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    last_promotion = StringField('Last Promotion', validators=[DataRequired()])
    promo1 = RadioField('Promotion 1', choices=[
        ('M', 'M'),
        ('E', 'E'),
        ('E+', 'E+'),
        ('S', 'S'),
        ], validators=[InputRequired()])
    promo2 = RadioField('Promotion 2', choices=[
        ('M', 'M'),
        ('E', 'E'),
        ('E+', 'E+'),
        ('S', 'S'),
        ], validators=[InputRequired()])
    promo3 = RadioField('Promotion 3', choices=[
        ('M', 'M'),
        ('E', 'E'),
        ('E+', 'E+'),
        ('S', 'S'),
        ], validators=[InputRequired()])