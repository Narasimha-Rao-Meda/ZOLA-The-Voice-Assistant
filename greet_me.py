import datetime

hour = int(list(str(list(str(datetime.datetime.now()).split(" "))[1]).split(":"))[0])


def greet():
    if hour>=6 and hour<12:
        return "good morning"
    elif hour>=12 and hour<18:
        return "good afternoon"
    else:
        return "good evening"