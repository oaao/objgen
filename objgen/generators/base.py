class Base:

    def __init__(self, *specs, **kwargs):

        for spec in specs:
            for field in spec:
                setattr(self, field, spec[field])

        for field in kwargs:
            setattr(self, field, kwargs[field])


class Recursive:

    def __init__(self, *specs, **kwargs):

        for spec in specs:
            for field in spec:
                if isinstance(spec[field], dict):
                    setattr(self, field, Recursive(spec[field]))
                else:
                    setattr(self, field, spec[field])

        for field in kwargs:
            if isinstance(spec[field], dict):
                setattr(self, field, Recursive(spec[field]))
            else:
                setattr(self, field, spec[field])