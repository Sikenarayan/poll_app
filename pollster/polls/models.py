# this imports the base model class for us to use
from django.db import models

# Create your models/tables here.
# here we have models.Model such that it inheirtates all the methods from it
class Question(models.Model): # the foregin key is being connected to this promary key(Question)
    #our fields
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
#making a relationship in between Question and Choice
class Choice(models.Model):
    #This basically deletes choices if the question is deleted.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# the def __str__(self) for both Questions and Choices is done to show the text of questions and choices.
# if not just objects(1), (2).... (n) would be shown
 