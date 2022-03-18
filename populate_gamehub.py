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

    LostArk_comments = [
        {'id': 10,
         'content': 'cannot wait to introduce this to my friend',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'id': 11,
         'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'id': 12,
         'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5}, ]

    Witcher3_comments = [
        {'id': 13,
         'content': 'cannot wait to introduce this to my friend',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'id': 14,
         'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'id': 15,
         'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5}, ]

    Division2_comments = [
        {'id': 16,
         'content': 'cannot wait to introduce this to my friend',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'id': 17,
         'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'id': 18,
         'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5}, ]

    NeedForSpeed2021_comments = [
        {'id': 19,
         'content': 'cannot wait to introduce this to my friend',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'id': 20,
         'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'id': 21,
         'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5}, ]

    FIFA2022_comments = [
        {'id': 22,
         'content': 'cannot wait to introduce this to my friend',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'id': 23,
         'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'id': 24,
         'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5}, ]

    Csgo_comments = [
        {'id': 25,
         'content': 'cannot wait to introduce this to my friend',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'id': 26,
         'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'id': 27,
         'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5}, ]

    DeathStanding_comments = [
        {'id': 28,
         'content': 'cannot wait to introduce this to my friend',
         'quality_rate': 5,
         'music_rate': 5,
         'community_rate': 5},

        {'id': 29,
         'content': 'Music is attractive',
         'quality_rate': 4,
         'music_rate': 5,
         'community_rate': 3},

        {'id': 30,
         'content': 'Content is a little bit boring',
         'quality_rate': 3,
         'music_rate': 4,
         'community_rate': 5}, ]


    games = {1: {'name': 'Destiny2', 'publisher': 'Bungie','price': 49,
                 'description': 'Destiny 2 is a free-to-play online-only multiplayer first-person shooter video game',
                 'category': 'FPS','poster': '/static/images/destiny2.png', 'store_link': 'https://www.bungie.net/7/en/destiny/newlight',
                 'avg_quality_rate': 4.6, 'avg_music_rate': 4.2,'avg_community_rate': 4.1, 'views': 32,
                 'comments': Destiny2_comments},

             2: {'name':'Dota2', 'publisher': 'Valve','price': 0,
                 'description': 'Dota 2 is a multiplayer online battle arena video game', 'category': 'MOBA',
                 'poster': '/static/images/dota2.png', 'store_link': 'https://www.dota2.com/home',
                 'avg_quality_rate': 3.6, 'avg_music_rate': 3.2,'avg_community_rate': 3.1, 'views': 64,
                 'comments': Dota2_comments},

             3: {'name': 'Elderring', 'publisher': 'FromSoftware', 'price': 59,
                  'description': 'Elden Ring is an action role-playing game developed by FromSoftware and published by Bandai Namco Entertainment.',
                  'category': 'MOBA',
                  'poster': '/static/images/elder_ring.png',
                  'store_link': 'https://store.steampowered.com/app/1245620/ELDEN_RING/',
                  'avg_quality_rate': 4.4, 'avg_music_rate': 3.5, 'avg_community_rate': 4.0, 'views': 300,
                  'comments': Elderring_comments},

             4: {'name': 'LostArk', 'publisher': 'Smilegate', 'price': 0,
                 'description': 'Lost Ark is a top-down 2.5D fantasy massively multiplayer online action role-playing game', 'category': 'ARPG',
                 'poster': '/static/images/lost_ark.png', 'store_link': 'https://store.steampowered.com/app/1599340/Lost_Ark/',
                 'avg_quality_rate': 3.0, 'avg_music_rate': 2.5, 'avg_community_rate': 4.6, 'views': 164,
                 'comments': LostArk_comments},

             5: {'name': 'Witcher3', 'publisher': 'CD Projekt Red', 'price': 39,
                 'description': 'The Witcher 3: Wild Hunt is an action role-playing game developed by Polish developer CD Projekt Red, and first published in 2015', 'category': 'RPG',
                 'poster': '/static/images/witcher3.png', 'store_link': 'https://thewitcher.com/en/witcher3',
                 'avg_quality_rate': 4.9, 'avg_music_rate': 4.1, 'avg_community_rate': 4.0, 'views': 200,
                 'comments': Witcher3_comments},

             6: {'name': 'Division2', 'publisher': 'Ubisoft', 'price': 30,
                 'description': 'Tom Clancys The Division 2 is an online-only action role-playing video game developed by Massive Entertainment and published by Ubisoft', 'category': 'TPS',
                 'poster': '/static/images/division2.png', 'store_link': 'https://www.ubisoft.com/en-gb/game/the-division/the-division-2',
                 'avg_quality_rate': 3.9, 'avg_music_rate': 3.0, 'avg_community_rate': 3.2, 'views': 88,
                 'comments': Division2_comments},

             7: {'name': 'NeedForSpeed2021', 'publisher': 'EA', 'price': 44,
                 'description': 'Need for Speed is a video game series that has been going for over 25 year now.', 'category': 'RACING',
                 'poster': '/static/images/needforspeed2021.png',
                 'store_link': 'https://www.ea.com/games/need-for-speed',
                 'avg_quality_rate': 4.0, 'avg_music_rate': 4.5, 'avg_community_rate': 3.0, 'views': 102,
                 'comments': NeedForSpeed2021_comments},

             8: {'name': 'FIFA2022', 'publisher': 'EA', 'price': 79,
                 'description': 'EA SPORTS™ FIFA 22 brings the game even closer to the real thing with fundamental gameplay advances and a new season of innovation across every mode.', 'category': 'Sports',
                 'poster': '/static/images/fifa2022.png',
                 'store_link': 'https://store.steampowered.com/app/1506830/FIFA_22/?utm_medium=organic&utm_source=franchise_web&utm_content=buylink',
                 'avg_quality_rate': 4.1, 'avg_music_rate': 3.5, 'avg_community_rate': 3.0, 'views': 55,
                 'comments': FIFA2022_comments},

             9: {'name': 'CS:GO', 'publisher': 'Valve', 'price': 0,
                 'description': 'Counter-Strike: Global Offensive is a multiplayer first-person shooter developed by Valve and Hidden Path Entertainment.', 'category': 'FPS',
                 'poster': '/static/images/csgo.png',
                 'store_link': 'https://blog.counter-strike.net/',
                 'avg_quality_rate': 4.4, 'avg_music_rate': 2.5, 'avg_community_rate': 4.3, 'views': 166,
                 'comments': Csgo_comments},

             10: {'name': 'DeathStanding', 'publisher': 'Kojima Productions', 'price': 47,
                 'description': 'Death Stranding is an action game developed by Kojima Productions.', 'category': 'MOBA',
                 'poster': '/static/images/deathstanding.png',
                 'store_link': 'https://store.steampowered.com/app/1245620/ELDEN_RING/',
                 'avg_quality_rate': 4.1, 'avg_music_rate': 3.5, 'avg_community_rate': 3.0, 'views': 211,
                 'comments': DeathStanding_comments}

             }


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
