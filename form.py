from calendar import month, weekday
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set a secret key for CSRF protection

class MyForm(FlaskForm):
    Seller_Type_Individual = StringField('Seller_Type_Individual', validators=[DataRequired(), Length(min=2, max=20)])
    Car_Model = StringField('Car_Model',validators=[DataRequired(), Length(min=2, max=20)])
    Mileage = IntegerField('Mileage', validators=[DataRequired(), Length(min=2, max=20)])
    Fuel_Type_Petrol = StringField('Fuel_Type_Petrol',validators=[DataRequired(), Length(min=2, max=20)])
    Registration = StringField('Registration', validators=[DataRequired(), Length(min=2, max=20)])
    Year = IntegerField('Year',validators=[DataRequired(), Length(min=2, max=20)])
    
    
    submit = SubmitField('submit')

@app.route('/', methods=['POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        flash(f'Hello, {form.name.data}!', 'success')
        return redirect(url_for('index.'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)