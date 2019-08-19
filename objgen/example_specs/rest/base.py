SINGLE_ENDPOINT = {
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