import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Team16_Django_project.settings')

import django
django.setup()

from gamehub.models import Game, Comment

def populate():
    Destiny2_comments = [
        {'content': 'This game is awesome!',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5},]

    Dota2_comments = [
        {'content': 'interesting',
         'quality_rate': 4,
         'music_rate': 4,
         'community_rate': 4},

        {'content': 'Music is awesome',
         'quality_rate': 3,
         'music_rate': 5,
         'community_rate': 1},

        {'content': 'nearly no content',
         'quality_rate': 1,
         'music_rate': 4,
         'community_rate': 5}, ]

    Elderring_comments = [
        {'content': 'cannot wait to introduce this to my friend',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5}, ]

    games = {'Destiny2': {'comments': Destiny2_comments, 'views': 32},
            'Dota2': {'comments': Dota2_comments, 'views': 64},
            'Elderring': {'comments': Elderring_comments, 'views': 128}}

    for game, game_data in games.items():
        g = add_game(game, game_data['views'])
        for c in game_data['comments']:
            add_comment(g, c['content'], c['quality_rate'], c['music_rate'], c['community_rate'])

    for g in Game.objects.all():
        for c in Comment.objects.filter(game=g):
            print(f'- {g}: {c}')

def add_comment(game, content, quality_rate, music_rate, community_rate):
    c = Comment.objects.get_or_create(game=game, content=content)[0]
    c.quality_rate = quality_rate
    c.music_rate = music_rate
    c.community_rate = community_rate
    c.save()
    return c

def add_game(name, views):
    g = Game.objects.get_or_create(name=name)[0]
    g.views = views
    g.save()
    return g

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
