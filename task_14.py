class EvenNumbers:
    def __init__(self, n):
        self.n = self._check_input(n)

    def _check_input(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return 0
    
    def __iter__(self):
            return (i * 2 for i in range(self.n))
