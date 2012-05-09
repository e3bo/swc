def pairwise(fun, v1, v2):
    n = len(v1)
    assert n == len(v2), "Whoops: different lengths"
    ret = []
    for count in range(len(v1)):
        ret.append(fun(v1[count],v2[count]))
    return ret

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

