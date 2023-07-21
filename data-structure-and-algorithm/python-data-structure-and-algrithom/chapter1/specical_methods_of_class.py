class myClass():
    def __init__(self, greet):
        self.greet = greet
    def __repr__(self):
        return 'a custom object (%r)' % (self.greet)


cls1 = myClass('keixa')
print(cls1)