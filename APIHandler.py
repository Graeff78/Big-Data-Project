import requests
import json
from Headers import *
from Loader import load
""" 
This class pulls the GET meta data from the source db API.

establish http connection.
Use JSON format to fit into queried request object.
"""
def fetch():

    author = auth()
    """ 
    increase range for more movie data. 10 movies per page.
    """ 
    for page in range(1, 8001):

        url = "https://api.themoviedb.org/3/discover/tv?include_adult=false&include_null_first_air_dates=false&language=en-US&page="+str(page)+"&sort_by=popularity.desc"
        headers = {
            "accept": author.type,
            "Authorization": author.key
        }
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)

        """ 
        #call loader instance to inject movie into redis
        """ 
        for item in data["results"]:
            load(item)
    
#url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page="+str(page)+"&sort_by=popularity.desc"