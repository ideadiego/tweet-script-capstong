import json
def top_tweets():
    with open('farmers-protest-tweets-2021-03-5.json', 'r') as data:
        entries = []
        for i in range(3):
            entries.append(json.loads(data.readline()))
    print(entries[0]['url'])

if __name__ == "__main__":
    top_tweets()