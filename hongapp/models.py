from django.db import models

class Hong(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)


    class Meta:
        db_table = 'cafe'
        managed = False

#회원 정보
# class User(models.Model):
#     email = models.CharField(max_length=20)
#     name = models.CharField(max_length=20)
#     pwd = models.CharField(max_length=20)
#     c_date = models.DateTimeField()
