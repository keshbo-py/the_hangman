import praw
import config
#import time

def bot_login():
    print("Logging in...")
    r = praw.Reddit(client_id=config.client_id,
                         client_secret=config.client_secret,
                         username=config.username,
                         password=config.password,
                         user_agent=config.user_agent)
    print("Logged in!")
    return r

def run_bot(r, subreddit, id_list):

    print("Looking for comments...")
    for comment in r.subreddit(subreddit).comments(limit=25):
        if "!hangman" in comment.body and comment.id not in id_list and comment.author != r.user.me():
            comment.reply("You Called Me?")
            print("Comment found!")
            id_list.append(comment.id)
            with open("id_list_txt.txt", "a") as f:
                f.write(comment.id + "\n")

#    print("sleeping... zzz...")
#    time.sleep(10)
#    print("Waked Up!")

def save_comment():
    with open("id_list_txt.txt", "r") as f:
        id_list = f.read()
        id_list = id_list.split("\n")
        return id_list

id_list = save_comment()
r = bot_login()
sub = "test"

while True:
    try:
        run_bot(r, sub, id_list)
    except:
        print("\n\nRate Limit\n\n")