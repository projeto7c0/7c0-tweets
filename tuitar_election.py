if __name__ == '__main__':
    import time
    import database
    import twitter_election

    print("iniciando a coleta de arrobas para tuitar")
    # arrobas = database.get_handles_to_tweet_election()
    candidatos = database.get_candidatos()

    print("Coletados " + str(len(candidatos)) + " arrobas para tuitar...")

    print("iniciando processo de tuites... ")
    # twitter_election.tweet_start()

    qtde_tweets = 0
    for candidato in candidatos:
        tweet_ids = database.get_tweets_ids_election(candidato)
        last_tweet = twitter_election.tweet_start_arroba(candidato, len(tweet_ids))
        for tweet_id in tweet_ids:
            qtde_tweets += 1
            id, tweet, handle, archive_url, creation_date = database.retrieve_tweet(tweet_id)
            last_tweet = twitter_election.tweet(handle, tweet, archive_url, creation_date, id, last_tweet)
            if not qtde_tweets%20:
                time.sleep(3600)
        
        database.update_tweeted_election(tweet_ids)
        twitter_election.tweet_end_arroba(candidato, last_tweet)
