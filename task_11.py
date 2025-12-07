class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        if value is None:
            self._calories = None
        else:
            try:
                self._calories = float(value)
            except (ValueError, TypeError):
                self._calories = None

    def is_healthy(self):
        return self._calories is not None and self._calories < 200

    def is_delicious(self):
        return True