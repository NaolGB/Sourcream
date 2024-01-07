mandt = 'SC1'

sales_orgs = {
    'UK': {
        'distribution_channels': {'TR': 'Truck Delivery'},
        'sales_offices': {'UK-1': 'London, Holborn Office'}
    }
}

shipping_conditions = {
    'SS': 'Standard Shipping',
    'ES': 'Express Shipping'
}

dd07t_combinations = {
    'VBAK': [
        {'DOMVALUE_L': 'C', 'DOMNAME': 'VBTYP', 'DDTEXT': 'Order'},
        {'DOMVALUE_L': 'I', 'DOMNAME': 'VBTYP', 'DDTEXT': 'Order w/o charge'},
    ],
    'TVAK': [
        {'DOMVALUE_L': 'D', 'DOMNAME': 'KLIMP', 'DDTEXT': 'D' }, # TODO add custom values
    ]
}

goods_movement_types = { # TODO check codes
    'GoodsIssue': {'code': '601', 'is_reverse': None},
    'ReverseGoodsReceipt': {'code': '102', 'is_reverse': 'X'},
    'ReturnGoodsReceipt': {'code': '651', 'is_reverse': 'X'},
    'ReturnDeliveryToVendor': {'code': '122', 'is_reverse': 'X'},
}

sales_doc_types = {
    'OR': 'Standard Order',
    'QT': 'Quotation',
}

om_company_codes = {
    'CC-1': {
        'BUKRS': 'CC01',
        'BUTXT': 'UK-HLB-01',
    }
}

om_valuation_areas = ['VA01']

om_plants = {
    "UK-1": {'country_key': 'UK', 'country_name': 'United Kingdom', 'plant_number': 'PL01'}
}

om_dimensions = {
    'DIM-1': {
        'DIMID': 'DIM',
        'MSSIE': 'ST'
    }
}

om_units = {
    'UNIT-1': {
        'MSEHI': 'UNT',
        'DIMID': 'DIM', # -- must matech om_dimensions' DIMID
    }
}

om_material_groups = {
    'GRP-1': {
        'MATKL': 'GROUP-013',
        'WGBEZ': 'Group 013'
    }
}

om_material_types = {
    'MAT-1': {
        'MTART': 'ST-1',
        'MTBEZ': 'Standard Material'
    }
}

om_industries = {
    'IND-1': {
        'MBRSH': 'I',
        'MBBEZ': 'Food and Beverages'
    }
}

om_status = {
    'apprive_sales_order': {
        'ISTAT': 'I0002',
        'TXT30': 'Approve'
    }
}

om_billing_blocks = {
    '01': {
        'FAKSP': '01',
        'VTEXT': 'Standard Billing Block'
    }
}

om_delivery_blocks = {
    '01': {
        'LIFSP': '01',
        'VTEXT': 'Standard Delivery Block'
    }
}

