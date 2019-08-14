# objgen

Dynamically generate class objects by digesting key-value / pairwise data structures as object specifications.

`objgen` has no external dependencies and can be used immediately.


## usage

```python
>>> from objgen.generators.generic import Base
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

Anything that can be cast into a dictionary will be digested. Anything that cannot will be lost as information and announced as such.

```python
>>> from objgen.generators.generic import Base, Recursive
>>> b = Base(
...     {'this': 'is', 'valid': 'input'},
...     'this_is_not_pairwise_data',
...     [('this', 'however'), ('will', 'work'), ('just', 'fine')]
... )
Element cannot be cast into dict, and is being discarded: <class 'str'> this_is_not_pairwise_data
>>> b
Base ['this', 'valid', 'will', 'just']
```
----

## gore ( fun! ( examples ) ) <a name="ex"></a>

+ [nesting is possible, intentional, and half the point of all this!](#ex_nesting_manual)
+ [nesting can be recursive, if we let it](#ex_nesting_recursive)


### nesting - manual <a name="ex_nesting_manual"></a>

Say we want to create a `dog`, but also be able to access/call a `dog.actions.{action}`.
```python
>>> dog_info = {
...         'name': 'monty',
...         'breed': 'donkey child',
...         'is_good_boy': True,
...         'actions': {'run_to': 'car', 'bark_at': 'squirrel', 'pee_on': 'hydrant'},
...     }
```

Instantiate and hydrate a generator as `dog`, then do the same to the resulting `dog.actions`.

```python
>>> from objgen.generators.generic import Base
>>>
>>> dog = Base(dog_info)
>>> dog.actions
{'run_to': 'car', 'bark_at': 'squirrel', 'pee_on': 'hydrant'}
>>> dog.actions = Base(dog.actions)
>>> dog.actions.run_to
'car'
```

----
[back](#ex)

### nesting - recursive <a name="ex_nesting_recursive"></a>


Let's make a `Recursive` generator to digest the full depth of the data structure, since it would be ridiculous to have to `cls.attr = Base(cls.attr)` for all nested attributes at any 'depth'.

Whereas a `Base` generator will simply create `cls.key = value` relationships,
```python
                setattr(self, field, spec[field])
```

a `Recursive` generator will continue to digest any dictionary objects it encounters along any nesting path.

```python
                if isinstance(spec[field], dict):
                    setattr(self, field, Recursive(spec[field]))
```

Let's try making our `dog` again, but with a `Recursive` generator:

```python
>>> from objgen.generators.generic import Recursive
>>>
>>> dog = Recursive(dog_info)
>>> dog.actions
<objgen.generators.generic.Recursive object at 0x7f2bb4ef2c18>
>>> dog.actions.run_to
'car'
```

----
[back](#ex)
