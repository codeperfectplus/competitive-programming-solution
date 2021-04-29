import datetime

def add(moment):
    result = moment + datetime.timedelta(seconds=1e9)
    return result