om_customers = {
    "Tasty Bites Co.": {"credit_risk": 0.61, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109653'},
    "Brewmaster's Blend": {"credit_risk": 0.28, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109654'},
    "Crispy Cravings": {"credit_risk": 0.85, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109655'},
    "Sips & Savories": {"credit_risk": 0.68, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109656'},
    "Gourmet Delights Inc.": {"credit_risk": 0.21, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109657'},
    "Flavor Fusion Foods": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109658'},
    "Café Elegance": {"credit_risk": 0.29, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109659'},
    "SodaStreamers": {"credit_risk": 0.48, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109660'},
    "Sweets & Sips": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109661'},
    "Gastronomy Galore": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109662'},
    "Nectar Nook": {"credit_risk": 0.35, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109663'},
    "Spice & Savor": {"credit_risk": 0.54, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109664'},
    "Wholesome Treats": {"credit_risk": 0.52, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109665'},
    "Munchies Magic": {"credit_risk": 0.71, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109666'},
    "Siplicity Drinks": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109667'},
    "Foodie Fantasy": {"credit_risk": 0.37, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109668'},
    "Yummy Morsels": {"credit_risk": 0.51, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109669'},
    "Baker's Bliss Co.": {"credit_risk": 0.67, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109670'},
    "ThirstQuencher": {"credit_risk": 0.13, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109671'},
    "Epicurean Eats": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109672'},
    "Gusto Gourmets": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109673'},
    "Beverage Bliss": {"credit_risk": 0.44, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109674'},
    "Taste Troupe": {"credit_risk": 0.77, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109675'},
    "ChocoCharm Confections": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109676'},
    "SavorStreet": {"credit_risk": 0.40, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109677'},
    "Culinary Crafters": {"credit_risk": 0.70, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109678'},
    "BrewBurst Beverages": {"credit_risk": 0.09, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109679'},
    "NoshNation": {"credit_risk": 0.82, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109680'},
    "Gastronomic Gather": {"credit_risk": 0.38, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109681'},
    "FreshNosh": {"credit_risk": 0.73, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109682'},
    "Greyjoy Foods Inc.": {"credit_risk": 0.63, 'payment_term': 'Z030', 'country': 'Westeros', 'region': 'Iron Islands', 'city': 'Pyke', 'id': 'C109683'},
}

om_routes = {
    'R-1': {
        'ROUTE': 'SEA',
        'TRAZTD': 14
    }
}

om_users = {
    "Alex Johnson": {'type': 'A', 'nation': 'UK'},
    "Bailey Smith": {'type': 'A', 'nation': 'UK'},
    "Carmen Davis": {'type': 'A', 'nation': 'UK'},
    "Darnell Williams": {'type': 'A', 'nation': 'UK'},
    "Evelyn Brown": {'type': 'A', 'nation': 'UK'},
    "Francis Taylor": {'type': 'A', 'nation': 'UK'},
    "Gabriel Moore": {'type': 'A', 'nation': 'UK'},
    "Harper Clark": {'type': 'A', 'nation': 'UK'},
    "Ibrahim Lewis": {'type': 'A', 'nation': 'UK'},
    "Jaden Hall": {'type': 'A', 'nation': 'UK'},
    "Kai Lee": {'type': 'A', 'nation': 'UK'},
    "Logan Mitchell": {'type': 'A', 'nation': 'UK'},
    "Morgan Anderson": {'type': 'A', 'nation': 'UK'},
    "Nathan Harris": {'type': 'A', 'nation': 'UK'},
    "Olive White": {'type': 'A', 'nation': 'UK'},
    "Peyton Turner": {'type': 'A', 'nation': 'UK'},
    "Quinn Martin": {'type': 'A', 'nation': 'UK'},
    "Riley Walker": {'type': 'A', 'nation': 'UK'},
    "Sasha Baker": {'type': 'A', 'nation': 'UK'},
    "Taylor Turner": {'type': 'A', 'nation': 'UK'},
    'Catelyn Stark': {'type': 'A', 'nation': 'Westeros'},
    "BATCH_JOB": {'type': 'B', 'nation': 'UK'},
}

om_materials = {
    "Rice": {"price": 2.99, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058832'}, # type(E) = 'in house production
    "Coffee": {"price": 5.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058833'}, 
    "Tea": {"price": 3.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058834'}, 
    "Soda": {"price": 1.49, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058835'}, 
    "Bottled Water": {"price": 0.99, "availability": 1.0, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058836'}, 
    "Chips": {"price": 2.79, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058837'}, 
    "Cookies": {"price": 3.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058838'}, 
    "Candy": {"price": 1.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058839'}, 
    "Ice Cream": {"price": 4.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058840'}, 
    "Frozen Pizza": {"price": 5.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058841'}, 
    "Canned Soup": {"price": 1.79, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058842'}, 
    "Honey": {"price": 4.29, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058843'}, 
    "Peanut Butter": {"price": 3.29, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058844'}, 
    "Jam": {"price": 2.99, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058845'}, 
    "Canned Vegetables": {"price": 1.69, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058846'}, 
    "Frozen Vegetables": {"price": 2.49, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058847'}, 
    "Olive Oil": {"price": 6.99, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058848'}, 
    "Vinegar": {"price": 2.19, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058849'}, 
    "Balsamic Vinegar": {"price": 4.99, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058850'}, 
    "Wine": {"price": 9.99, "availability": 0.4, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058851'}, 
    "Beer": {"price": 1.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058852'}, 
    "Worcestershire Sauce": {"price": 2.79, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058853'}, 
    "Pickles": {"price": 2.49, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058854'}, 
    "Olives": {"price": 3.29, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058855'}, 
    "Canned Tuna": {"price": 1.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058856'}, 
    "Canned Salmon": {"price": 3.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058857'}, 
    "Dried Fruits": {"price": 4.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058858'}, 
    "Nuts": {"price": 5.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058859'}, 
    "Hamburger Buns": {"price": 2.49, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058860'}, 
    "Hot Dog Buns": {"price": 2.29, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058861'}, 
    "Mustard": {"price": 1.79, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058862'}, 
    "Barbecue Sauce": {"price": 2.99, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058863'}, 
    "Salsa": {"price": 2.49, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058864'}, 
    "Tortilla Chips": {"price": 2.79, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058865'}, 
    "Sour Cream": {"price": 1.99, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058866'}, 
    "Cottage Cheese": {"price": 3.29, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058867'}, 
    "Pudding": {"price": 1.49, "availability": 0.95, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058868'}, 
    "Cereal Bars": {"price": 3.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058869'}, 
    "Oatmeal": {"price": 2.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058870'}, 
    "Frozen Burritos": {"price": 4.49, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058871'}, 
    "Frozen Dinners": {"price": 3.99, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058872'}, 
    "Sausages": {"price": 5.49, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058873'}, 
    "Muffins": {"price": 2.79, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058874'}, 
    "Bagels": {"price": 2.49, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058875'}, 
    "Donuts": {"price": 1.99, "availability": 0.95, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058876'}, 
    "Canned Fruit": {"price": 2.29, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058877'}, 
    "Fruit Cups": {"price": 2.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058878'}, 
    "Almond Milk": {"price": 3.49, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058879'}, 
    "Coconut Water": {"price": 2.79, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058880'}, 
    "Trail Mix": {"price": 4.9, "availability": 0.1, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058881'}, 
    "Soy Sauce": {"price": 2.29, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058882'}, 
    "Lemon Cake": {"price": 3.9, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058883'}, 
}

om_sales_doc_item_categories = {
    'CAT01': {
        'PSTYV': 'CAT01',
        'VTEXT': 'Category - 01'
    }
}

om_sales_doc_rejection_reasons = {
    'R1': {
        'ABGRU': 'R1',
        'BEZEI': 'Invalid Sales Document'
    }
}
