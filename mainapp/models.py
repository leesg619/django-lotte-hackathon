from django.db import models

# Create your models here.

class Box(models.Model):
    box_type = models.BooleanField() # True = 받는 False = 보내는
    code = models.CharField(max_length = 30) # 송장번호
    company = models.CharField(max_length = 30) # 택배사
 
    sender = models.CharField(max_length = 30) # 보내는사람 이름
    sender_phone = models.CharField(max_length = 30) # 보내는사람 전화번호
    sender_address = models.CharField(max_length = 100) # 보내는사람 주소
    
    receiver =  models.CharField(max_length = 30) # 받는사람 이름
    receiver_phone = models.CharField(max_length = 30) # 받는사람 전화번호
    receiver_address = models.CharField(max_length = 100) # 받는사람 주소

    box_detail = models.CharField(max_length = 30) # 상품정보
    worker = models.CharField(max_length = 30, default ="미정") # 배송기사 이름
    worker_phone = models.CharField(max_length = 30, default = " ") # 배송기사 전화번호
    visit_date = models.DateTimeField(null = True)# 택배 예약시 방문희망일

class State(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    box_date = models.DateTimeField()
    box_now = models.CharField(max_length = 50)
    box_state = models.CharField(max_length = 30)

