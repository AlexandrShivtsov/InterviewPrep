from django.contrib import admin

from .models import Quiz_question, Quiz_answer


admin.site.register(Quiz_question)
admin.site.register(Quiz_answer)


