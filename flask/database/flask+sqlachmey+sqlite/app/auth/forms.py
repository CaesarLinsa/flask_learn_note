from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField(label=u'用户名', validators=[DataRequired(message="数据不能为空")])
    password = PasswordField(label=u'密码', validators=[DataRequired(message="数据不能为空")])
    submit = SubmitField(label=u'提交')
