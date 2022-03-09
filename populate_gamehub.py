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

    games = {1: {'name': 'Destiny2', 'publisher': 'Bungie','price': 49,'description': 'Destiny 2 is a free-to-play online-only multiplayer first-person shooter video game', 'category': 'FPS','poster': '/static/images/elder_ring.jpg', 'store_link': 'https://www.bungie.net/7/en/destiny/newlight','avg_quality_rate': 4.6, 'avg_music_rate': 4.2,'avg_community_rate': 4.1, 'views': 32, 'comments': Destiny2_comments},
             2: {'name':'Dota2', 'publisher': 'Valve','price': 0,'description': 'Dota 2 is a multiplayer online battle arena video game', 'category': 'MOBA', 'poster': '/static/images/elder_ring.jpg', 'store_link': 'https://www.dota2.com/home','avg_quality_rate': 3.6, 'avg_music_rate': 3.2,'avg_community_rate': 3.1, 'views': 64, 'comments': Dota2_comments},
             3: {'name':'Elderring', 'publisher': 'FromSoftware','price': 59,'description': 'THE NEW FANTASY ACTION RPG', 'category': 'MOBA', 'poster': '/static/images/elder_ring.jpg', 'store_link': 'https://store.steampowered.com/app/1245620/ELDEN_RING/','avg_quality_rate': 4.1, 'avg_music_rate': 3.5,'avg_community_rate': 3.0, 'views': 128, 'comments': Elderring_comments}}

    for id, game_data in games.items():
        g = add_game(id, game_data['name'], game_data['publisher'], game_data['price'], game_data['description'], game_data['category'], game_data['poster'], game_data['store_link'], game_data['avg_quality_rate'], game_data['avg_music_rate'], game_data['avg_community_rate'], game_data['views'],game_data['comments'])
        for c in game_data['comments']:
            add_comment(g, c['id'], c['content'], c['quality_rate'], c['music_rate'], c['community_rate'])

    for g in Game.objects.all():
        print(type(g))
        print(g.description)
        print(g.category)

def add_comment(game, id, content, quality_rate, music_rate, community_rate):
    c = Comment.objects.get_or_create(game=game, content=content)[0]
    c.id = id
    c.quality_rate = quality_rate
    c.music_rate = music_rate
    c.community_rate = community_rate
    c.save()
    return c

def add_game(id, name, publisher, price, description, category, poster, store_link, avg_quality_rate, avg_music_rate, avg_community_rate, views, comments):
    g = Game.objects.get_or_create(id=id)[0]
    g.name = name
    g.publisher = publisher
    g.price = price
    g.description = description
    g.category= category
    g.poster = poster
    g.store_link = store_link
    g.avg_quality_rate = avg_quality_rate
    g.avg_music_rate = avg_music_rate
    g.avg_community_rate = avg_community_rate
    g.views = views
    g.comments = comments
    g.save()
    return g

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
