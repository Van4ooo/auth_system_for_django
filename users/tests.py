from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class SingUpTests(TestCase):
    username = "test_user1"
    email = "test_email@gmail.com"
    password = "secret123#"
    age = 19

    def test_status_code_by_url(self):
        resp = self.client.get("/users/signup/")
        self.assertEqual(resp.status_code, 200)

    def test_status_code_by_name(self):
        resp = self.client.get(reverse("signup"))
        self.assertEqual(resp.status_code, 200)

    def test_template_used(self):
        resp = self.client.get(reverse("signup"))
        self.assertTemplateUsed(resp, "signup.html")

    def test_signup_forms(self):
        user = get_user_model().objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            age=self.age
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)

        self.assertEqual(get_user_model().objects.all()[0].username,
                         self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,
                         self.email)
        self.assertEqual(get_user_model().objects.all()[0].age,
                         self.age)


class LoginPageTests(TestCase):
    username = "just_user"
    password = "secret1233"

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            password=self.password,
            email="test-email@gmail.com",
            username=self.username
        )

    def test_status_code_by_url(self):
        resp = self.client.get("/users/login/")
        self.assertEqual(resp.status_code, 200)

    def test_status_code_by_name(self):
        resp = self.client.get(reverse("login"))
        self.assertEqual(resp.status_code, 200)

    def test_template_used(self):
        resp = self.client.get(reverse("login"))
        self.assertTemplateUsed(resp, 'registration/login.html')

    def test_login_system(self):
        resp = self.client.post(reverse("login"), {
            "username": self.username,
            "password": self.password
        })

        self.assertEqual(resp.status_code, 302)

