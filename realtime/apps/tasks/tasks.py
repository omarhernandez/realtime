import redis

def publish(name , message):
    comment_json = {
        'comment': 1,
        'user_name': name , 
        'submit_date':message}

    r = redis.StrictRedis()
    r.publish('channel_comments_',comment_json)

