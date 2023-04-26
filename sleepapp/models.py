from django.db import models

class Sleep(models.Model):
    
    #id = models.AutoField(primary_key=True)

    Colunm_1 = models.CharField(max_length=20)
    Colunm_2 = models.CharField(max_length=20)
    Colunm_3 = models.CharField(max_length=20)
    Colunm_4 = models.CharField(max_length=20)
    Colunm_5 = models.CharField(max_length=20)
    Colunm_6 = models.FloatField()
    Colunm_7 = models.CharField(max_length=20)
    Colunm_8 = models.CharField(max_length=40)
    Colunm_9 = models.CharField(max_length=40)
    Colunm_10 = models.FloatField()
    Colunm_11 = models.FloatField()
    Colunm_12 = models.CharField(max_length=20)
    Colunm_13 = models.FloatField()
    Colunm_14 = models.CharField(max_length=20)
    Colunm_15 = models.CharField(max_length=20)
    Colunm_16 = models.CharField(max_length=20)
    Colunm_17 = models.CharField(max_length=20)
    Colunm_18 = models.CharField(max_length=20)
    Colunm_19 = models.CharField(max_length=20)


    class Meta:
        db_table = 'sleep'
        managed = False

# #회원 정보
# class User(models.Model):
#     email = models.CharField(max_length=20)
#     name = models.CharField(max_length=20)
#     pwd = models.CharField(max_length=20)
#     c_date = models.DateTimeField()
