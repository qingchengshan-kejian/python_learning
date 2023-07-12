def sample():
    n = 0
    # Closure function
    def func():
        print('n=', n)

    # accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()

f.set_n(10)
f()