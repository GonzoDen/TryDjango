import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):

    def test_was_pub_recently_w_future_question(self):
        time = timezone.now()+datetime.timedelta(days=30)
        future_q = Question(pub_date=time)
        self.assertIs(future_q.was_pub_recently(), False)


class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        future_q = create_question(question_text='Future Question', days=5)
        url=reverse('polls:detail', args=(future_q.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)