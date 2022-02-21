import collections

a = dict()
a = {}
a = {'key1': 'value1', 'key2': 'value2'}
a['key3'] = 'value3'
print(a)

for k, v in a.items():
    print(k, v)

default_dict = collections.defaultdict(int)
default_dict['A'] = 5
default_dict['B'] = 4
print(default_dict)

list = [1, 2, 3, 4, 5, 5, 5, 6, 6]
counter = collections.Counter(list)
print(counter)

print(counter.most_common(2))

print(collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}))
