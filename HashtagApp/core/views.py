from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from HashtagApp.core.services import GitHubService

def index(request):
    if request.method == 'POST':
        hashtag = request.POST['hashtag']
        hashtag = hashtag.replace(" ", "+")
        github_service = GitHubService()
        posts = github_service.get_posts(hashtag)
        hashtag = hashtag.replace("+", " ")
        return render(request, 'index.html', { 'hashtag' : hashtag, 'posts' : posts })
    else:
		return render(request, 'index.html')