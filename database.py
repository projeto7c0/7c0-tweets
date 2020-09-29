import re, time
import database_auth

def get_handles_to_tweet():
    sql = "select distinct(handle) from mimic_tweets where erased = 1 and 7c0_tweeted = 0;"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchall()
    except Exception as E:
        print(E)
    finally:
        db.close()

    return value

def get_candidatos():
    sql = "select * from candidatos_2020;"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchall()
    except Exception as E:
        print(E)
    finally:
        db.close()

    return value



def get_tweets_ids(conta):
    print(conta)
    sql = "select idTweets from mimic_tweets where handle = \"" + conta[0] + "\" and 7c0_tweeted = 0 and erased = 1 order by idTweets asc;"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchall()
    except Exception as E:
        print(E)
    finally:
        db.close()

    return value

def get_tweets_ids_election(conta):
    print(conta)
    sql = "select idTweets from election_tweets_2020 where handle = \"" + conta[1] + "\" and 7c0_tweeted = 0 and erased = 1 order by idTweets asc;"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchall()
    except Exception as E:
        print(E)
    finally:
        db.close()

    return value


def retrieve_tweet(tweet_id):
    sql = "select * from mimic_tweets where idTweets = \"" + str(tweet_id[0]) + "\";"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchone()
    except Exception as E:
        print(E)
    finally:
        db.close()

    if value:
        if value[10]:
            return tweet_id, value[2], value[4], value[10], value[3]
        else:
            return tweet_id, value[2], value[4], "Não arquivado", value[3]
    else:
        return [0], "", "", "Não arquivado", ""

def retrieve_tweet_election(tweet_id):
    sql = "select * from election_tweets_2020 where idTweets = \"" + str(tweet_id[0]) + "\";"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchone()
    except Exception as E:
        print(E)
    finally:
        db.close()

    if value:
        if value[11]:
            return tweet_id, value[2], value[4], value[11], value[3]
        else:
            return tweet_id, value[2], value[4], "Não arquivado", value[3]
    else:
        return [0], "", "", "Não arquivado", ""


def update_tweeted(id_set):
    db = database_auth.conecta_banco()
    cursor = db.cursor()

    sql = "update mimic_tweets set 7c0_tweeted = 1 where idTweets in ("

    for id in id_set:
        sql += "\"" + str(id[0]) + "\","

    sql += "\"0\");"

    try:
        cursor.execute(sql)
    except Exception as E:
        print(E)

    db.commit()
    db.close()


def update_tweeted_election(id_set):
    db = database_auth.conecta_banco()
    cursor = db.cursor()

    sql = "update election_tweets_2020 set 7c0_tweeted = 1 where idTweets in ("

    for id in id_set:
        sql += "\"" + str(id[0]) + "\","

    sql += "\"0\");"

    try:
        cursor.execute(sql)
    except Exception as E:
        print(E)

    db.commit()
    db.close()
