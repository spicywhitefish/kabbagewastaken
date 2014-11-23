import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http.response import HttpResponse, HttpResponseBadRequest

def search(request):
    if request.method == 'GET':
        return render_to_response('search/search.html', {}, RequestContext(request))
    else:
        response_data = {
            'reason': render_to_string("search/failure.html", {'reason': 'Search not implemented yet!'})
        }
        return HttpResponseBadRequest(json.dumps(response_data), content_type="application/json")