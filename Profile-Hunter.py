import requests

BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
NORMAL = "\033[0m"

def profile_find():
    try:
        req = requests.get(f"https://{sm}.com/{username}")
        if req.status_code == 200:
            print(f"{GREEN}{username} found on {sm}{NORMAL}: https://{sm}.com/{username}")
        else:
            print(f"{RED}{username} not found on {sm}: {NORMAL}https://{sm}.com/{username}")
    except:
          print(f"{RED}Error connecting to {sm}")
        

social_media = [
    'facebook',
    'twitter',
    'linkedin',
    'instagram',
    'youtube',
    'pinterest',
    'snapchat',
    'tumblr',
    'reddit',
    'github',
    'medium',
    'tiktok',
    'whatsapp',
    'telegram',
    'vimeo',
    'quora',
    'flickr',
    'vkontakte',
    'weibo',
    'xing',
    'myspace',
    'badoo',
    'meetup',
    'foursquare',
    'yelp',
    'soundcloud',
    'deviantart',
    'behance',
    'dribbble',
    'stackexchange',
    'tripadvisor',
    'steam',
    'goodreads',
    'lastfm',
    'disqus',
    '500px',
    'couchsurfing',
    'viber',
    'kik',
    'vine',
    'ello',
    'imgur',
    'mix',
    'askfm',
    'patreon',
    'twitch',
    'vine',
    'newgrounds',
]

print(f"{BLUE}######  Profile-Hunter ######{NORMAL}")
print(f"{BLUE}[*] Credit: Invictus27{NORMAL}")
print(f"{BLUE}[*] This tool is for educational purposes only.{NORMAL}\n\n")


try:
	username = input(f'{BLUE}Enter  username:{NORMAL}')
	if username:
		for sm in social_media:
			profile_find()
	else:
		print(f'{RED}Enter Username!{NORMAL}')

except Exception as e:
	print(f'{RED}Error {e} {NORMAL}')
except:
	print(f'{RED}Error Profile-Hunter not working{NORMAL}')
