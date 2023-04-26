from django.db import models

class Sleep(models.Model):
    
    id = models.AutoField(primary_key=True)
    졸음쉼터명 = models.CharField(max_length=20)
    시도명 = models.CharField(max_length=20)
    시군구명 = models.CharField(max_length=20)
    도로종류 = models.CharField(max_length=20)
    도로노선명 = models.CharField(max_length=20)
    도로노선번호 = models.FloatField()
    도로노선방향 = models.CharField(max_length=20)
    소재지도로명주소 = models.CharField(max_length=40)
    소재지지번주소 = models.CharField(max_length=40)
    위도 = models.FloatField()
    경도 = models.FloatField()
    총연장 = models.CharField(max_length=20)
    주차면수 = models.FloatField()
    화장실유무 = models.CharField(max_length=20)
    방범용CCTV수 = models.CharField(max_length=20)
    기타편의시설 = models.CharField(max_length=20)
    관리기관명 = models.CharField(max_length=20)
    관리기관전화번호 = models.CharField(max_length=20)
    데이터기준일자 = models.CharField(max_length=20)

    class Meta:
        db_table = 'sleep'
        managed = False

#회원 정보
class User(models.Model):
    email = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    c_date = models.DateTimeField()
