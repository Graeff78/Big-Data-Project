from db_config import get_redis_connection
import json
from TV import TV
""" 
This class will connect to redis and load JSON data onto the redis API

establish redis connection.
db_setup 
""" 
r = get_redis_connection()
""" 
call request objects. 
transform and load item data into redis.json.
""" 
def load(item):
    tv_show = TV(item)
    r.json().set('shows:'+str(tv_show.name)+'', '.', json.dumps(item))
