class MyClass:
    def __init__(self) -> None:
        self.alligator = 'hatchling'
        self.elephant = 'calf'

for key, value in MyClass().__dict__.items():
    print(f'{key}: {value}')
