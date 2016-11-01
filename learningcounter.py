from collections import Counter

counter = Counter('superfluous')
counter['u']
list(counter.elements())
counter.most_common(2)

counter_one = counter
counter_two = Counter('super')
counter_one.subtract(counter_two)
counter_one
list(counter_one.elements())
