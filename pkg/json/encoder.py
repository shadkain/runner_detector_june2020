from json import JSONEncoder


class Encoder(JSONEncoder):
    def default(self, o):
        if hasattr(o, '__json__'):
            return o.__json__()
        else:
            return super().default(o)