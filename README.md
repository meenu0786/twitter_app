# twitter_app

This repository help you to create the new tweet and get the list of all the tweets.

# README
This README covers setup instructions and how to run the api's.

# Twiiter App API's 
## this api is used to create a new tweet  
        endpoint: <domain name>/create_tweet/
        request method: POST 
        request data : {'name': "<your name>", 'message':"<your message"}
        response : {"id", "name", "message", "time"}  

## this api is used to get the list of all tweet
        endpoint: <domain name>/get_tweet_list/
        request method: GET 
        query_params : {'sort_by': "name/time"}
        response :[{"id", "name", "message", "time"}, ......]