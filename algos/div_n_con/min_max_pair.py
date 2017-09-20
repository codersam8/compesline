class MinMaxPair:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __str__(self):
        return 'min is %s, max is %s' % (self.min, self.max)
