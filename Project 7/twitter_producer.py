import tweepy
import time
from confluent_kafka import Producer
import time
import logging
import json


api_key ="esbTFosPhgM5aM3qR6u6XlaKt"
api_secret ="egsaXsdI45Eu5XoU09tY4KyYj9A40uTLXHLYDRsotKeZhyw1l7"
bearer_token =r"AAAAAAAAAAAAAAAAAAAAACVShwEAAAAAXO6MzFXiHTB7e5xzT88e5%2Bvrga0%3DRxjRKlO0lYmlTgyXX643tWDvQDsab004DF0AmCXVQEURhwS1eA"
access_token ="1577563364619735041-vCeuegMZxH6dEdhcnpYf5bPlhiUpLE"
access_token_secret="jzEQng6OnusDqyMdA4OFGvZ8F9HpItX3O2j0GnB3GuCJz"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

search_terms =["naruto"]
###############
logging.basicConfig(format='%(message)s',
                    filename='producer.log',
                    filemode='w')

###############
p=Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logging.info(message)
        print(message)

###############
def main():
    class MyStream(tweepy.StreamingClient):
        def on_connect(self):
            print('Connected')

        def on_tweet(self, tweet):
            if tweet.referenced_tweets == None:
                data = {
                    'id' : tweet.id,
                    'text' : tweet.text
                    }
                print(data)
                m=json.dumps(data)
                logging.warning(data)
                p.poll(1)
                p.produce('naruto-topic', m.encode('utf-8'),callback=receipt) 
                time.sleep(0.2)

    stream = MyStream(bearer_token= bearer_token)
    
    for term in search_terms:
        stream.add_rules(tweepy.StreamRule(term))
        stream.filter(tweet_fields=["referenced_tweets"])

if __name__ == '__main__':
    main()
