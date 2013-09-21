from django.shortcuts import render_to_response
import redis
from django.contrib.comments.signals import comment_was_posted

def main(request):
	return render_to_response('main/index.html',ctx,  context_instance = RequestContext(request)  )


def publish(request):
    comment_json = {
        'comment': 1,
        'user_name': 'user name',
        'submit_date':'date' }

    r = redis.StrictRedis()
    r.publish('channel_comments_%s_%s' % (comment.content_type.id, comment.object_pk), comment_json)

