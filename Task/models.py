from djongo import models

# Create your models here.



class Banks(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Branchs(models.Model):
    ifsc = models.CharField(max_length=30)
    bank = models.ForeignKey(Banks,on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    


