from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    answer = StringField("Ответ: ", validators=[DataRequired()])
    submit = SubmitField("Проверить")