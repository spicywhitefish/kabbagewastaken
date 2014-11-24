Kabbage Was Taken

(ironically, kabbage.herokuapp.com was not claimed when this name was chosen)

Setup:

Required environment variables:
DJANGO_SECRET_KEY
TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET
TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET

Demo:

http://kabbagewastaken.herokuapp.com/

Performance:

The REST calls to the Twitter and Wikipedia APIs are fully blocking. Moving these to a job queue on another
thread/VM/server/region would allow the application to give snappier feedback that the user's query has indeed hit the
server.
If it's worth bragging about, doing search via an AJAX POST and changing browser history with Javascript does save
the bandwidth of sending the entire page again and improves client-side performance by not re-rendering the entire page

Areas for Improvement:

Unit testing for front-end components.
More correct error handling instead of bare excepts on API calls.
Logging.
Retrieving search results on GET requests with a valid querystring instead of simulating user action and loading results
via AJAX POST.
Better formatting of Tweet results.
Pagination of results.
Rendering the SearchForm in the template and easing the process of adding an additional search source.
Polishing the "source select" animation
Adding a little more color to the page (background, favicon, etc...)
