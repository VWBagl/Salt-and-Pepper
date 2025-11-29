class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = None
        self._calories = None
        self.set_name(name)
        self.set_calories(calories)
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if name is None or isinstance(name, str):
            self._name = name
        else:
            self._name = str(name)
    
    def get_calories(self):
        return self._calories
    
    def set_calories(self, calories):
        try:
            if calories is None:
                self._calories = None
            else:
                self._calories = float(calories)
        except (ValueError, TypeError):
            self._calories = None
    
    def is_healthy(self):
        if self._calories is None:
            return False
        return self._calories < 200
    
    def is_delicious(self):
        return True


