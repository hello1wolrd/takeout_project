import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Question


# Create your tests here.
class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        u'''
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(
        question_text=question_text,
        pub_date=time
        )


class QuestionViewTests(TestCase):
    def test_index_view_with_no_question(self):
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "no hello are available")

        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        create_question(question_text="past question", days=-30)
        response = self.client.get(reverse('hello:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],
            ['<Question: past question>']
            )

    def test_index_view_with_a_future_question(self):
        create_question(question_text="future_question", days=30)
        response = self.client.get(reverse('hello:index'))
        self.assertContains(response, "no hello are available", status_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_and_past_question(self):
        create_question(question_text="past question", days=-30)
        create_question(question_text="future question", days=30)
        response = self.client.get(reverse('hello:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: past question>']
            )

    def test_index_view_with_two_past_questions(self):
        create_question(question_text="past question 1", days=-30)
        create_question(question_text="past question 2", days=-5)
        response = self.client.get(reverse('hello:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: past question 2>',
            '<Question: past question 1>']
            )


class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        future_question = create_question(question_text='future question',days=30)
        response = self.client.get(reverse('hello:detail',
            args=(future_question.id,)
            ))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        past_question = create_question(question_text='past question',
            days=-5)
        response = self.client.get(reverse('hello:detail',
            args=(past_question.id,)))
        self.assertContains(response, past_question.question_text,
            status_code=200)
