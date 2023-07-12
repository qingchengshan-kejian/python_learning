def recv(maxsize, *, block):
    pass

recv(1024, True)
# 需要1个位置参数，给了两个
recv(1024, block=True)
# block是一个关键字参数


def minium(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


minium(1, 5, 2, -5, 10) # -5
minium(1, 5, 2, -5, 10, clip=0) # 0