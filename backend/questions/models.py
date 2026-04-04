from django.db import models
from catalog.models import Category


class Question(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='question_data')
    question_text = models.TextField(max_length=500, default='', blank=True, null=True)
    answer_text = models.TextField(max_length=500, default='', blank=True, null=True)
    
    def __str__(self):
        return self.category.tech + ': ' + self.question_text[:50] 
    
    
