from _collections_abc import MutableMapping


class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key
    
    def __len__(self):
        return len(self.data)


sorted_ranks = SortedDict()
votes = {
    'a': 200,
    'b': 125,
    'c': 155
}
