class foo:
    def __init__(self):
        pass

    def addDashes(fn):
        def newFunc(self):
            print("\nStart: %s" %(fn.__name__))
            fn(self)
            print("End: %s\n" %(fn.__name__))
        return newFunc

    @addDashes
    def bar(self):
        print('Hello')

    @addDashes
    def foobar(self):
        print('Hello Again')

if __name__ == "__main__":
    var = foo()
    var.bar()
    var.foobar()

