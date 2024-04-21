from time import time

class RateLimiter:
    def __init__(self, rate):
        self.rate = rate
        self.tokens = self.rate
        self.last_check = time()

    def allow(self):
        now = time()
        elapsed = now - self.last_check
        self.last_check = now
        self.tokens += elapsed * self.rate
        if self.tokens > self.rate:
            self.tokens = self.rate
        if self.tokens < 1:
            return False
        self.tokens -= 1
        return True
