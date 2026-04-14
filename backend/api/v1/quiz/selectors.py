from quiz.models import Quiz_question, Quiz_answer


def get_questions_by_category(tech_id):
   resalt = Quiz_question.objects.filter(tech=tech_id).prefetch_related('quiz_answers')
   return resalt
 