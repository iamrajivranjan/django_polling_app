from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name=("Poll Question"), on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
