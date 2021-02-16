from django.db import models
from django.conf import settings # 인증 관련 패키지 사용을 위한 import
from django.core.validators import RegexValidator

# Create your models here.

class Profile(models.Model):
    # settings의 AUTH_USER_MODEL의 필드와 1대1 대응해서 사용
    # user_id
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 이름
    user_name = models.CharField('이름', max_length=10)
    # 생년월일
    birth_date = models.DateField('date published')
    # 성별
    Gender = (
        ('성별', '성별'),
        ('남성', '남성'),
        ('여성', '여성'),
    )
    gender = models.CharField('성별',
                              max_length=10,
                              choices=Gender,
                              default='N')

    # E-mail : 선택사항
    email = models.EmailField(verbose_name='본인 확인 이메일(선택사항)',
                              max_length=128,
                              blank=True)
    # 휴대전화 번호
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(r'^010[1-9]\d{7}$')])

    def __str__(self):
        return self.user_name