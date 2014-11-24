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
            results_context = {}
            has_results = False
            if source in ('twitter', 'both'):
                # Search Twitter
                consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
                consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
                access_token_key = os.environ.get("TWITTER_ACCESS_TOKEN")
                access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
                try:
                    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
                    results_context['twitter_results'] = (
                        [item['text'] for item in (api.request('search/tweets', {'q': form.cleaned_data['q']}))][:10]
                    )
                    has_results = True
                except:
                    results_context["twitter_error"] = "Twitter appears to be offline"
            if source in ('wikipedia', 'both'):
                # Search Wikipedia
                try:
                    results_context['wiki_results'] = [item['snippet'] for item in json.load(urllib2.urlopen(
                        "http://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&srlimit=10&format=json".format(form.cleaned_data['q']))
                    )['query']['search']]
                    has_results = True
                except Exception as e:
                    print e
                    results_context["wiki_error"] = "Wikipedia appears to be offline"
            if has_results:
                response_data['reason'] = render_to_string("search/results.html", results_context)
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data['reason'] = render_to_string("search/failure.html", results_context)
                return HttpResponseBadRequest(json.dumps(response_data), content_type="application/json")
        else:
            for field in form.fields:
                print field.errors
            reason = 'Please select a search source'
            response_data['reason'] = render_to_string("search/failure.html", {'reason': reason})
            return HttpResponseBadRequest(json.dumps(response_data), content_type="application/json")