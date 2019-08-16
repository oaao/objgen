DOG_INFO = {
    'name': 'monty',
    'breed': 'donkey child',
    'is_good_boy': True,
    'actions': {'run_to': 'car', 'bark_at': 'squirrel', 'pee_on': 'hydrant'},
}

DOG_INFO_FILTERING = DOG_INFO
DOG_INFO_FILTERING.update({
     'friends': {
         'lassie': {'breed': 'collie', 'met_at': 'dog park'},
         'marnie': {'breed': 'shih tzu', 'met_at': 'dms'},
         'air_bud': {'breed': 'golden retriever', 'met_at': 'basketball courts'},
         'laika': {'breed': 'mongrel', 'met_at': 'outer space'}
    }
})


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
