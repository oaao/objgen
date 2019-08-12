class Base:

    def __init__(self, *specs, **kwargs):

        for spec in specs:
            for field in spec:
                setattr(self, field, spec[field])

        for field in kwargs:
            setattr(self, field, kwargs[field])
