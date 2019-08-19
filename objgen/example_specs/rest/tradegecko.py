DEFAULT_FILTERS = [
    'ids',  # ?ids[]=1&ids[]=2
    'created_at_min',
    'created_at_max',
    'updated_at_min',
    'updated_at_max',
    'order',
    'limit',  # default 50, max 250
    'page'
]


ENDPOINTS = {

    'account': {

        'path': 'accounts',

        'actions': {
            # action: (method, subpath)
            'get_current': ('GET', '/current'),
            'update': ('PUT', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('location_ids', list),
            ('website', str),

            # writeable
            ('billing_contact_id', int),
            ('contact_email', str),
            ('contact_mobile', str),
            ('contact_phone', str),
            ('country', str),
            ('default_currency_id', int),
            ('default_order_price_list_id', str),
            ('default_payment_term_id', int),
            ('default_purchase_order_price_list_id', str),
            ('default_purchase_order_tax_type_id', int),
            ('default_sales_ledger_account_on', str),
            ('default_sales_order_tax_type_id', int),
            ('default_tax_exempt_id', int),
            ('default_tax_treatment', str),
            ('default_tax_type_id', int),
            ('industry', str),
            ('name', str),
            ('primary_location_id', int),
            ('primary_billing_location_id', int),
            ('stock_level_warn', bool),  # warn iDEFAULT_FILTERS = [
    'ids',  # ?ids[]=1&ids[]=2
    'created_at_min',
    'created_at_max',
    'updated_at_min',
    'updated_at_max',
    'order',
    'limit',  # default 50, max 250
    'page'
]


ENDPOINTS = {

    'account': {

        'path': 'accounts',

        'actions': {
            # action: (method, subpath)
            'get_current': ('GET', '/current'),
            'update': ('PUT', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('location_ids', list),
            ('website', str),

            # writeable
            ('billing_contact_id', int),
            ('contact_email', str),
            ('contact_mobile', str),
            ('contact_phone', str),
            ('country', str),
            ('default_currency_id', int),
            ('default_order_price_list_id', str),
            ('default_payment_term_id', int),
            ('default_purchase_order_price_list_id', str),
            ('default_purchase_order_tax_type_id', int),
            ('default_sales_ledger_account_on', str),
            ('default_sales_order_tax_type_id', int),
            ('default_tax_exempt_id', int),
            ('default_tax_treatment', str),
            ('default_tax_type_id', int),
            ('industry', str),
            ('name', str),
            ('primary_location_id', int),
            ('primary_billing_location_id', int),
            ('stock_level_warn', bool),  # warn if shipment tried without stock
            ('tax_label', str),
            ('tax_number', str),
            ('tax_number_label', str),
            ('time_zone', str),
            ('user_ids', list)
        ],

        'filters': []
    },

    'address': {

        'path': 'addresses',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),  # 'active' or 'archived'

            # writeable - required
            ('address1', str),
            ('company_id', int),

            #  writeable
            ('address2', str),
            ('city', str),
            ('company_name', str),
            ('country', str),
            ('country_code', str),
            ('email', str),
            ('first_name', str),
            ('last_name', str),
            ('label', str),
            ('phone_number', str),
            ('state', str),
            ('suburb', str),
            ('zip_code', str)
        ],

        'filters': [
            'company_id',
            'status'
        ]
    },

    'company': {

        'path': 'companies',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('address_ids', list),
            ('contact_ids', list),
            ('note_ids', list),

            # writeable - required
            ('company_type', str),  # 'business', 'supplier', or 'consumer'
            ('name', str),

            # writeable
            ('assignee_id', int),
            ('company_code', str),
            ('default_discount_rate', str),
            ('default_ledger_account_id', int),
            ('default_payment_term_id', int),
            ('default_price_list_id', str),
            ('default_stock_location_id', int),
            ('default_tax_type_id', int),
            ('description', str),
            ('email', str),
            ('fax', str),
            ('name', str),
            ('phone_number', str),
            ('status', str),  # 'active', 'archived', or 'disabled'
            ('tags', list),
            ('tax_number', str),
            ('website', str),
        ],

        'filters': [
            'status',  # 'active',  'disabled'
            'assignee_id',
            'company_code',
            'company_type',  # 'business', 'supplier', 'consumer'
            'default_ledger_account_id',
            'default_payment_term_id',
            'default_price_list_id',
            'default_stock_location_id',
            'default_tax_type_id',
            'email'
        ]
    },

    'contact': {

        'path': 'contacts',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),  # 'active' or 'archived'

            # writeable - required
            ('company_id', int),
            ('first_name', str),

            # writeable
            ('email', str),
            ('fax', str),
            ('last_name', str),
            ('location', str),
            ('mobile', str),
            ('notes', str),
            ('phone_number', str),
            ('position', str),
            ('online_ordering', bool)
        ],

        'filters': [
            'status',
            'company_id',
            'online_ordering'
        ]
    },

    'currency': {

        'path': 'currencies',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),  # 'active' or 'archived'

            # writeable - required
            ('iso', str),

            # writeable
            ('delimiter', str),
            ('format', str),  # %n number, %u unit e.g. %u%n -> '$12'
            ('name', str),
            ('precision', str),
            ('rate', str),  # exchange rate based on account's base currency
            ('separator', str),
            ('symbol', str)
        ],

        'filters': [
            'status'
        ]
    },

    'fulfillment': {

        'path': 'fulfillments',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),

            # writeable - required
            ('order_id', int),

            # writeable
            ('billing_address_id', int),
            ('shipping_address_id', int),
            ('stock_location_id', int),
            ('delivery_type', str),
            ('exchange_rate', str),
            ('notes', str),
            ('packed_at', str),
            ('received_at', str),
            ('service', str),
            ('status', str),   # 'packed', 'fulfilled', or 'deleted', 'void'
            ('tracking_company', str),
            ('tracking_number', str),
            ('tracking_url', str),

            # child attributes
            ('fulfillment_line_item_ids', list)

        ],

        'filters': [
            'billing_address_id',
            'company_id'
            'order_id',
            'receipt',
            'shipping_address_id',
            'status',  # 'packed', 'fulfilled', or 'deleted', 'void'
            'stock_location_id',
        ]
    },

    'fulfillment_line_item': {

        'path': 'fulfillment_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('base_price', str),
            ('variant_id', str),
            ('variant_sku', str),

            # writeable - required
            ('fulfillment_id', int),
            ('order_line_item_id', int),
            ('quantity', str),

            # writeable
            ('position', int),
        ],

        'filters': [
            'fulfillment_id',
            'order_line_item_id',
            'base_price',
            'position',
            'quantity'
        ]
    },

    'fulfillment_return': {

        'path': 'fulfillment_returns',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('company_id', int),

            # writeable - required
            ('order_id', int),

            # writeable
            ('credit_note_number', str),
            ('delivery_type', str),
            ('exchange_rate', str),
            ('location_id', int),
            ('notes', str),
            ('received_at', str),
            ('status', str),
            ('tracking_company', str),
            ('tracking_number', str),
            ('tracking_url', str),

            # child attributes
            ('fulfillment_return_line_item_ids', list),
        ],

        'filters': [
            'status',
            'company_id',
            'location_id',
            'order_id'
        ]
    },

    'fulfillment_return_line_items': {

        'path': 'fulfillment_return_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),

            # writeable - required
            ('fulfillment_return_id', int),
            ('order_line_item_id', int),
            ('quantity', str),

            # writeable
            ('base_price', str),
            ('ledger_account_id', int),
            ('position', int),
        ],

        'filters': [
            'fulfillment_return_id',
            'ledger_account_id',
            'order_line_item_id'
        ]
    },

    'image': {

        'path': 'images',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('base_path', str),
            ('file_name', str),
            ('image_processing', bool),
            ('position', int),
            ('versions', list),

            # writeable - required
            ('product_id', int),
            ('variant_ids', list),
            ('url', str),

            # writeable
            ('name', str)
        ],

        'filters': [
            'product_id',
            'uploader_id'
            'variant_ids',
        ]
    },

    'invoice': {

        'path': 'invoices',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('cached_total', str),
            ('company_id', str),
            ('currency_id', int),
            ('invoice_line_item_ids', list),
            ('order_number', str),
            ('payment_ids', list),
            ('payment_status', str),

            # writeable - required
            ('order_id', int),

            # writeable
            ('billing_address_id', int),
            ('due_at', str),
            ('exchange_rate', str),
            ('invoiced_at', str),
            ('invoice_number', str),
            ('notes', str),
            ('payment_term_id', int),
            ('shipping_address_id', int),

            # child attributes
            ('invoice_line_item_ids', list)
        ],

        'filters': [
            'billing_address_id',
            'company_id',
            'currency_id',
            'invoice_number',
            'order_id',
            'payment_status',
            'payment_term_id',
            'shipping_address_id',
        ]
    },

    'invoice_line_items': {

        'path': 'invoice_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),

            # writeable - required
            ('invoice_id', int),
            ('order_line_item_id', int),
            ('quantity', int),

            # writeable
            ('position', int)
        ],

        'filters': [
            'base_price',
            'invoice_id',
            'order_line_item_id',
            'position',
            'quantity'
        ]
    },

    'location': {

        'path': 'locations',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),

            # writeable - required
            ('address1', str),
            ('country', str),
            ('label', str),

            # writeable
            ('address2', str),
            ('city', str),
            ('country', str),  # two-letter code
            ('holds_stock', str),
            ('label', str),
            ('state', str),
            ('suburb', str),
            ('zip_code', str)

        ],

        'filters': [
            'status'
        ]
    },


    'note': {

        'path': 'notes',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('user_id', int),

            # writeable - required
            ('company_id', int),

            # writeable
            ('body', str),
        ],

        'filters': [
            'company_id',
            'user_id'
        ]
    },

    'order': {

        'path': 'orders',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),

            # create fulfillment with {'status': 'pack'}
            'pack': ('POST', '/{}/actions/pack'),

            # create fulfillment with {'status': 'fulfilled'}
            'fulfil': ('POST', '/{}/actions/fulfil'),

            'invoice': ('POST', '/{}/actions/invoice'),
            'pay': ('POST', '/{}/actions/pay'),
            'void': ('POST', '/{}/actions/void'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('document_url', str),
            ('backordering_status', str),  # not_backordered, partially_backordered, backordered  # noqa: 501
            ('fulfillment_ids', list),
            ('fulfillment_return_ids', list),
            ('fulfillment_status', str),  # unshipped, partial, shipped
            ('invoices', list),
            ('invoice_ids', list),  # uninvoiced, partial, invoiced
            ('invoice_numbers', dict),
            ('invoice_status', str),
            ('order_line_item_ids', list),
            ('packed_status', str),  # unpaid, partial, paid
            ('payment_ids', list),
            ('payment_status', str),
            ('refund_ids', list),
            ('return_status', str),  # unreturned, partial, returning
            ('returning_status', str),
            ('shippability_status', str),  # not_shippable, partially_shippable, shippable  # noqa: 501
            ('source_id', str),  # internal ID of app that created order
            ('total', str),
            ('user_id', int),

            # writeable - required
            ('billing_address_id', int),
            ('company_id', int),
            ('issued_at', str),
            ('shipping_address_id', int),

            # writeable
            ('status', str),  # draft, active, finalized
            ('assignee_id', int),
            ('contact_id', int),
            ('currency_id', int),
            ('default_price_list_id', str),
            ('document_url', str),
            ('email', str),
            ('notes', str),
            ('order_number', str),
            ('phone_number', str),
            ('reference_number', str),
            ('ship_at', str),
            ('source_id', str),
            ('source_url', str),
            ('stock_location_id', int),
            ('tags', list),
            ('tax_treatment', str),
            ('total', str),
            ('user_id', int),

            # child attributes
            ('order_line_item_ids', list)
        ],

        'filters': [
            'billing_address_id',
            'company_id',
            'contact_id',
            'currency_id',
            'order_number',
            'reference_number',
            'shipping_address_id',
            'source_id',
            'status',
            'stock_location_id',
            'tags',
            'user_id',
        ]
    },

    'order_line_items': {

        'path': 'order_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('fulfillment_line_item_ids', list),
            ('fulfillment_return_line_item_ids', list),
            ('invoice_line_item_ids', list),

            # writeable - required
            ('order_id', int),
            ('price', str),
            ('tax_type_id', int),
            ('variant_id', int),

            # writeable
            ('discount', str),
            ('freeform', bool),
            ('image_url', str),
            ('label', str),
            ('line_type', str),  # optional: product, discount, shipping, rounding, fee, gift_wrap # noqa: 501
            ('position', int),

        ],

        'filters': [
            'order_id',
            'order_status',
            'tax_type_id',
            'variant_id',
        ]
    },

    'payment_term': {

        'path': 'payment_terms',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('status', str),

            # writeable - required

            # writeable
        ],

        'filters': []
    },

    'product': {

        'path': 'products',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('image_url', str),
            ('quantity', str),
            ('status', str),

            # writeable - required
            ('name', str),

            # writeable
            ('brand', str),
            ('description', str),
            ('image_ids', list),
            ('opt1', str),  # custom product property name
            ('opt2', str),
            ('opt3', str),
            ('product_type', str),
            ('supplier_ids', list),
            ('tags', list),
            ('variant_ids', list),

            # child attributes - read-only
            ('variant_ids', list),

        ],

        'filters': [
            'status',  # 'active', 'disabled'
            'brand',
            'product_type',
            'tags'
        ]
    },

    'purchase_order': {

        'path': 'purchase_orders',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),

            # create a procurement for the PO
            'receive': ('POST', '/{}/actions/receive')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),
            ('cached_quantity', str),
            ('document_url', str),
            ('procurement_ids', list),
            ('procurement_status', str),
            ('received_at', str),
            ('total', str),

            # writeable - required
            ('company_id', int),
            ('due_at', str),  # default 14d from creation
            ('payment_due_at', str),  # default 14d from creation
            ('tax_treatment', str),  # 'exclusive'/'inclusive', account default

            # writeable
            ('billing_address_id', int),
            ('currency_id', int),
            ('default_price_list_id', str),
            ('email', str),
            ('notes', str),
            ('order_number', str),
            ('reference_number', str),
            ('stock_location_id', int),
            ('supplier_address_id', int),
            ('tags', str),

            # child attributes - read-only
            ('purchase_order_line_item_ids', list),
        ],

        'filters': [
            'procurement_id',
            'purchase_order_id',
            'purchase_order_status',
            'tax_type_id',
            'variant_id',
        ]
    },

    'purchase_order_line_item': {

        'path': 'purchase_order_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('base_price', str),
            ('image_url', str),
            ('extra_cost_value', str),
            ('procuremend_id', str),  # relevant if received

            # writeable - required
            ('purchase_order_id', str),
            ('variant_id', int),
            ('tax_type_id', int),
            ('price', str),

            # writeable
            ('freeform', bool),
            ('image_url', str),
            ('label', str),
            ('position', int),
            ('quantity', str),
            ('tax_rate_override', str)  # optional
        ],

        'filters': [
            'procurement_id',
            'purchase_order_id',
            'purchase_order_status',
            'tax_type_id',
            'variant_id',

        ]
    },

    'stock_adjustment': {

        'path': 'stock_adjustments',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('cached_quantity', str),
            ('cached_total', str),

            # writeable
            ('adjustment_number', str),
            ('notes', str),
            ('reason', str),  # reasons:
                                    # 'supplier' (new products)
                                    # 'customer' (returned goods)
                                    # 'damaged'
                                    # 'shrinkage'
                                    # 'promotion'
                                    # 'production'
            ('reason_label', str),  # combines this and the next field
            ('stock_adjustment_reason_id', int),  # internal ID
            ('stock_location_id', int),  # defaults to account primary_location

            # child attributes - read-only
            ('stock_adjustment_line_item_ids', list)
        ],

        'filters': [
            'adjustment_number',
            'stock_adjustment_reason_id',
            'stock_location_id'
        ]
    },

    'stock_adjustment_line_item': {

        'path': 'stock_adjustment_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),

            # writeable - required
            ('price', str),
            ('stock_adjustment_id', int),
            ('variant_id', int),

            # writeable
            ('position', int),
            ('quantity', str),
        ],

        'filters': [
            'stock_adjustment_id',
            'variant_id'
        ]
    },

    'stock_level': {

        'path': 'stock_levels',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('committed_stock', str),
            ('locations', str),
            ('stock_on_hand', str),
            ('incoming_stock', str)
        ],

        'filters': []
    },

    'stock_transfer': {

        'path': 'stock_transfers',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),

            'receive': ('POST', '/stock_transfers/{}/actions/receive'),
            'revert': ('POST', '/stock_transfers/{}/actions/revert')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('cached_quantity', str),

            # writeable - required
            ('destination_location_id', int),
            ('source_location_id', int),

            # writeable
            ('adjustment_number', str),
            ('cached_quantity', str),
            ('notes', str),
            ('received_at', str),  # auto set when status becomes 'received'
            ('status', str),  # active, received
            ('transacted_at', str),

            # child attributes - read-only
            ('stock_transfer_line_item_ids', list),

        ],

        'filters': [
            'status',
            'adjustment_number',
            'received_at',
            'notes',
            'source_location_id',
            'destination_location_id',
            'cached_quantity',
            'transacted_at',
            'stock_transfer_line_item_ids'
        ]
    },

    'stock_transfer_line_item': {

        'path': 'stock_transfer_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('image_url', str),

            # writeable - required
            ('stock_transfer_id', int),
            ('variant_id', int),

            # writeable
            ('quantity', str),
            ('position', int)
        ],

        'filters': []
    },

    'tax_type': {

        'path': 'tax_types',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('effective_rate', str),  # computed rate of child tax_components
            ('imported_from', str),
            ('status', str),  # active, archived
            ('tax_component_ids', list),

            # writeable - required
            ('name', str),

            # writeable
            ('code', str),
        ],

        'filters': [
            'status'
        ]
    },

    'user': {

        'path': 'users',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),
            ('account_id', str),
            ('login_id', int),

            # writeable - required

            # writeable
            ('action_items_email', str),  # off, daily, weekly
            ('avatar_url', str),
            ('billing_contact', bool),  # is user billing contact for account
            ('email', str),
            ('first_name', str),
            ('last_name', str),
            ('last_sign_in_at', str),
            ('location', str),
            ('mobile', str),
            ('notification_email', bool),
            ('permissions', list),
            ('phone_number', str),
            ('position', str),  # role in company
            ('sales_report_email', bool),
        ],

        'filters': [
            'status',
            'account_id',
            'login_id',
        ]
    },

    'variant': {

        'path': 'variants',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),  # active, archived
            ('committed_stock', str),
            ('incoming_stock', str),
            ('last_cost_price', str),
            ('locations', str),
            ('moving_average_cost', str),
            ('product_name', str),
            ('product_status', str),
            ('product_type', str),
            ('stock_on_hand', str),  # stock across all locations

            # writeable - required
            ('product_id', int),

            # writeable
            ('buy_price', str),
            ('composite', bool),  # is variant composed of other variants
            ('default_ledger_account_id', int),
            ('description', str),
            ('image_ids', list),
            ('initial_cost_price', str),
            ('initial_stock_level', str),
            ('initial_stock_location_id', int),
            ('keep_selling', bool),
            ('locations', list),  # list of per-warehouse data on variant
            ('manage_stock', bool),  # always true for composites
            ('max_online', str),  # integrated stores show this max value
            ('name', str),
            ('online_ordering', bool),  # is for sale on B2B platform? (N/A)
            ('opt1', str),
            ('opt2', str),
            ('opt3', str),
            ('position', str),
            ('purchasable', bool),  # can create PO with variant
            ('retail_price', str),
            ('sellable', str),  # can be added to sales orders
            ('sku', str),
            ('supplier_code', str),
            ('taxable', bool),
            ('upc', str),  # barcode number
            ('variant_prices', list),
                # list of [{'price_list_id': 'retail', 'value': '12.0'}, ..., ]
            ('weight', str),
            ('weight_unit', str),
            ('wholesale_price', str)
        ],

        'filters': [
            'status',
            'product_id',
            'sku'
        ]
    },

    'webhook': {

        'path': 'webhooks',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),

            # writeable - required
            ('event', str),
            ('address', str)
        ],

        'events': {
            # 'object': ('action1', 'action2', ...) ---> 'object.action1'
            'account': ('update', ),
            'address': ('create', 'update'),
            'channel': ('destroy', ),
            'company': ('create', 'update'),
            'contact': ('create', 'update'),
            'document_theme': ('update', ),
            'fulfillment': ('create', 'fulfilled'),
            'fulfillment_return': ('create'),
            'invoice': ('create', ),
            'location': ('create', 'update'),
            'order': ('create', 'finalized', 'fulfilled'),
            'payment': ('create', ),
            'product': ('create', ),
            'procurement': ('create', ),
            'purchase_order': ('create', ),
            'stock_adjustment': ('create', ),
            'stock_transfer': ('create', ),
            'variant': ('create', 'stock_level_update'),
            'image': ('create', )
        },

        'filters': []
    },

    # 'endpoint': {

    #     'path': '',

    #     'actions': {
    #         # action: (method, subpath)
    #         'get_all': ('GET', ''),
    #         'get': ('GET', '/{}'),
    #         'create': ('POST', '/'),
    #         'update': ('PUT', '/{}'),
    #         'delete': ('DELETE', '/{}'),
    #     },

    #     'attributes': [
    #         # read-only
    #         ('id', int),
    #         ('created_at', str),
    #         ('updated_at', str),

    #         # writeable - required

    #         # writeable
    #     ],

    #     'filters': []
    # },
}

