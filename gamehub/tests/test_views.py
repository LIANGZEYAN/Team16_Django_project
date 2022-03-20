from django.test import TestCase, Client
from django.urls import reverse
from gamehub.models import Game,Comment
import  json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.about_url = reverse('gamehub:about')
        self.show_comments_url = reverse('gamehub:show_comments', args=['some-slug'])
        self.sortByQual_url = reverse('gamehub:sortByQual')
        self.sortByMusic_url = reverse('gamehub:sortByMusic')
        self.sortByComm_url = reverse('gamehub:sortByComm')
        self.register_url = reverse('gamehub:register')
        self.login_url = reverse('gamehub:login')
        self.thanks_url = reverse('gamehub:thanks')


    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamehub/index.html')

    def test_about_GET(self):
        response = self.client.get(self.about_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamehub/about.html')

    def test_show_comments_GET(self):
        response = self.client.get(self.show_comments_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamehub/thanks.html')

    def test_sortByQual_GET(self):
        response = self.client.get(self.sortByQual_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamehub/sort.html')

    def test_sortByMusic_GET(self):
        response = self.client.get(self.sortByMusic_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamehub/sort.html')

    def test_sortByComm_GET(self):
        response = self.client.get(self.sortByComm_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamehub/sort.html')

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamehub/register.html')

    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamehub/login.html')

    def test_thanks_GET(self):
        response = self.client.get(self.thanks_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamehub/thanks.html')