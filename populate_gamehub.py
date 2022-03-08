import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Team16_Django_project.settings')

import django
django.setup()

from gamehub.models import Game, Comment

def populate():
    Destiny2_comments = [
        {'id':1,
         'content': 'This game is awesome!',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'id':2,
         'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'id':3,
         'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5},]

    Dota2_comments = [
        {'id':4,
         'content': 'interesting',
         'quality_rate': 4,
         'music_rate': 4,
         'community_rate': 4},

        {'id':5,
         'content': 'Music is awesome',
         'quality_rate': 3,
         'music_rate': 5,
         'community_rate': 1},

        {'id':6,
         'content': 'nearly no content',
         'quality_rate': 1,
         'music_rate': 4,
         'community_rate': 5}, ]

    Elderring_comments = [
        {'id':7,
         'content': 'cannot wait to introduce this to my friend',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'id':8,
         'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'id':9,
         'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5}, ]

    games = {'Destiny2': {'id': 1, 'publisher': 'Bungie','price': 49,'description': 'Destiny 2 is a free-to-play online-only multiplayer first-person shooter video game', 'category': 'FPS','store_link': 'https://www.bungie.net/7/en/destiny/newlight','avg_quality_rate': 4.6, 'avg_music_rate': 4.2,'avg_community_rate': 4.1, 'comments': Destiny2_comments, 'views': 32},
            'Dota2': {'id':2, 'publisher': 'Valve','price': 0,'description': 'Dota 2 is a multiplayer online battle arena video game', 'category': 'MOBA','store_link': 'https://www.dota2.com/home','avg_quality_rate': 3.6, 'avg_music_rate': 3.2,'avg_community_rate': 3.1, 'comments': Dota2_comments, 'views': 64},
            'Elderring': {'id':3, 'publisher': 'FromSoftware','price': 59,'description': 'THE NEW FANTASY ACTION RPG', 'category': 'MOBA','store_link': 'https://store.steampowered.com/app/1245620/ELDEN_RING/','avg_quality_rate': 4.1, 'avg_music_rate': 3.5,'avg_community_rate': 3.0, 'comments': Elderring_comments, 'views': 128}}

    for game, game_data in games.items():
        g = add_game(game, game_data['id'], game_data['publisher'], game_data['price'], game_data['description'], game_data['category'], game_data['store_link'], game_data['avg_quality_rate'], game_data['avg_music_rate'], game_data['avg_community_rate'], game_data['views'])
        for c in game_data['comments']:
            add_comment(g, c['id'], c['content'], c['quality_rate'], c['music_rate'], c['community_rate'])

    for g in Game.objects.all():
        for c in Comment.objects.filter(game=g):
            print(f'- {g}: {c}')

def add_comment(game, id, content, quality_rate, music_rate, community_rate):
    c = Comment.objects.get_or_create(game=game, content=content)[0]
    c.id = id
    c.quality_rate = quality_rate
    c.music_rate = music_rate
    c.community_rate = community_rate
    c.save()
    return c

def add_game(name, id, publisher, price, description, category, store_link, avg_quality_rate, avg_music_rate, avg_community_rate, views):
    g = Game.objects.get_or_create(name=name)[0]
    g.id = id
    g.publisher = publisher
    g. price = price
    g.description = description
    g.category= category
    g.store_link = store_link
    g.avg_quality_rate = avg_quality_rate
    g.avg_music_rate = avg_music_rate
    g.avg_community_rate = avg_community_rate
    g.views = views
    g.save()
    return g

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
