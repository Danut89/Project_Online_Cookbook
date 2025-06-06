from wtforms import SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from flask_wtf.file import FileAllowed, FileField
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    IntegerField,
    SelectField,
    SubmitField,
    PasswordField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    NumberRange,
    ValidationError,
)
from app.models import User, Category



# Custom widget for checkboxes
class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


# User Registration Form
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=50)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        """Check if username already exists in database."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "That username is already taken. Please choose a different one."
            )

    def validate_email(self, email):
        """Check if email already exists in database."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is already registered. Please log in.")


# User Login Form
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# Recipe Submission Form
class RecipeForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=3, max=255)])
    description = TextAreaField("Description", validators=[DataRequired()])
    ingredients = TextAreaField("Ingredients", validators=[DataRequired()])
    steps = TextAreaField("Steps", validators=[DataRequired()])
    cuisine = StringField("Cuisine", validators=[DataRequired(), Length(max=100)])
    prep_time = IntegerField(
        "Prep Time (minutes)", validators=[DataRequired(), NumberRange(min=1)]
    )
    difficulty = SelectField(
        "Difficulty",
        choices=[("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")],
        validators=[DataRequired()],
    )
    image = FileField(
        "Recipe Image", validators=[FileAllowed(["jpg", "png", "jpeg", "gif", "webp"])]
    )
    categories = MultiCheckboxField("Categories", coerce=int)
    submit = SubmitField("Add Recipe")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(FlaskForm):
    content = TextAreaField(
        "Add a Comment", validators=[DataRequired(), Length(min=1, max=1000)]
    )
    submit = SubmitField("Post Comment")


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=1000)])
    submit = SubmitField('Send Message')
