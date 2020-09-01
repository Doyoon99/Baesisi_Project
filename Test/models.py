from django.db import models
from django import forms



# 0. 들어갈 책들의 데이터
# 이 책들의 Score가 쌓이는 형식(유저 name참조)으로 views를 짜야함
# 책은 pk id번호 (1~16)로 분류될 것
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    poet = models.CharField(max_length=200)
    img = models.URLField()
    keyword = models.CharField(max_length=200)
    result = models.TextField()
    poem = models.TextField() #시전문
    Plink = models.TextField() #구매링크
    content = models.TextField() #시구절

# 1. 테스트를 진행하는 유저
class Tester(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    #score
    Bada = models.IntegerField(default=0)
    Possible = models.IntegerField(default=0)
    Love = models.IntegerField(default=0)
    Sobolo = models.IntegerField(default=0)
    Small = models.IntegerField(default=0)
    Math = models.IntegerField(default=0)
    Meehee = models.IntegerField(default=0)
    Antiseptic = models.IntegerField(default=0)
    Because = models.IntegerField(default=0)
    Jangma = models.IntegerField(default=0)
    Lofi = models.IntegerField(default=0)
    Blackleaf = models.IntegerField(default=0)
    Fifteen= models.IntegerField(default=0)
    Kind = models.IntegerField(default=0)
    Station = models.IntegerField(default=0)
    Nowrite = models.IntegerField(default=0)
    result = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)

# 2. 질문 데이터
class Question(models.Model):
    title = models.TextField()
    score = models.IntegerField()
    img = models.ImageField(blank=True)
    opt1 = models.TextField()
    opt2 = models.TextField()
    opt3 = models.TextField(blank=True)
    opt4 = models.TextField(blank=True)
    opt5 = models.TextField(blank=True)

#result 모델 굳이 필요 없이 views에서 max구하는 함수짜서, Max를 출력해주면 될 듯.
