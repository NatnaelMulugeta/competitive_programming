class RecentCounter:

    def __init__(self):
        self.req = []

    def ping(self, t: int) -> int:
        while self.req and t - self.req[0] > 3000:
            self.req.pop(0)
        self.req.append(t)
        return len(self.req)