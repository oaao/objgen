DOG_INFO = {
    'name': 'monty',
    'breed': 'donkey child',
    'is_good_boy': True,
    'actions': {'run_to': 'car', 'bark_at': 'squirrel', 'pee_on': 'hydrant'},
}


EXAMPLE_ENDPOINT = {
    'path': 'my_path',

    'actions': {
        # action: (http_verb, subpath)
        'get_all': ('GET', '/'),
        'get':     ('GET', '/{}'),
    },

    'attributes': [
        # attr_name, type
        ('name', str),
        ('age', int),
        ('hobbies', list)
    ]
}

MULTIPLE_ENDPOINT = {

    'person': {
        'path': 'people',

        'actions': {
            # action: (http_verb, subpath)
            'get_all': ('GET', '/'),
            'get':     ('GET', '/{}'),
        },

        'attributes': [
            # attr_name, type
            ('name', str),
            ('age', int),
            ('hobbies', list)
        ],
    },

    'pet': {
        'path': 'pets',

        'actions': {
            'get_all': ('GET', '/'),
            'get':     ('GET', '/{}'),
        },

        'attributes': [
            ('name', str),
            ('age', int),
            ('species', str),
        ]
    }
}
