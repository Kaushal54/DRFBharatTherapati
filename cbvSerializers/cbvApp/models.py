from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120,null=True,blank=True)
    score = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name+' '+self.id

    # class Meta:
    #     db_table = 'proj_employee'
