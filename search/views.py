import os
import json
from TwitterAPI import TwitterAPI
import urllib2
from urllib2 import URLError
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http.response import HttpResponse, HttpResponseBadRequest
from .forms import SearchForm


def search(request):
    if request.method == 'GET':
        return render_to_response('search/search.html', {}, RequestContext(request))
    else:
        form = SearchForm(request.POST)
        response_data = {}
        if form.is_valid():
            source = form.cleaned_data['source']
            results_context = {'source': form.cleaned_data['source']}
            has_results = False
            if source in ('twitter', 'both'):
                # Search Twitter
                try:
                    results_context['twitter_results'] = _search_twitter(form.cleaned_data['q'])
                except:
                    results_context["twitter_error"] = "Twitter appears to be offline"
                else:
                    has_results = True
            if source in ('wikipedia', 'both'):
                # Search Wikipedia
                try:
                    results_context['wiki_results'] = _search_wikipedia(form.cleaned_data['q'])
                except:
                    results_context["wiki_error"] = "Wikipedia appears to be offline"
                else:
                    has_results = True
            if has_results:
                response_data['reason'] = render_to_string("search/results.html", results_context)
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['reason'] = render_to_string("search/failure.html", results_context)
                return HttpResponseBadRequest(json.dumps(response_data), content_type="application/json")
        else:
            reason = 'Please select a search source'
            response_data['reason'] = render_to_string("search/failure.html", {'reason': reason})
            return HttpResponseBadRequest(json.dumps(response_data), content_type="application/json")

def _search_twitter(query):
    # Search Twitter
    consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
    consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
    access_token_key = os.environ.get("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    return [item['text'] for item in (api.request('search/tweets', {'q': query}))][:10]

def _search_wikipedia(query):
    query = "+".join(query.split())
    return [
        item for item in json.load(
            urllib2.urlopen(
                "http://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&srlimit=10&format=json".format(query)
            )
        )['query']['search']
    ]