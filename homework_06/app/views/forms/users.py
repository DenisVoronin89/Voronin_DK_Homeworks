from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    name = StringField(
        label="User name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
        render_kw={"placeholder": "Desktop"},
    )
    short_description = StringField(
        "Short description",
        validators=[DataRequired()],
    )
