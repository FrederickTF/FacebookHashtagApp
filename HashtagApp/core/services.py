import urllib, urllib2, json, operator
from urllib2 import Request, urlopen
from operator import itemgetter

class GitHubService:
    def get_posts(self, hashtag):
        token =  '<insert your token here>'

        fb_posts = 'https://graph.facebook.com/search?q=%23' + hashtag + '&type=post&limit=999' + '&access_token=' + token

        request = Request(fb_posts)
        data = json.load(urlopen(request))

        data = data['data']

        posts = []

        for post in data:
			id = post['from']['id']
			name = post['from']['name']
			time = post['updated_time']
			description = 'no description'
			if 'description' in post:
				if '#'+hashtag.lower() in post['description'].lower():
					description = post['description']
			if 'message' in post:
				if '#'+hashtag.lower() in post['message'].lower():
					description = post['message']
			if 'caption' in post:
				if '#'+hashtag.lower() in post['caption'].lower():
					description = post['caption']
			if 'name' in post:
				if '#'+hashtag.lower() in post['name'].lower():
					description = post['name']
			
			posts.append({ 'id' : id, 'name' : name, 'time' : time, 'description' : description })
	return posts
