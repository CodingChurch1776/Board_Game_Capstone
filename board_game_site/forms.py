from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email



class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    submit_button = SubmitField()

class UserCollectionUpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    year = StringField('Year')
    rating = IntegerField('Rating (1-10)')
    designer = StringField('Designer')
    genre = StringField('Genre')
    submit_button = SubmitField()

class AtlasInfoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit_button = SubmitField()

#class UserBlogPostForm(FlaskForm):
    #message = StringField(validators=[DataRequired()])
    #submit_button = SubmitField()

#class UserBoardGameRankingSearch(FlaskForm):
    #game_name = StringField(validators=[DataRequired()])
    #year = StringField()
    #submit_button = SubmitField()


