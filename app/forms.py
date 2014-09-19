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
from app.models import Category, Major

class UserForm(Form):
    email = EmailField(
        u'E-mail *정확히 입력하세요!',
        [validators.data_required(u'이메일을 입력하세요!')],
        description={'placeholder':u'이메일을 입력하세요.'}
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
    
class LoginForm(Form):
    login_email = EmailField(
        u"Email",
        [validators.data_required(u'이메일을 입력하세요!')],
        description={'placeholder':u'이메일 입력하세요.'}
        )
    login_password = PasswordField(
        u'Password',
        [validators.data_required(u'패스워드를 입력하세요!')],
        description={'placeholder':u'패스워드를 입력하세요.'}
        )

class MusicianProfileForm(Form):
    # category = SelectField(u"전공 분야", coerce=int)
    # major = SelectField(u"어쩌구", choices=[])
    phrase = StringField(
        u"당신을 표현하는 인상적인 100자 메시지",
        [validators.data_required(u"100자 메시지를 입력하세요."),
        validators.Length(max=100)]
        )
    
    education = StringField(
        u"학력사항",
        [validators.data_required(u"학력사항을 입력하세요.")]
        )
    
    education_status = SelectField(
        u"학적사항",
        choices=[(1, "졸업"), (2, "재학"), (3, "휴학"), (4, "중퇴")],
        )

    awards = StringField(
        u"수상경력",
        [validators.data_required(u"수상경력을 입력하세요.")]
        )
    
    awards_data = StringField(
        u"수상일자",
        [validators.data_required(u"수상일자를 입력하세요")]
        )
