from questions.models import Question


def get_questions_by_category(tech_id):
   return Question.objects.filter(category=tech_id)