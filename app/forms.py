from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, FloatField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Length

class VehicleForm(FlaskForm):
    make = StringField('Make', validators=[DataRequired(), Length(max=50)])
    model = StringField('Model', validators=[DataRequired(), Length(max=50)])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1900, max=2100)])
    price = FloatField('Price ($)', validators=[DataRequired(), NumberRange(min=0)])
    mileage = IntegerField('Mileage', validators=[NumberRange(min=0)])
    fuel_type = SelectField('Fuel Type', choices=[
        ('', 'Select Fuel Type'),
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid')
    ])
    transmission = SelectField('Transmission', choices=[
        ('', 'Select Transmission'),
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic')
    ])
    color = StringField('Color', validators=[Length(max=30)])
    description = TextAreaField('Description')
    image = FileField('Vehicle Image', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
    ])
    is_available = BooleanField('Available for Sale', default=True)
    submit = SubmitField('Save Vehicle')

class InquiryForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    phone = StringField('Phone Number', validators=[Length(max=20)])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Inquiry')
