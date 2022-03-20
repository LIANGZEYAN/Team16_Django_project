from django.test import  TestCase
from gamehub.models import Game, Comment, User


class TestModels(TestCase):

    def setUp(self):
        self.game1 = Game.objects.create(
            name= 'nba2k',
            publisher= '2kgames'
        )

    def test_game_is_assigned_slug_on_creation(self):
        self.assertEquals(self.game1.slug, 'nba2k')