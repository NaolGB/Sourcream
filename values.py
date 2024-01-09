mandt = 'SC1'
om_sales_orgs = {
    'EMEA': {
        'distribution_channels': {
            '10': 'Direct Sales',
            '20': 'Dealers Sales',
            '30': 'Distributor Sales',
            '40': 'Stock Transfer',
            '50': 'Exports Sales'
        },
        'sales_offices': {
            'UK01': 'London, Holborn',
            'SP01': 'Madrid, Pl. de Manuel Gómez-Moreno',
            'GR01': 'Munich, Theresienstr',
        }
    },
    'NAM': {
        'distribution_channels': {
            '10': ' Direct Sales',
            '20': 'Dealers Sales',
            '30': 'Distributor Sales',
            '40': 'Stock Transfer',
            '50': 'Exports Sales'
        },
        'sales_offices': {
            'US01': 'New York, One World Trade Center',
            'US02': 'Raleigh, 223 S. West',
            'US03': 'San Francisco, 28 2nd',
        }
    },
    'JAPC': {
        'distribution_channels': {
            '10': ' Direct Sales',
            '20': 'Dealers Sales',
            '30': 'Distributor Sales',
            '40': 'Stock Transfer',
            '50': 'Exports Sales'
        },
        'sales_offices': {
            'JP01': 'Tokyo, Marunouchi Kitaguchi',
            'IN01': 'Bengaluru, The Pavilion 62/63',
        }
    },
}
om_plants = {
    'PL01': {'country_key': 'ID', 'country_name': 'Indonesia', 'name': 'Jakarta Plant'},	
    'PL02': {'country_key': 'QA', 'country_name': 'Qatar', 'name': 'Doha Plant'},	
    'PL03': {'country_key': 'AE', 'country_name': 'United Arab Emirates', 'name': 'Dubai Plant'},	
    'PL04': {'country_key': 'IN', 'country_name': 'India', 'name': 'Bangalore Plant'},	
    'PL05': {'country_key': 'DE', 'country_name': 'Germany', 'name': 'Franfurt Plant'},	
    'PL06': {'country_key': 'AU', 'country_name': 'Australia', 'name': 'Australia Plant'},	
    'PL07': {'country_key': 'BE', 'country_name': 'Belgium', 'name': 'Belgium Plant'},	
    'PL08': {'country_key': 'CA', 'country_name': 'Canada', 'name': 'Canada Plant'},	
    'PL09': {'country_key': 'US', 'country_name': 'United States', 'name': 'Philadelphia Plant'},	
    'PL10': {'country_key': 'GB', 'country_name': 'Great Britain', 'name': 'Great Britain Plant'},	
    'PL11': {'country_key': 'HK', 'country_name': 'Hong Kong', 'name': 'Hong Kong Plant'},	
    'PL12': {'country_key': 'IE', 'country_name': 'Ireland', 'name': 'Ireland Plant'},	
    'PL13': {'country_key': 'MY', 'country_name': 'Malaysia', 'name': 'Kuala Lumpur Plant'},	
    'PL14': {'country_key': 'NZ', 'country_name': 'New Zealand', 'name': 'New Zealand Plant'},	
    'PL15': {'country_key': 'PH', 'country_name': 'Philippines', 'name': 'Manila Plant'},	
    'PL16': {'country_key': 'SG', 'country_name': 'Singapore', 'name': 'Singapore Plant'},	
    'PL17': {'country_key': 'US', 'country_name': 'United States', 'name': 'New York Plant'},	
    'PL18': {'country_key': 'ZA', 'country_name': 'South Africa', 'name': 'South Africa Plant'},	
}
om_valuation_areas = ['VA01']
om_company_codes = {
    'ID01': {'BUTXT': 'SourCream ID01', 'plants': ['PL01']},
    'QA01': {'BUTXT': 'SourCream QA01', 'plants': ['PL02']},
    'AE01': {'BUTXT': 'SourCream AE01', 'plants': ['PL03']},
    'IN01': {'BUTXT': 'SourCream IN01', 'plants': ['PL04']},
    'DE01': {'BUTXT': 'SourCream DE01', 'plants': ['PL05']},
    'AU01': {'BUTXT': 'SourCream AU01', 'plants': ['PL06']},
    'BE01': {'BUTXT': 'SourCream BE01', 'plants': ['PL07']},
    'CA01': {'BUTXT': 'SourCream CA01', 'plants': ['PL08']},
    'US02': {'BUTXT': 'SourCream US02', 'plants': ['PL09']},
    'GB01': {'BUTXT': 'SourCream GB01', 'plants': ['PL10']},
    'HK01': {'BUTXT': 'SourCream HK01', 'plants': ['PL11']},
    'IE01': {'BUTXT': 'SourCream IE01', 'plants': ['PL12']},
    'MY01': {'BUTXT': 'SourCream MY01', 'plants': ['PL13']},
    'NZ01': {'BUTXT': 'SourCream NZ01', 'plants': ['PL14']},
    'PH01': {'BUTXT': 'SourCream PH01', 'plants': ['PL15']},
    'SG01': {'BUTXT': 'SourCream SG01', 'plants': ['PL16']},
    'US01': {'BUTXT': 'SourCream US01', 'plants': ['PL17']},
    'ZA01': {'BUTXT': 'SourCream ZA01', 'plants': ['PL18']},
}
om_sales_doc_types = {
    'ZOR': 'Standard order',
    'BV': 'Cash Sale',
    'ZDLR': 'Dealer Sales',
    'ZDIR': 'Direct Sales',
    'ZDOM': 'Domestic Sales',
    'SO': 'Rush Order',
    'ZDIS': 'Distributor Sales',
    'ZEXP': 'Export Sales',
    'ZSCR': 'Scrap Sales',
    'ZREJ': 'Rejected Order ',
}
dd07t_combinations = {
    'VBAK': [
        {'DOMVALUE_L': 'C', 'DOMNAME': 'VBTYP', 'DDTEXT': 'Order'},
        {'DOMVALUE_L': 'I', 'DOMNAME': 'VBTYP', 'DDTEXT': 'Order w/o charge'},
    ],
    'TVAK': [
        {'DOMVALUE_L': 'D', 'DOMNAME': 'KLIMP', 'DDTEXT': 'D' }, # TODO add custom values -- attached to TVAK.KLIMP
    ]
}
goods_movement_types = { # TODO check codes
    'GoodsIssue': {'code': '601', 'is_reverse': None},
    'ReverseGoodsReceipt': {'code': '102', 'is_reverse': 'X'},
    'ReturnGoodsReceipt': {'code': '651', 'is_reverse': 'X'},
    'ReturnDeliveryToVendor': {'code': '122', 'is_reverse': 'X'},
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

shipping_conditions = {
    'SS': 'Standard Shipping',
    'ES': 'Express Shipping'
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
om_routes = {
    'R-1': {
        'ROUTE': 'SEA',
        'TRAZTD': 14
    }
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
        'BEZEI': 'Incorrect Sales Document Entries'
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







om_material_groups = {
    'GRP-1': {
        'MATKL': 'GROUP-013',
        'WGBEZ': 'Group 013'
    }
}

x = {
    "Banana Chips": {'price': 0.075, 'availability': 0., 'type': 'E'},
    "Beef Lasagna Frozen Dinner": {'price': 3.25, 'availability': 0., 'type': 'E'},
    "Beef Stew": {'price': 2.25, 'availability': 0., 'type': 'E'},
    "Berry Blast Smoothie": {'price': 2.25, 'availability': 0., 'type': 'E'},
    "Berry Medley Frozen Fruit": {'price': 0.15, 'availability': 0., 'type': 'E'},
    "Black Bean Salsa": {'price': 0.30, 'availability': 0., 'type': 'E'},
    "Blueberry Greek Yogurt": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Butter Biscuits": {'price': 0.15, 'availability': 0., 'type': 'E'},
    "Cajun Seasoning Blend": {'price': 0.075, 'availability': 0., 'type': 'E'},
    "Cashew Nuts": {'price': 0.15, 'availability': 0., 'type': 'E'},
    "Chia Seeds": {'price': 0.25, 'availability': 0., 'type': 'E'},
    "Chicken Alfredo Instant Noodles": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Chicken Tikka Masala Frozen Dinner": {'price': 3.00, 'availability': 0., 'type': 'E'},
    "Chili Powder": {'price': 0.05, 'availability': 0., 'type': 'E'},
    "Chocolate Chip Granola Bars": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Chocolate Fudge Brownie Ice Cream": {'price': 1.75, 'availability': 0., 'type': 'E'},
    "Chocolate Milk": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Chocolate Protein Bars": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Chunky Tomato Soup": {'price': 1.50, 'availability': 0., 'type': 'E'},
    "Classic Cola": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Classic Margarine Tub": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Classic Marinara Sauce": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Classic Potato Chips": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Coconut Oil": {'price': 0.30, 'availability': 0., 'type': 'E'},
    "Cornflakes Cereal": {'price': 0.40, 'availability': 0., 'type': 'E'},
    "Cranberry Juice": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Creamy Butter": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Creamy Peanut Butter": {'price': 1.50, 'availability': 0., 'type': 'E'},
    "Creamy Ranch Dressing": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Crispy Apple Chips": {'price': 0.30, 'availability': 0., 'type': 'E'},
    "Crunchy Pretzels": {'price': 0.30, 'availability': 0., 'type': 'E'},
    "Cumin Seasoning Blend": {'price': 0.075, 'availability': 0., 'type': 'E'},
    "Curry Instant Noodles": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Dark Roast Ground Coffee": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Double Chocolate Cookies": {'price': 0.40, 'availability': 0., 'type': 'E'},
    "Dried Blueberries": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Dried Cranberries": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Earl Grey Tea Bags": {'price': 0.10, 'availability': 0., 'type': 'E'},
    "Extra Virgin Olive Oil": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "French Vanilla Ice Cream": {'price': 1.75, 'availability': 0., 'type': 'E'},
    "Frozen Pea Packs": {'price': 0.40, 'availability': 0., 'type': 'E'},
    "Garlic Bread": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Garlic Mayonnaise": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Green Bean Cans": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Green Tea Bags": {'price': 0.10, 'availability': 0., 'type': 'E'},
    "Hearty Beef Chili": {'price': 2.00, 'availability': 0., 'type': 'E'},
    "Honey Mustard Dressing": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Iced Tea Mix": {'price': 0.20, 'availability': 0., 'type': 'E'},
    "Instant Classic Coffee": {'price': 0.20, 'availability': 0., 'type': 'E'},
    "Italian Seasoning Blend": {'price': 0.075, 'availability': 0., 'type': 'E'},
    "Lemonade": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Mango Juice": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Medium Salsa": {'price': 0.30, 'availability': 0., 'type': 'E'},
    "Mint Chocolate Chip Ice Cream": {'price': 1.75, 'availability': 0., 'type': 'E'},
    "Mixed Nuts": {'price': 0.20, 'availability': 0., 'type': 'E'},
    "Mixed Vegetable Frozen Mix": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Multigrain Crackers": {'price': 0.40, 'availability': 0., 'type': 'E'},
    "Oatmeal Cookies": {'price': 0.40, 'availability': 0., 'type': 'E'},
    "Pancake Mix": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Peach Halves in Syrup": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Peanut Protein Bars": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Pepper Jack Cheese": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Pepperoni Frozen Pizza": {'price': 3.50, 'availability': 0., 'type': 'E'},
    "Pitted Black Olives": {'price': 0.30, 'availability': 0., 'type': 'E'},
    "Protein Shakes": {'price': 1.50, 'availability': 0., 'type': 'E'},
    "Pumpkin Seeds": {'price': 0.20, 'availability': 0., 'type': 'E'},
    "Pure Orange Juice": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Refresh Bottled Water": {'price': 0.20, 'availability': 0., 'type': 'E'},
    "Roasted Almonds": {'price': 0.20, 'availability': 0., 'type': 'E'},
    "Rye Bread": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Salted Butter": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Salted Tortilla Chips": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Sesame Oil": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Sharp Cheddar Cheese Block": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Shortbread Cookies": {'price': 0.40, 'availability': 0., 'type': 'E'},
    "Smoked Gouda Cheese": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Sourdough Bread": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Spaghetti Carbonara Ready Meal": {'price': 3.00, 'availability': 0., 'type': 'E'},
    "Spicy Dill Pickles": {'price': 0.30, 'availability': 0., 'type': 'E'},
    "Stir-Fry Vegetables": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Strawberry Banana Smoothie": {'price': 2.00, 'availability': 0., 'type': 'E'},
    "Strawberry Jam": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Strawberry Yogurt": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Sunflower Seeds": {'price': 0.20, 'availability': 0., 'type': 'E'},
    "Sweet Gherkin Pickles": {'price': 0.30, 'availability': 0., 'type': 'E'},
    "Taco Seasoning Blend": {'price': 0.075, 'availability': 0., 'type': 'E'},
    "Tangy Mayonnaise": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Thunder Energy Drink": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Tropical Fruit Snacks": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Vanilla Bean Yogurt": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Vanilla Ice Cream": {'price': 1.50, 'availability': 0., 'type': 'E'},
    "Vanilla Sports Nutrition Shake": {'price': 2.00, 'availability': 0., 'type': 'E'},
    "Waffle Mix": {'price': 0.50, 'availability': 0., 'type': 'E'},
    "Wheat Crackers": {'price': 0.40, 'availability': 0., 'type': 'E'},
    "Whipped Cream": {'price': 0.75, 'availability': 0., 'type': 'E'},
    "Whole Wheat Bread Loaf": {'price': 1.00, 'availability': 0., 'type': 'E'},
    "Zesty Relish": {'price': 0.50, 'availability': 0., 'type': 'E'},
}







# om_customers = {
#     "Tasty Bites Co.": {"credit_risk": 0.61, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109653'},
#     "Brewmaster's Blend": {"credit_risk": 0.28, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109654'},
#     "Crispy Cravings": {"credit_risk": 0.85, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109655'},
#     "Sips & Savories": {"credit_risk": 0.68, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109656'},
#     "Gourmet Delights Inc.": {"credit_risk": 0.21, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109657'},
#     "Flavor Fusion Foods": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109658'},
#     "Café Elegance": {"credit_risk": 0.29, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109659'},
#     "SodaStreamers": {"credit_risk": 0.48, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109660'},
#     "Sweets & Sips": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109661'},
#     "Gastronomy Galore": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109662'},
#     "Nectar Nook": {"credit_risk": 0.35, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109663'},
#     "Spice & Savor": {"credit_risk": 0.54, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109664'},
#     "Wholesome Treats": {"credit_risk": 0.52, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109665'},
#     "Munchies Magic": {"credit_risk": 0.71, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109666'},
#     "Siplicity Drinks": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109667'},
#     "Foodie Fantasy": {"credit_risk": 0.37, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109668'},
#     "Yummy Morsels": {"credit_risk": 0.51, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109669'},
#     "Baker's Bliss Co.": {"credit_risk": 0.67, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109670'},
#     "ThirstQuencher": {"credit_risk": 0.13, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109671'},
#     "Epicurean Eats": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109672'},
#     "Gusto Gourmets": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109673'},
#     "Beverage Bliss": {"credit_risk": 0.44, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109674'},
#     "Taste Troupe": {"credit_risk": 0.77, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109675'},
#     "ChocoCharm Confections": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109676'},
#     "SavorStreet": {"credit_risk": 0.40, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109677'},
#     "Culinary Crafters": {"credit_risk": 0.70, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109678'},
#     "BrewBurst Beverages": {"credit_risk": 0.09, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109679'},
#     "NoshNation": {"credit_risk": 0.82, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109680'},
#     "Gastronomic Gather": {"credit_risk": 0.38, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109681'},
#     "FreshNosh": {"credit_risk": 0.73, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'id': 'C109682'},
#     "Greyjoy Foods Inc.": {"credit_risk": 0.63, 'payment_term': 'Z030', 'country': 'Westeros', 'region': 'Iron Islands', 'city': 'Pyke', 'id': 'C109683'},
# }



# om_materials = {
#     "Rice": {"price": 2.99, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058832'}, # type(E) = 'in house production
#     "Coffee": {"price": 5.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058833'}, 
#     "Tea": {"price": 3.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058834'}, 
#     "Soda": {"price": 1.49, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058835'}, 
#     "Bottled Water": {"price": 0.99, "availability": 1.0, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058836'}, 
#     "Chips": {"price": 2.79, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058837'}, 
#     "Cookies": {"price": 3.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058838'}, 
#     "Candy": {"price": 1.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058839'}, 
#     "Ice Cream": {"price": 4.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058840'}, 
#     "Frozen Pizza": {"price": 5.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058841'}, 
#     "Canned Soup": {"price": 1.79, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058842'}, 
#     "Honey": {"price": 4.29, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058843'}, 
#     "Peanut Butter": {"price": 3.29, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058844'}, 
#     "Jam": {"price": 2.99, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058845'}, 
#     "Canned Vegetables": {"price": 1.69, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058846'}, 
#     "Frozen Vegetables": {"price": 2.49, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058847'}, 
#     "Olive Oil": {"price": 6.99, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058848'}, 
#     "Vinegar": {"price": 2.19, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058849'}, 
#     "Balsamic Vinegar": {"price": 4.99, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058850'}, 
#     "Wine": {"price": 9.99, "availability": 0.4, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058851'}, 
#     "Beer": {"price": 1.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058852'}, 
#     "Worcestershire Sauce": {"price": 2.79, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058853'}, 
#     "Pickles": {"price": 2.49, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058854'}, 
#     "Olives": {"price": 3.29, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058855'}, 
#     "Canned Tuna": {"price": 1.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058856'}, 
#     "Canned Salmon": {"price": 3.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058857'}, 
#     "Dried Fruits": {"price": 4.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058858'}, 
#     "Nuts": {"price": 5.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058859'}, 
#     "Hamburger Buns": {"price": 2.49, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058860'}, 
#     "Hot Dog Buns": {"price": 2.29, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058861'}, 
#     "Mustard": {"price": 1.79, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058862'}, 
#     "Barbecue Sauce": {"price": 2.99, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058863'}, 
#     "Salsa": {"price": 2.49, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058864'}, 
#     "Tortilla Chips": {"price": 2.79, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058865'}, 
#     "Sour Cream": {"price": 1.99, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058866'}, 
#     "Cottage Cheese": {"price": 3.29, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058867'}, 
#     "Pudding": {"price": 1.49, "availability": 0.95, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058868'}, 
#     "Cereal Bars": {"price": 3.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058869'}, 
#     "Oatmeal": {"price": 2.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058870'}, 
#     "Frozen Burritos": {"price": 4.49, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058871'}, 
#     "Frozen Dinners": {"price": 3.99, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058872'}, 
#     "Sausages": {"price": 5.49, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058873'}, 
#     "Muffins": {"price": 2.79, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058874'}, 
#     "Bagels": {"price": 2.49, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058875'}, 
#     "Donuts": {"price": 1.99, "availability": 0.95, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058876'}, 
#     "Canned Fruit": {"price": 2.29, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058877'}, 
#     "Fruit Cups": {"price": 2.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058878'}, 
#     "Almond Milk": {"price": 3.49, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058879'}, 
#     "Coconut Water": {"price": 2.79, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058880'}, 
#     "Trail Mix": {"price": 4.9, "availability": 0.1, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058881'}, 
#     "Soy Sauce": {"price": 2.29, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058882'}, 
#     "Lemon Cake": {"price": 3.9, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7, 'plants': ['UK-1'], 'id': 'M1058883'}, 
# }


