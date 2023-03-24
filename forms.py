from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class CreateForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()], id='id')
    url = StringField('url', id='url', validators=[DataRequired()])
    status = SelectField('status', choices=[(True, 'True'), (False, 'False')],
                         id='status', validators=[DataRequired()])
    submit = SubmitField('Создать')


class EditorForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()], id='id')
    url = StringField('url', id='url')
    status = SelectField('status', choices=[(True, "True"), (False, 'False')])
    submit = SubmitField('Изменить')
    delete = SubmitField('Удалить')

