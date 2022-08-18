from top_tweets import top_tweets

if __name__ == "__main__":
    print("""
Elige función: 
[1] Top 10 tweets
[2] Top 10 users
[3] Top 10 days
[4] Top 10 hashtags""")
    a = input()
    while int(a) not in range(1,5):
        print("Elige de nuevo")
        a = input()
    print("Elegiste", a)
    if a == '1':
        top_tweets()
    elif a == '2':
        pass
        # top_users()
    elif a == '3':
        pass
        # top_days()
    else:
        pass
        # top_hashtags()
