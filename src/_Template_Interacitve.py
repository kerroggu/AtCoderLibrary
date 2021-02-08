

def judge(x):
    an=a[x-1]
    print(an)
    return an

def query(x): # for submission
    print('?',x)
    sys.stdout.flush()
    y=I()
    return y

def query(x): # for local test
    print('?',x)
    sys.stdout.flush()
    #y=I()
    y=judge(x)
    return y
