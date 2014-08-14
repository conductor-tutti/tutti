# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms.fields import (
    StringField,
    PasswordField,
    TextAreaField,
    SelectField
)
from wtforms import validators
from wtforms.fields.html5 import EmailField


class ArticleForm(Form):
    title = StringField(
        u'제목',
        [validators.data_required(u'제목을 입력하시기 바랍니다.')],
        description={'placeholder': u'제목을 입력하세요.'}
    )
    content = TextAreaField(
        u'내용',
        [validators.data_required(u'내용을 입력하시기 바랍니다.')],
        description={'placeholder': u'내용을 입력하세요.'}
    )
    author = StringField(
        u'작성자',
        [validators.data_required(u'이름을 입력하시기 바랍니다.')],
        description={'placeholder': u'이름을 입력하세요.'}
    )
    category = StringField(
        u'카테고리',
        [validators.data_required(u'카테고리를 입력하시기 바랍니다.')],
        description={'placeholder': u'카테고리를 입력하세요.'}
    )


class CommentForm(Form):
    content = StringField(
        u'내용',
        [validators.data_required(u'내용을 입력하시기 바랍니다.')],
        description={'placeholder': u'내용을 입력하세요.'}
    )
    author = StringField(
        u'작성자',
        [validators.data_required(u'이름을 입력하시기 바랍니다.')],
        description={'placeholder': u'이름을 입력하세요.'}
    )
    password = PasswordField(
        u'비밀번호',
        [validators.data_required(u'비밀번호를 입력하시기 바랍니다.')],
        description={'placeholder': u'비밀번호를 입력하세요.'}
    )
    email = EmailField(
        u'이메일',
        [validators.data_required(u'이메일을 입력하시기 바랍니다.')],
        description={'placeholder': u'이메일을 입력하세요.'}
    )
class LoginForm(Form):
    userid = StringField(
        u"ID",
        [validators.data_required(u"아이디를 입력하세요!")],
        description={'placeholder': u"아이디를 입력하세요."}
        )
    password = PasswordField(
        u"Password",
        [validators.data_required(u"패스워드를 입력하세요!")],
        description={"placeholder": u"패스워드를 입력하세요."}
        )

class UserForm(Form):
    userid = StringField(
        u'ID',
        [validators.data_required(u'아이디를 입력하세요!')],
        description={'placeholder':u'아이디를 입력하세요.'}
        )
    password = PasswordField(
        u'Password',
        [validators.data_required(u'패스워드를 입력하세요!'),
        validators.EqualTo('confirm_password', message=u'패스워드가 일치하지 않네요.')],
        description={'placeholder':u'패스워드를 입력하세요.'}
        )
    confirm_password = PasswordField(
        u'Confirm password',
        [validators.data_required(u'패스워드를 한 번 더 입력하세요!')],
        description={'placeholder':u'패스워드를 한 번 더 입력하세요.'})
    username = StringField(
        u'Username *성과 이름을 모두 입력하세요!',
        [validators.data_required(u'성과 이름을 모두 입력하세요. 예: 오정민')],
        description={'placeholder':u'성과 이름을 모두 입력하세요. 예: 오정민.'}
        )
    email = EmailField(
        u'E-mail *정확히 입력하세요!',
        [validators.data_required(u'이메일을 입력하세요!')],
        description={'placeholder':u'이메일을 입력하세요.'}
        )
