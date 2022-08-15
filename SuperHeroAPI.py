from decorators import decoration_logger, decoration_log_dir
import requests

TOKEN = '2619421814940190'
LINK = f'https://www.superheroapi.com/api.php/{TOKEN}/search/'

urls = [
    f'{LINK}Hulk',
    f'{LINK}Thanos',
    f'{LINK}Captain%America',
]


@decoration_log_dir('log/super_hero_api_log.txt')
def requests_get(url_all):
    r = (requests.get(url) for url in url_all)
    return r


@decoration_logger
def parser():
    super_man = []
    for item in requests_get(urls):
        intelligence = item.json()
        try:
            for power_stats in intelligence['results']:
                super_man.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f"Проверте ссылки urls: {urls}")

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")


if __name__ == '__main__':
    parser()