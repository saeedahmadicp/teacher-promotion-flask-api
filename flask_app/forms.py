from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange

class InputForm(FlaskForm):
    firstName = StringField('First Name', validators=[InputRequired()])
    lastName = StringField('Last Name', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired(), NumberRange(min=-0, message='Enter a number greater than 0')])
    experience = IntegerField('Experience', validators=[InputRequired(), NumberRange(min=0, message='Enter a number greater than 0')])
    grade = IntegerField('Grade', validators=[InputRequired(), NumberRange(min=0, message='Enter a number greater than 0')])
    last_promotion = IntegerField('Last Promotion', validators=[InputRequired(), NumberRange(min=0, message='Enter a number greater than 0')])
    promo1 = RadioField('Promotion 1', choices=[
        ('M', 'M'),
        ('E', 'E'),
        ('E+', 'E+'),
        ('S', 'S'),
        ], validators=[InputRequired()], default='M')
    promo2 = RadioField('Promotion 2', choices=[
        ('M', 'M'),
        ('E', 'E'),
        ('E+', 'E+'),
        ('S', 'S'),
        ], validators=[InputRequired()], default='M')
    promo3 = RadioField('Promotion 3', choices=[
        ('M', 'M'),
        ('E', 'E'),
        ('E+', 'E+'),
        ('S', 'S'),
        ], validators=[InputRequired()], default='M')