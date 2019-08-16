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

Any input that can be cast into a dictionary will be digested; any data that cannot will be discarded.


```python
>>> from objgen.generators.generic import Base, Recursive
>>> b = Base(
...     {'this': 'is', 'valid': 'input'},
...     'this_is_not_pairwise_data',
...     [('this', 'however'), ('will', 'work'), ('just', 'fine')]
... )
Element cannot be cast into dict, and is being discarded: <class 'str'> this_is_not_pairwise_data
```

If multiples of a field exists in a given collection of input arguments, the most recent passed value for that field will be preserved.



```python
>>> b = Base({'this': 'is'}, [('this', 'however'), ])
>>> b
Base ['this']
>>> b.this
'however'
```

----

## gore ( fun! ( examples ) ) <a name="ex"></a>

+ [nesting is possible, intentional, and half the point of all this!](#ex_nesting_manual)
+ [nesting can be recursive, if we let it](#ex_nesting_recursive)
+ [recursive nesting can be inclusively/exclusively filtered](#ex_nesting_selective)


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

Let's make a `Recursive` generator to digest the full depth of the data structure -- having to call `cls.attr = Base(cls.attr)` for every single nested attributes at each given 'depth' is ridiculous.

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

### nesting -  selectively recursive <a name="ex_nesting_selective"></a>

So far so good - except, what if we *want* certain things to stay as dictionaries, rather than be indiscriminately digested?

For example, we want to add our `dog`'s friends, and be able to access `dog.friends` - however, it would be silly for each `{friend}` to become a `dog.friends.{friend}` attribute instead of staying preserved as elements in a data structure.

```python
... dog_info.update(
...     {
...         'friends': {
...             'lassie': {'breed': 'collie', 'met_at': 'dog park'},
...             'marnie': {'breed': 'shih tzu', 'met_at': 'dms'},
...             'air_bud': {'breed': 'golden retriever', 'met_at': 'basketball courts'},
...             'laika': {'breed': 'mongrel', 'met_at': 'outer space'}
...         }
...    }
...)
```

Let's make a `RecursiveFiltered` that deals with this for us.

Optionally, supply either `_exclude` or `_include_only` keyword arguments when creating the `RecursiveFilter` to determine which fields are (dis)allowed to be digested.

```python
>>> from objgen.generators.generic import RecursiveFiltered
>>>
>>> dog = RecursiveFiltered(dog_info, _exclude='friends')
>>>
>>> type(dog.actions)
<class 'objgen.generators.generic.RecursiveFiltered'>
>>> type(dog.friends)
<class 'dict'>

```

Note that excluding a field means that digestion along that path in the data tree will terminate at that field, rather than skip that field and continue down that path's depth.

----
[back](#ex)
