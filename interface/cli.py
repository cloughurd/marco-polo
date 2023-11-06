import requests

from core.capitals import CapitalsGame
from core.game import Round

def run():
    url = 'http://localhost:8080'
    try:
        r = requests.get(f'{url}/status')
        if r.status_code != 200:
            print('Uh-oh, looks like the server is having an issue!')
            return
    except requests.exceptions.ConnectionError:
        print('Uh-oh, looks like the server is not running!')
        return

    games = [
        ('Capitals Quiz', CapitalsGame),
    ]

    choice = ''
    while True:
        print('Welcome to Marco Polo games!')
        print('Which game would you like to play?')
        games_map = {}
        for idx, g in enumerate(games):
            name = g[0]
            games_map[name] = idx
            print(f'\n\t{idx}) {name}')
        print('Enter "quit" to quit.')
        choice = input('Selection: ').lower()
        if choice == 'quit':
            break
        if choice in games_map:
            choice = games_map[choice]

        try:
            choice = int(choice)
        except ValueError:
            print('Not a valid option!')
            continue
        if choice >= len(games):
            print('Not a valid option!')
            continue

        r = Round(games[choice][1].build_game(url))
        r.play()


if __name__ == '__main__':
    run()
