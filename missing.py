class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value
