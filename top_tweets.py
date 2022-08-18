import json
def top_tweets():
    print("calculando top tweets...")
    with open('farmers-protest-tweets-2021-03-5.json', 'r') as data:
        entries = []
        for line in data.readlines():
            entries.append(json.loads(line))
    max_count = 0
    url = ""
    for entrie in entries:
        if entrie['retweetCount'] > max_count:
            url = entrie["url"]
            max_count = entrie['retweetCount']
    print(f'url: {url}, retweets: {max_count}')

if __name__ == "__main__":
    top_tweets()