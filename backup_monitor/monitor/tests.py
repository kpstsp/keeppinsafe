# backup_monitor/monitor/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class MonitorViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')


    def test_calendar_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('calendar'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monitor/calendar.html')