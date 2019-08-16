class Base:

    def __init__(self, *specs, **kwargs):

        for spec in specs:
            try:
                spec_dict = dict(spec)
                self.digest(spec_dict)
            except ValueError:
                print(f'Element cannot be cast into dict, and is being discarded: {type(spec)} {spec}')

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


class RecursiveFiltered(Recursive):

    _exclude      = None
    _include_only = None

    def __init__(self, *specs, **kwargs):

        if '_exclude' in kwargs and not '_include_only' in kwargs:
            self._exclude = self._allow_single_element(kwargs.pop('_exclude'))
        elif '_include_only' in kwargs and not '_exclude' in kwargs:
            self._include_only = self._allow_single_element(kwargs.pop('_include_only'))
        elif '_exclude' in kwargs and '_include_only' in kwargs:
            raise Exception('The parameters _exclude and _include_only may not be used together.')

        super(RecursiveFiltered, self).__init__(*specs, **kwargs)

    def digest(self, data):

        if self._include_only:
            digestible = (k for k, v in data.items() if k in self._include_only)
            print(f' Included only: {self._include_only}')
        elif self._exclude:
            digestible = (k for k, v in data.items() if k not in self._exclude)
            print(f' Excluded: {self._exclude}')
        else:
            digestible = data

        for field in data:
            if isinstance(data[field], dict) and field in digestible:
                setattr(self, field, RecursiveFiltered(data[field]))
            else:
                setattr(self, field, data[field])

    def _allow_single_element(self, data):

        if isinstance(data, str):
            t = [data]
        else:
            t = data

        return t
