class Base:

    def __init__(self, *specs, **kwargs):

        for spec in specs:
            self.digest(spec)

        self.digest(kwargs)

    def digest(self, data):
        for field in data:
            setattr(self, field, data[field])

    def __repr__(self):
        return f'{self.__class__.__name__} {list(vars(self).keys())}'


class Recursive(Base):

    def __init__(self, *specs, **kwargs):
        super(Recursive, self).__init__(*specs, **kwargs)

    def digest(self, data):
        for field in data:
            if isinstance(data[field], dict):
                setattr(self, field, Recursive(data[field]))
            else:
                setattr(self, field, data[field])
