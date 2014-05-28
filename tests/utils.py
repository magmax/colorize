class FakeIO(object):
    def __init__(self, stream):
        self._lines = stream.splitlines()

    def readline(self):
        return self.next()

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.closed:
            raise StopIteration()
        return self._lines.pop(0)

    @property
    def closed(self):
        return len(self._lines) == 0
