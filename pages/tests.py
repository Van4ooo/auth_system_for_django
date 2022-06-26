from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_status_code(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_by_name_status_code(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertTemplateUsed(resp, "home.html")

    def test_contains_in_home_page(self):
        resp = self.client.get(reverse("home"))
        self.assertContains(resp, 'You are not logged in')
