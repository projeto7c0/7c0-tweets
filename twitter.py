import tweepy
import twitter_auth
import time
from datetime import datetime

def tweet(handle, tweet, archive_url, creation_date, idTweets, status):
    api = twitter_auth.autentica_tweets()
    status = api.update_status(in_reply_to_status_id = status.id, status = "O tweet com id " + str(idTweets[0]) + " de " + str(creation_date) + " que falava sobre: ")
    # print(str(idTweets[0]) + " - " + creation_date)
    tweet = str(tweet).replace("//", "/ /")
    status = api.update_status(in_reply_to_status_id = status.id, status = (tweet[0:200]+"..."))
    # print(tweet[0:200])
    if not archive_url.startswith("Não"):
        # print(archive_url)
        status = api.update_status(in_reply_to_status_id = status.id, status = "O bot tentou arquivar o tweet nesse link: " + archive_url)
    
    return status

def tweet_start():
    api = twitter_auth.autentica_tweets()
    status = api.update_status(status = ("Começando o relatório às " + datetime.now().isoformat(timespec='minutes') +". Os tweets serão espaçados de tempos em tempos, para evitar que o bot seja bloqueado pelo twitter."))
    # print(datetime.now().isoformat(timespec='minutes'))
    
    return status


def tweet_start_arroba(handle, qtde_tweets):
    api = twitter_auth.autentica_tweets()
    status = api.update_status("Começando a listagem de tweets recuperados para a arroba " + handle[0] + ". Sumiram desde a nossa última checagem " + str(qtde_tweets) + " tweets.")
    # print(handle[0] +"  "+ str(qtde_tweets))

    return status

def tweet_end(qtde_tweets):
    api = twitter_auth.autentica_tweets()
    print(qtde_tweets)
    status = api.update_status("Fim da triagem diária, foram encontrados " + str(qtde_tweets) + " tweets que sumiram compartilhe o perfil @projeto7c0 para que mais " +
                               "pessoas saibam o que desaparece da timeline dos políticos.")
    status = api.update_status(in_reply_to_status_id = status.id, status = "Quer saber mais sobre o projeto? Acesse https://projeto7c0.com.br/ e veja saiba tudo sobre o projeto")
    status = api.update_status(in_reply_to_status_id = status.id, status = "Quer ajudar a financiar a transparência na comunicação da democracia brasileira? Acesse o nosso apoia-se em https://apoia.se/projeto-7c0 e veja como contribuir")
    api.update_status(in_reply_to_status_id = status.id, status = "Quer ficar atualizado? Assine a nossa newsletter, que teremos informações quinzenais para você! Para assinar só clicar aqui https://projeto7c0.us20.list-manage.com//subscribe/post?u=984470f280d60b82c247e3d7b&id=00a31b0d4a")

def tweet_end_arroba(arroba, last_tweet):
    api = twitter_auth.autentica_tweets()
    api.update_status(in_reply_to_status_id = last_tweet.id, status = ("Fim da listagem de tweets recuperados para a arroba " + arroba[0]))
    # print(arroba[0])
