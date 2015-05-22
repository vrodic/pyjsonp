import simplejson
import urllib2
from cgi import parse_qs, escape

def application(env, start_response):

	parameters = parse_qs(env.get('QUERY_STRING', ''))
	if 'url' in parameters:
		url = urllib2.unquote(parameters['url'][0])
	else: 
		return "no url param"
	
	req = urllib2.Request(url)
	opener = urllib2.build_opener()
	f = opener.open(req)
	json = simplejson.load(f)
	
	start_response('200 OK', [('Content-Type', 'text/html')])
	return [simplejson.JSONEncoder().encode(json)]