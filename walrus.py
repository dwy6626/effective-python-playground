# before
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get('apple', 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        to_enjoy = 'Nothing'

# after
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('apple', 0)) >= 4:
    to_enjoy = make_cider(count)
else:
    to_enjoy = 'Nothing'

# before
while True:
    fresh_fruit = pick_fruit()
    if not fresh_fruit:
        break
    
    ...

# after
while (fresh_fruit := pick_fruit()):
    if not fresh_fruit:
        break
    
    ...
