def compress(L):
    dc={v:i for i,v in enumerate(sorted(set(L)))}
    CL=[dc[i] for i in L]
    return CL,dc