#  a) consider hard sectioning of r/o, w-req, w, and child attrs
#  b) consider (http_method, subpath, desired_response)
#     instead of (http_method, subpath) -> 200, 201, 203...
#  CHECK child classes - all # child attributes to be ('', list)
pment tried without stock
            ('tax_label', str),
            ('tax_number', str),
            ('tax_number_label', str),
            ('time_zone', str),
            ('user_ids', list)
        ],

        'filters': []
    },

    'address': {

        'path': 'addresses',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),  # 'active' or 'archived'

            # writeable - required
            ('address1', str),
            ('company_id', int),

            #  writeable
            ('address2', str),
            ('city', str),
            ('company_name', str),
            ('country', str),
            ('country_code', str),
            ('email', str),
            ('first_name', str),
            ('last_name', str),
            ('label', str),
            ('phone_number', str),
            ('state', str),
            ('suburb', str),
            ('zip_code', str)
        ],

        'filters': [
            'company_id',
            'status'
        ]
    },

    'company': {

        'path': 'companies',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('address_ids', list),
            ('contact_ids', list),
            ('note_ids', list),

            # writeable - required
            ('company_type', str),  # 'business', 'supplier', or 'consumer'
            ('name', str),

            # writeable
            ('assignee_id', int),
            ('company_code', str),
            ('default_discount_rate', str),
            ('default_ledger_account_id', int),
            ('default_payment_term_id', int),
            ('default_price_list_id', str),
            ('default_stock_location_id', int),
            ('default_tax_type_id', int),
            ('description', str),
            ('email', str),
            ('fax', str),
            ('name', str),
            ('phone_number', str),
            ('status', str),  # 'active', 'archived', or 'disabled'
            ('tags', list),
            ('tax_number', str),
            ('website', str),
        ],

        'filters': [
            'status',  # 'active',  'disabled'
            'assignee_id',
            'company_code',
            'company_type',  # 'business', 'supplier', 'consumer'
            'default_ledger_account_id',
            'default_payment_term_id',
            'default_price_list_id',
            'default_stock_location_id',
            'default_tax_type_id',
            'email'
        ]
    },

    'contact': {

        'path': 'contacts',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),  # 'active' or 'archived'

            # writeable - required
            ('company_id', int),
            ('first_name', str),

            # writeable
            ('email', str),
            ('fax', str),
            ('last_name', str),
            ('location', str),
            ('mobile', str),
            ('notes', str),
            ('phone_number', str),
            ('position', str),
            ('online_ordering', bool)
        ],

        'filters': [
            'status',
            'company_id',
            'online_ordering'
        ]
    },

    'currency': {

        'path': 'currencies',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),  # 'active' or 'archived'

            # writeable - required
            ('iso', str),

            # writeable
            ('delimiter', str),
            ('format', str),  # %n number, %u unit e.g. %u%n -> '$12'
            ('name', str),
            ('precision', str),
            ('rate', str),  # exchange rate based on account's base currency
            ('separator', str),
            ('symbol', str)
        ],

        'filters': [
            'status'
        ]
    },

    'fulfillment': {

        'path': 'fulfillments',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),

            # writeable - required
            ('order_id', int),

            # writeable
            ('billing_address_id', int),
            ('shipping_address_id', int),
            ('stock_location_id', int),
            ('delivery_type', str),
            ('exchange_rate', str),
            ('notes', str),
            ('packed_at', str),
            ('received_at', str),
            ('service', str),
            ('status', str),   # 'packed', 'fulfilled', or 'deleted', 'void'
            ('tracking_company', str),
            ('tracking_number', str),
            ('tracking_url', str),

            # child attributes
            ('fulfillment_line_item_ids', list)

        ],

        'filters': [
            'billing_address_id',
            'company_id'
            'order_id',
            'receipt',
            'shipping_address_id',
            'status',  # 'packed', 'fulfilled', or 'deleted', 'void'
            'stock_location_id',
        ]
    },

    'fulfillment_line_item': {

        'path': 'fulfillment_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('base_price', str),
            ('variant_id', str),
            ('variant_sku', str),

            # writeable - required
            ('fulfillment_id', int),
            ('order_line_item_id', int),
            ('quantity', str),

            # writeable
            ('position', int),
        ],

        'filters': [
            'fulfillment_id',
            'order_line_item_id',
            'base_price',
            'position',
            'quantity'
        ]
    },

    'fulfillment_return': {

        'path': 'fulfillment_returns',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('company_id', int),

            # writeable - required
            ('order_id', int),

            # writeable
            ('credit_note_number', str),
            ('delivery_type', str),
            ('exchange_rate', str),
            ('location_id', int),
            ('notes', str),
            ('received_at', str),
            ('status', str),
            ('tracking_company', str),
            ('tracking_number', str),
            ('tracking_url', str),

            # child attributes
            ('fulfillment_return_line_item_ids', list),
        ],

        'filters': [
            'status',
            'company_id',
            'location_id',
            'order_id'
        ]
    },

    'fulfillment_return_line_items': {

        'path': 'fulfillment_return_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),

            # writeable - required
            ('fulfillment_return_id', int),
            ('order_line_item_id', int),
            ('quantity', str),

            # writeable
            ('base_price', str),
            ('ledger_account_id', int),
            ('position', int),
        ],

        'filters': [
            'fulfillment_return_id',
            'ledger_account_id',
            'order_line_item_id'
        ]
    },

    'image': {

        'path': 'images',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('base_path', str),
            ('file_name', str),
            ('image_processing', bool),
            ('position', int),
            ('versions', list),

            # writeable - required
            ('product_id', int),
            ('variant_ids', list),
            ('url', str),

            # writeable
            ('name', str)
        ],

        'filters': [
            'product_id',
            'uploader_id'
            'variant_ids',
        ]
    },

    'invoice': {

        'path': 'invoices',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('cached_total', str),
            ('company_id', str),
            ('currency_id', int),
            ('invoice_line_item_ids', list),
            ('order_number', str),
            ('payment_ids', list),
            ('payment_status', str),

            # writeable - required
            ('order_id', int),

            # writeable
            ('billing_address_id', int),
            ('due_at', str),
            ('exchange_rate', str),
            ('invoiced_at', str),
            ('invoice_number', str),
            ('notes', str),
            ('payment_term_id', int),
            ('shipping_address_id', int),

            # child attributes
            ('invoice_line_item_ids', list)
        ],

        'filters': [
            'billing_address_id',
            'company_id',
            'currency_id',
            'invoice_number',
            'order_id',
            'payment_status',
            'payment_term_id',
            'shipping_address_id',
        ]
    },

    'invoice_line_items': {

        'path': 'invoice_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),

            # writeable - required
            ('invoice_id', int),
            ('order_line_item_id', int),
            ('quantity', int),

            # writeable
            ('position', int)
        ],

        'filters': [
            'base_price',
            'invoice_id',
            'order_line_item_id',
            'position',
            'quantity'
        ]
    },

    'location': {

        'path': 'locations',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),

            # writeable - required
            ('address1', str),
            ('country', str),
            ('label', str),

            # writeable
            ('address2', str),
            ('city', str),
            ('country', str),  # two-letter code
            ('holds_stock', str),
            ('label', str),
            ('state', str),
            ('suburb', str),
            ('zip_code', str)

        ],

        'filters': [
            'status'
        ]
    },


    'note': {

        'path': 'notes',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('user_id', int),

            # writeable - required
            ('company_id', int),

            # writeable
            ('body', str),
        ],

        'filters': [
            'company_id',
            'user_id'
        ]
    },

    'order': {

        'path': 'orders',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),

            # create fulfillment with {'status': 'pack'}
            'pack': ('POST', '/{}/actions/pack'),

            # create fulfillment with {'status': 'fulfilled'}
            'fulfil': ('POST', '/{}/actions/fulfil'),

            'invoice': ('POST', '/{}/actions/invoice'),
            'pay': ('POST', '/{}/actions/pay'),
            'void': ('POST', '/{}/actions/void'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('document_url', str),
            ('backordering_status', str),  # not_backordered, partially_backordered, backordered  # noqa: 501
            ('fulfillment_ids', list),
            ('fulfillment_return_ids', list),
            ('fulfillment_status', str),  # unshipped, partial, shipped
            ('invoices', list),
            ('invoice_ids', list),  # uninvoiced, partial, invoiced
            ('invoice_numbers', dict),
            ('invoice_status', str),
            ('order_line_item_ids', list),
            ('packed_status', str),  # unpaid, partial, paid
            ('payment_ids', list),
            ('payment_status', str),
            ('refund_ids', list),
            ('return_status', str),  # unreturned, partial, returning
            ('returning_status', str),
            ('shippability_status', str),  # not_shippable, partially_shippable, shippable  # noqa: 501
            ('source_id', str),  # internal ID of app that created order
            ('total', str),
            ('user_id', int),

            # writeable - required
            ('billing_address_id', int),
            ('company_id', int),
            ('issued_at', str),
            ('shipping_address_id', int),

            # writeable
            ('status', str),  # draft, active, finalized
            ('assignee_id', int),
            ('contact_id', int),
            ('currency_id', int),
            ('default_price_list_id', str),
            ('document_url', str),
            ('email', str),
            ('notes', str),
            ('order_number', str),
            ('phone_number', str),
            ('reference_number', str),
            ('ship_at', str),
            ('source_id', str),
            ('source_url', str),
            ('stock_location_id', int),
            ('tags', list),
            ('tax_treatment', str),
            ('total', str),
            ('user_id', int),

            # child attributes
            ('order_line_item_ids', list)
        ],

        'filters': [
            'billing_address_id',
            'company_id',
            'contact_id',
            'currency_id',
            'order_number',
            'reference_number',
            'shipping_address_id',
            'source_id',
            'status',
            'stock_location_id',
            'tags',
            'user_id',
        ]
    },

    'order_line_items': {

        'path': 'order_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('fulfillment_line_item_ids', list),
            ('fulfillment_return_line_item_ids', list),
            ('invoice_line_item_ids', list),

            # writeable - required
            ('order_id', int),
            ('price', str),
            ('tax_type_id', int),
            ('variant_id', int),

            # writeable
            ('discount', str),
            ('freeform', bool),
            ('image_url', str),
            ('label', str),
            ('line_type', str),  # optional: product, discount, shipping, rounding, fee, gift_wrap # noqa: 501
            ('position', int),

        ],

        'filters': [
            'order_id',
            'order_status',
            'tax_type_id',
            'variant_id',
        ]
    },

    'payment_term': {

        'path': 'payment_terms',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('status', str),

            # writeable - required

            # writeable
        ],

        'filters': []
    },

    'product': {

        'path': 'products',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('image_url', str),
            ('quantity', str),
            ('status', str),

            # writeable - required
            ('name', str),

            # writeable
            ('brand', str),
            ('description', str),
            ('image_ids', list),
            ('opt1', str),  # custom product property name
            ('opt2', str),
            ('opt3', str),
            ('product_type', str),
            ('supplier_ids', list),
            ('tags', list),
            ('variant_ids', list),

            # child attributes - read-only
            ('variant_ids', list),

        ],

        'filters': [
            'status',  # 'active', 'disabled'
            'brand',
            'product_type',
            'tags'
        ]
    },

    'purchase_order': {

        'path': 'purchase_orders',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),

            # create a procurement for the PO
            'receive': ('POST', '/{}/actions/receive')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),
            ('cached_quantity', str),
            ('document_url', str),
            ('procurement_ids', list),
            ('procurement_status', str),
            ('received_at', str),
            ('total', str),

            # writeable - required
            ('company_id', int),
            ('due_at', str),  # default 14d from creation
            ('payment_due_at', str),  # default 14d from creation
            ('tax_treatment', str),  # 'exclusive'/'inclusive', account default

            # writeable
            ('billing_address_id', int),
            ('currency_id', int),
            ('default_price_list_id', str),
            ('email', str),
            ('notes', str),
            ('order_number', str),
            ('reference_number', str),
            ('stock_location_id', int),
            ('supplier_address_id', int),
            ('tags', str),

            # child attributes - read-only
            ('purchase_order_line_item_ids', list),
        ],

        'filters': [
            'procurement_id',
            'purchase_order_id',
            'purchase_order_status',
            'tax_type_id',
            'variant_id',
        ]
    },

    'purchase_order_line_item': {

        'path': 'purchase_order_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('base_price', str),
            ('image_url', str),
            ('extra_cost_value', str),
            ('procuremend_id', str),  # relevant if received

            # writeable - required
            ('purchase_order_id', str),
            ('variant_id', int),
            ('tax_type_id', int),
            ('price', str),

            # writeable
            ('freeform', bool),
            ('image_url', str),
            ('label', str),
            ('position', int),
            ('quantity', str),
            ('tax_rate_override', str)  # optional
        ],

        'filters': [
            'procurement_id',
            'purchase_order_id',
            'purchase_order_status',
            'tax_type_id',
            'variant_id',

        ]
    },

    'stock_adjustment': {

        'path': 'stock_adjustments',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('cached_quantity', str),
            ('cached_total', str),

            # writeable
            ('adjustment_number', str),
            ('notes', str),
            ('reason', str),  # reasons:
                                    # 'supplier' (new products)
                                    # 'customer' (returned goods)
                                    # 'damaged'
                                    # 'shrinkage'
                                    # 'promotion'
                                    # 'production'
            ('reason_label', str),  # combines this and the next field
            ('stock_adjustment_reason_id', int),  # internal ID
            ('stock_location_id', int),  # defaults to account primary_location

            # child attributes - read-only
            ('stock_adjustment_line_item_ids', list)
        ],

        'filters': [
            'adjustment_number',
            'stock_adjustment_reason_id',
            'stock_location_id'
        ]
    },

    'stock_adjustment_line_item': {

        'path': 'stock_adjustment_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),

            # writeable - required
            ('price', str),
            ('stock_adjustment_id', int),
            ('variant_id', int),

            # writeable
            ('position', int),
            ('quantity', str),
        ],

        'filters': [
            'stock_adjustment_id',
            'variant_id'
        ]
    },

    'stock_level': {

        'path': 'stock_levels',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('committed_stock', str),
            ('locations', str),
            ('stock_on_hand', str),
            ('incoming_stock', str)
        ],

        'filters': []
    },

    'stock_transfer': {

        'path': 'stock_transfers',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),

            'receive': ('POST', '/stock_transfers/{}/actions/receive'),
            'revert': ('POST', '/stock_transfers/{}/actions/revert')
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('cached_quantity', str),

            # writeable - required
            ('destination_location_id', int),
            ('source_location_id', int),

            # writeable
            ('adjustment_number', str),
            ('cached_quantity', str),
            ('notes', str),
            ('received_at', str),  # auto set when status becomes 'received'
            ('status', str),  # active, received
            ('transacted_at', str),

            # child attributes - read-only
            ('stock_transfer_line_item_ids', list),

        ],

        'filters': [
            'status',
            'adjustment_number',
            'received_at',
            'notes',
            'source_location_id',
            'destination_location_id',
            'cached_quantity',
            'transacted_at',
            'stock_transfer_line_item_ids'
        ]
    },

    'stock_transfer_line_item': {

        'path': 'stock_transfer_line_items',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('image_url', str),

            # writeable - required
            ('stock_transfer_id', int),
            ('variant_id', int),

            # writeable
            ('quantity', str),
            ('position', int)
        ],

        'filters': []
    },

    'tax_type': {

        'path': 'tax_types',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('effective_rate', str),  # computed rate of child tax_components
            ('imported_from', str),
            ('status', str),  # active, archived
            ('tax_component_ids', list),

            # writeable - required
            ('name', str),

            # writeable
            ('code', str),
        ],

        'filters': [
            'status'
        ]
    },

    'user': {

        'path': 'users',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),
            ('account_id', str),
            ('login_id', int),

            # writeable - required

            # writeable
            ('action_items_email', str),  # off, daily, weekly
            ('avatar_url', str),
            ('billing_contact', bool),  # is user billing contact for account
            ('email', str),
            ('first_name', str),
            ('last_name', str),
            ('last_sign_in_at', str),
            ('location', str),
            ('mobile', str),
            ('notification_email', bool),
            ('permissions', list),
            ('phone_number', str),
            ('position', str),  # role in company
            ('sales_report_email', bool),
        ],

        'filters': [
            'status',
            'account_id',
            'login_id',
        ]
    },

    'variant': {

        'path': 'variants',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),
            ('status', str),  # active, archived
            ('committed_stock', str),
            ('incoming_stock', str),
            ('last_cost_price', str),
            ('locations', str),
            ('moving_average_cost', str),
            ('product_name', str),
            ('product_status', str),
            ('product_type', str),
            ('stock_on_hand', str),  # stock across all locations

            # writeable - required
            ('product_id', int),

            # writeable
            ('buy_price', str),
            ('composite', bool),  # is variant composed of other variants
            ('default_ledger_account_id', int),
            ('description', str),
            ('image_ids', list),
            ('initial_cost_price', str),
            ('initial_stock_level', str),
            ('initial_stock_location_id', int),
            ('keep_selling', bool),
            ('locations', list),  # list of per-warehouse data on variant
            ('manage_stock', bool),  # always true for composites
            ('max_online', str),  # integrated stores show this max value
            ('name', str),
            ('online_ordering', bool),  # is for sale on B2B platform? (N/A)
            ('opt1', str),
            ('opt2', str),
            ('opt3', str),
            ('position', str),
            ('purchasable', bool),  # can create PO with variant
            ('retail_price', str),
            ('sellable', str),  # can be added to sales orders
            ('sku', str),
            ('supplier_code', str),
            ('taxable', bool),
            ('upc', str),  # barcode number
            ('variant_prices', list),
                # list of [{'price_list_id': 'retail', 'value': '12.0'}, ..., ]
            ('weight', str),
            ('weight_unit', str),
            ('wholesale_price', str)
        ],

        'filters': [
            'status',
            'product_id',
            'sku'
        ]
    },

    'webhook': {

        'path': 'webhooks',

        'actions': {
            # action: (method, subpath)
            'get_all': ('GET', ''),
            'get': ('GET', '/{}'),
            'create': ('POST', '/'),
            'update': ('PUT', '/{}'),
            'delete': ('DELETE', '/{}'),
        },

        'attributes': [
            # read-only
            ('id', int),
            ('created_at', str),
            ('updated_at', str),

            # writeable - required
            ('event', str),
            ('address', str)
        ],

        'events': {
            # 'object': ('action1', 'action2', ...) ---> 'object.action1'
            'account': ('update', ),
            'address': ('create', 'update'),
            'channel': ('destroy', ),
            'company': ('create', 'update'),
            'contact': ('create', 'update'),
            'document_theme': ('update', ),
            'fulfillment': ('create', 'fulfilled'),
            'fulfillment_return': ('create'),
            'invoice': ('create', ),
            'location': ('create', 'update'),
            'order': ('create', 'finalized', 'fulfilled'),
            'payment': ('create', ),
            'product': ('create', ),
            'procurement': ('create', ),
            'purchase_order': ('create', ),
            'stock_adjustment': ('create', ),
            'stock_transfer': ('create', ),
            'variant': ('create', 'stock_level_update'),
            'image': ('create', )
        },

        'filters': []
    },

    # 'endpoint': {

    #     'path': '',

    #     'actions': {
    #         # action: (method, subpath)
    #         'get_all': ('GET', ''),
    #         'get': ('GET', '/{}'),
    #         'create': ('POST', '/'),
    #         'update': ('PUT', '/{}'),
    #         'delete': ('DELETE', '/{}'),
    #     },

    #     'attributes': [
    #         # read-only
    #         ('id', int),
    #         ('created_at', str),
    #         ('updated_at', str),

    #         # writeable - required

    #         # writeable
    #     ],

    #     'filters': []
    # },
}

#  a) consider hard sectioning of r/o, w-req, w, and child attrs
#  b) consider (http_method, subpath, desired_response)
#     instead of (http_method, subpath) -> 200, 201, 203...
#  CHECK child classes - all # child attributes to be ('', list)
