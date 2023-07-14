import time
class timeC:
    def Cal(self, func, args):
        a = time.perf_counter()
        res = func(args)
        b = time.perf_counter()
        print(b-a)
        return b-a, res