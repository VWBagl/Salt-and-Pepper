from task_11 import Dessert

class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = None
        self.set_flavor(flavor)
    
    def get_flavor(self):
        return self._flavor
    
    def set_flavor(self, flavor):
        try:
            if flavor is None:
                self._flavor = None
            else:
                self._flavor = str(flavor).strip()
        except (ValueError, TypeError):
            self._flavor = None
    
    def is_delicious(self):
        if self._flavor.lower() == "black licorice":
            return False
        return True
