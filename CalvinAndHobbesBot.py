import argparse

from mastodon import Mastodon
from datetime import date


# def register():
#     """This only needs to be done once"""
#     Mastodon.create_app(
#         clientName,
#         api_base_url=apiBaseUrl,
#         to_file=clientCredentialsFile)


def login():
    mastodon = Mastodon(
        client_id=clientCredentialsFile,
        api_base_url=apiBaseUrl)
    version = mastodon.retrieve_mastodon_version()
    mastodon.log_in(
        username='marv42+calvinandhobbes@gmail.com',
        password='C4lv1nH08835M4rvaz!%',
        to_file=userCredentialsFile)


def get_instance():
    return Mastodon(
        access_token=userCredentialsFile,
        api_base_url=apiBaseUrl)


def toot_random():
    mastodon = get_instance()
    mastodon.toot('random comic:\nhttps://www.gocomics.com/random/calvinandhobbes')


def toot_daily():
    mastodon = get_instance()
    year = date.today().year
    month = date.today().month
    day = date.today().day - 1
    mastodon.toot(f'daily comic:\nhttps://www.gocomics.com/calvinandhobbes/{year}/{month}/{day}')


clientName = 'pytooterappcalvinandhobbes'
apiBaseUrl = 'https://botsin.space'
clientCredentialsFile = 'pytooter_clientcred_calvinandhobbes.secret'
userCredentialsFile = 'pytooter_usercred_calvinandhobbes.secret'


def parse_args():
    parser = argparse.ArgumentParser(description='toot a daily comic')
    parser.add_argument('--random', action='store_true', help='toot a random comic')
    return parser.parse_args()


if __name__ == '__main__':
    login()
    args = parse_args()
    if args.random:
        toot_random()
    else:
        toot_daily()
