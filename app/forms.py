# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms.fields import (
    StringField,
    PasswordField,
    TextAreaField
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


class UserForm(Form):
    name = StringField(
        u'name',
        [validators.data_required(u'Type your name.')],
        description={'placeholder':u'Type your name please.'}
        )
    username = StringField(
        u'username',
        [validators.data_required(u'Type your username.')],
        description={'placeholder':u'Type your username please.'}
        )
    password = PasswordField(
        u'password',
        [validators.data_required(u'Type your password.')],
        description={'placeholder':u'Type your password please.'}
        )
    email = EmailField(
        u'E-mail',
        [validators.data_required(u'Type your E-mail.')],
        description={'placeholder':u'Type your E-mail please.'}
        )