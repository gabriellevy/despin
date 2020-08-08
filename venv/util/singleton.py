
'''
Metaclasse empêchant la création d'autres instances de toutes les classes l'utilisant comme métaclasse
Créer une seonde instance implique d'accéder à celle précédemment créée
'''

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
