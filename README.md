# objgen

Dynamically generate Python class objects by digesting key-value / pairwise data structures as object specifications.

## usage

```python
>>> from objgen.generators.base import Base
>>> base = Base()
>>> vars(base)
{}
```

Pass a dictionary to a generator instance to construct its object, then use the object.

```python
>>> hydrated = Base({'attr1': 'val1', 'attr2': 'val2'}, attr3='val3')
>>> vars(hydrated)
{'attr1': 'val1', 'attr2': 'val2', 'attr3': 'val3'}
>>> hydrated.attr1, hydrated.attr2, hydrated.attr3
('val1', 'val2', 'val3')
```

## gore ( fun! ( examples ) )

+ [nesting is possible, intentional, and half the point of all this!](#ex_nesting_manual)

### nesting - manual <a name="ex_nesting_manual"></a>

Say we want to create a `dog`, but also be able to access/call a `dog.actions.{action}`.
```python
>>> dog_info = {
...         'name': 'monty',
...         'is_good_boy': True,
...         'actions': {'run_to': 'car', 'bark_at': 'squirrel', 'pee_on': 'hydrant'},
...     }
```

Instantiate and hydrate a generator as `dog`, then do the same to the resulting `dog.actions`.

```python
>>> from objgen.generators.base import Base
>>> dog = Base(dog_info)
>>> dog.actions
{'run_to': 'car', 'bark_at': 'squirrel', 'pee_on': 'hydrant'}
>>> dog.actions = Base(dog.actions)
>>> dog.actions.run_to
'car'
```
