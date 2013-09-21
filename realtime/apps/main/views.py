from django.template import RequestContext
from django.shortcuts import render_to_response

def main(request):
	ctx = { 'NODE_JS_SERVER' : 'localhost:8081' }
	return render_to_response('main/index.html',ctx,  context_instance = RequestContext(request)  )











