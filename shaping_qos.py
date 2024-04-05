import time
import threading

class TokenBucket:
    def __init__(self, tokens_capacity, init_tokens, fill_rate) -> None:
        self.capacity = tokens_capacity
        self._tokens = init_tokens
        self.fill_rate = fill_rate
        self.lock = threading.Lock()
        self.last_time = time.time()
    
    def _add_tokens(self):
        now_time = time.time()
        if self.last_time:
            elapsed = now_time - self.last_time
            tokens_to_add = elapsed * self.fill_rate
            self._tokens = min(self.capacity, self._tokens + tokens_to_add)
        self.last_time = now_time

    def consume_tokens_with_generated(self, tokens):
        with self.lock:
            self._add_tokens()
            if self._tokens >= tokens:
                self._tokens -= tokens
                return True
            else:
                return False

    def get_current_tokens_with_generated(self):
        with self.lock:
            self._add_tokens()
            return self._tokens


if __name__ == '__main__':
    bucket = TokenBucket(10, 5, 1) # one produced per sec, and 0.5 sec consuming/sending one.
    print('prepared:\n')
    for i in range(20):
        time.sleep(0.5)
        if bucket.consume_tokens_with_generated(1):
            print(f'Succeed to send packet, times={i}')
        else:
            print(f'not enough to consume')
