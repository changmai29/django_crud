from django.db import models

# Create your models here.
class Notes(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    body=models.TextField()
    timestamp=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "notes"
        managed=True

    def __str__(self):
        return self.title


