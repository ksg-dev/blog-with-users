from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[InputRequired()])
    subtitle = StringField("Subtitle", validators=[InputRequired()])
    img_url = StringField("Blog Image URL", validators=[InputRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[InputRequired()])
    submit = SubmitField("Submit Post")


# Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email",
                        validators=[
                            InputRequired()
                        ]
                        )
    name = StringField("Name",
                       validators=[
                           InputRequired()
                       ]
                       )
    password = StringField("Password",
                           validators=[
                               InputRequired()
                           ]
                           )
    submit = SubmitField("Sign Up")

# Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    password = StringField("Password", validators=[InputRequired()])
    submit = SubmitField("Log In")

# TODO: Create a CommentForm so users can leave comments below posts
