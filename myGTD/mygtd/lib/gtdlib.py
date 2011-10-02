# GTD module

__author__ = 'lubson'

import datetime

def duePhrase(date):
    phrase = ''
    if date is not None:
        deltaDue = (date - now()).days + 1
        if deltaDue > 1:
            phrase = 'Due in ' + str(deltaDue) + ' days'
        elif deltaDue == 1:
            phrase = 'Tomorrow'
        elif deltaDue == 0:
            phrase = 'Today'
        elif deltaDue == -1:
            phrase = 'Yesterday'
        else:
            phrase = str((-1)*deltaDue) + ' days late'
    return phrase

def dateState(date):
    state = ''
    if date is not None:
        deltaDue = (date - now()).days + 1
        if deltaDue > 0:
            state = 'ok'
        if deltaDue == 0:
            state = 'today'
        else:
            state = 'late'
    return state

def isInToday(date):
    if date is not None and ((date - now()).days + 1) <= 0:
        return True
    else:
        return False

def now():
    return datetime.datetime.now()