class ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        return {
            k: self._traverse(k, v) for k, v in instance_dict.items() 
        }

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        
        if isinstance(value, dict):
            return self._traverse_dict(value)
        
        if isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        
        if hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)

        return value


class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BinaryTree(
    10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11))
)
print(tree.to_dict())

# {'value': 10,
#  'left': {'value': 7,
#           'left': None,
#           'right': {'value': 9,
#                     'left': None,
#                     'right': None}},
#  'right': {'value': 13,
#            'left': {'value': 11,
#                     'left': None,
#                     'right': None},
#            'right': None}}
