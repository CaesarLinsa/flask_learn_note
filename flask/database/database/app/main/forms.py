from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Length,Regexp, EqualTo


class LoginForm(Form):
    username = StringField(label=u'用户名', validators=[DataRequired(message="数据不能为空")])
    password = PasswordField(label=u'密码', validators=[DataRequired(message="数据不能为空")])
    submit = SubmitField(label=u'提交')
