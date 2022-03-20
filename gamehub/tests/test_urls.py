from django.test import SimpleTestCase
from django.urls import reverse, resolve
from gamehub.views import index,about,show_comments,rate,view,sortByView,sortByQual,sortByMusic,sortByComm,register,user_login,restricted,user_logout,thanks


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_about_url_resolves(self):
        url = reverse('gamehub:about')
        self.assertEquals(resolve(url).func, about)

    def test_show_comments_url_resolves(self):
        url = reverse('gamehub:show_comments', args=['some-slug'])
        self.assertEquals(resolve(url).func, show_comments)

    def test_rate_url_resolves(self):
        url = reverse('gamehub:rate', args=['some-slug'])
        self.assertEquals(resolve(url).func, rate)

    def test_sortByQual_url_resolves(self):
        url = reverse('gamehub:sortByQual')
        self.assertEquals(resolve(url).func, sortByQual)

    def test_sortByMusic_url_resolves(self):
        url = reverse('gamehub:sortByMusic')
        self.assertEquals(resolve(url).func, sortByMusic)

    def test_sortByComm_url_resolves(self):
        url = reverse('gamehub:sortByComm')
        self.assertEquals(resolve(url).func, sortByComm)

    def test_register_url_resolves(self):
        url = reverse('gamehub:register')
        self.assertEquals(resolve(url).func, register)

    def test_login_url_resolves(self):
        url = reverse('gamehub:login')
        self.assertEquals(resolve(url).func, user_login)

    def test_restricted_url_resolves(self):
        url = reverse('gamehub:restricted')
        self.assertEquals(resolve(url).func, restricted)

    def test_logout_url_resolves(self):
        url = reverse('gamehub:logout')
        self.assertEquals(resolve(url).func, user_logout)

    def test_thanks_url_resolves(self):
        url = reverse('gamehub:thanks')
        self.assertEquals(resolve(url).func, thanks)