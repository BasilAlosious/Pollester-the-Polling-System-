from django.db import models

# Create your models here.
class Question(models.Model):
    questions_txt= models.CharField(max_length=200)
    pub_date= models.DateField('date published')

    def __str__(self):
        return self.questions_txt

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text =models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
     return self.choice_text