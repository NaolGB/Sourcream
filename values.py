mandt = 'SC1'

sales_order_doc_types = ['C', 'I'] # Order, Order w/o charge

shipping_conditions = [
    '01',
    '02',
    '03',
    '04',
    '05',
]

distribution_channels = [
    '01',
    '02',
    '03',
    '04',
    '05',
]

inco1_terms = [
    '01',
    '02',
    '03',
    '04',
    '05',
]

inco2_terms = [
    'A',
    'B',
    'C',
    'D',
    'E',
]

zterms = [
    '01',
    '02',
    '03',
    '04',
    '05',
]

sales_orgs = {
    'A': {
        'sales_offices': ['01', '02', '03'],
    },
    'B': {
        'sales_offices': ['01', '02', '03'],
    },
    'C': {
        'sales_offices': ['01', '02', '03'],
    },
    'D': {
        'sales_offices': ['01', '02', '03'],
    },
    'E': {
        'sales_offices': ['01', '02', '03'],
    },
}

credit_control_areas = [
    '01',
    '02',
    '03',
    '04',
    '05',
]

customers = {
    "Tasty Bites Co.": {"credit_risk": 0.61},
    "Brewmaster's Blend": {"credit_risk": 0.28},
    "Crispy Cravings": {"credit_risk": 0.85},
    "Sips & Savories": {"credit_risk": 0.68},
    "Gourmet Delights Inc.": {"credit_risk": 0.21},
    "Flavor Fusion Foods": {"credit_risk": 0.43},
    "Café Elegance": {"credit_risk": 0.29},
    "FreshNosh": {"credit_risk": 0.73},
    "SodaStreamers": {"credit_risk": 0.48},
    "Sweets & Sips": {"credit_risk": 0.78},
    "Gastronomy Galore": {"credit_risk": 0.23},
    "Nectar Nook": {"credit_risk": 0.35},
    "Spice & Savor": {"credit_risk": 0.54},
    "Wholesome Treats": {"credit_risk": 0.52},
    "Munchies Magic": {"credit_risk": 0.71},
    "Siplicity Drinks": {"credit_risk": 0.78},
    "Foodie Fantasy": {"credit_risk": 0.37},
    "Yummy Morsels": {"credit_risk": 0.51},
    "Baker's Bliss Co.": {"credit_risk": 0.67},
    "ThirstQuencher": {"credit_risk": 0.13},
    "Epicurean Eats": {"credit_risk": 0.78},
    "Gusto Gourmets": {"credit_risk": 0.43},
    "Beverage Bliss": {"credit_risk": 0.44},
    "Taste Troupe": {"credit_risk": 0.77},
    "ChocoCharm Confections": {"credit_risk": 0.23},
    "SavorStreet": {"credit_risk": 0.40},
    "Culinary Crafters": {"credit_risk": 0.70},
    "BrewBurst Beverages": {"credit_risk": 0.09},
    "NoshNation": {"credit_risk": 0.82},
    "Gastronomic Gather": {"credit_risk": 0.38},
    "Greyjoy Foods Inc.": {"credit_risk": 0.63},
}


users = {
    "Alex Johnson": 'A',
    "Bailey Smith": 'A',
    "Carmen Davis": 'A',
    "Darnell Williams": 'A',
    "Evelyn Brown": 'A',
    "Francis Taylor": 'A',
    "Gabriel Moore": 'A',
    "Harper Clark": 'A',
    "Ibrahim Lewis": 'A',
    "Jaden Hall": 'A',
    "Kai Lee": 'A',
    "Logan Mitchell": 'A',
    "Morgan Anderson": 'A',
    "Nathan Harris": 'A',
    "Olive White": 'A',
    "Peyton Turner": 'A',
    "Quinn Martin": 'A',
    "Riley Walker": 'A',
    "Sasha Baker": 'A',
    "Taylor Turner": 'A',
    'Catelyn Stark': 'A',
    "BATCH_JOB": 'B',
}

materials = {
    "Rice": {"price": 2.99, "availability": 0.8},
    "Coffee": {"price": 5.49, "availability": 0.6},
    "Tea": {"price": 3.99, "availability": 0.7},
    "Soda": {"price": 1.49, "availability": 0.9},
    "Bottled Water": {"price": 0.99, "availability": 1.0},
    "Chips": {"price": 2.79, "availability": 0.8},
    "Cookies": {"price": 3.49, "availability": 0.6},
    "Candy": {"price": 1.99, "availability": 0.7},
    "Ice Cream": {"price": 4.99, "availability": 0.5},
    "Frozen Pizza": {"price": 5.99, "availability": 0.5},
    "Canned Soup": {"price": 1.79, "availability": 0.9},
    "Honey": {"price": 4.29, "availability": 0.8},
    "Peanut Butter": {"price": 3.29, "availability": 0.7},
    "Jam": {"price": 2.99, "availability": 0.8},
    "Canned Vegetables": {"price": 1.69, "availability": 0.9},
    "Frozen Vegetables": {"price": 2.49, "availability": 0.8},
    "Olive Oil": {"price": 6.99, "availability": 0.6},
    "Vinegar": {"price": 2.19, "availability": 0.7},
    "Balsamic Vinegar": {"price": 4.99, "availability": 0.6},
    "Wine": {"price": 9.99, "availability": 0.4},
    "Beer": {"price": 1.99, "availability": 0.7},
    "Soy Sauce": {"price": 2.29, "availability": 0.8},
    "Worcestershire Sauce": {"price": 2.79, "availability": 0.6},
    "Pickles": {"price": 2.49, "availability": 0.8},
    "Olives": {"price": 3.29, "availability": 0.6},
    "Canned Tuna": {"price": 1.99, "availability": 0.7},
    "Canned Salmon": {"price": 3.99, "availability": 0.5},
    "Dried Fruits": {"price": 4.49, "availability": 0.6},
    "Nuts": {"price": 5.99, "availability": 0.5},
    "Hamburger Buns": {"price": 2.49, "availability": 0.9},
    "Hot Dog Buns": {"price": 2.29, "availability": 0.7},
    "Mustard": {"price": 1.79, "availability": 0.9},
    "Barbecue Sauce": {"price": 2.99, "availability": 0.8},
    "Salsa": {"price": 2.49, "availability": 0.7},
    "Tortilla Chips": {"price": 2.79, "availability": 0.8},
    "Sour Cream": {"price": 1.99, "availability": 0.9},
    "Cottage Cheese": {"price": 3.29, "availability": 0.6},
    "Pudding": {"price": 1.49, "availability": 0.95},
    "Cereal Bars": {"price": 3.49, "availability": 0.6},
    "Oatmeal": {"price": 2.99, "availability": 0.7},
    "Frozen Burritos": {"price": 4.49, "availability": 0.5},
    "Frozen Dinners": {"price": 3.99, "availability": 0.6},
    "Sausages": {"price": 5.49, "availability": 0.5},
    "Muffins": {"price": 2.79, "availability": 0.7},
    "Bagels": {"price": 2.49, "availability": 0.9},
    "Donuts": {"price": 1.99, "availability": 0.95},
    "Canned Fruit": {"price": 2.29, "availability": 0.9},
    "Fruit Cups": {"price": 2.99, "availability": 0.7},
    "Almond Milk": {"price": 3.49, "availability": 0.8},
    "Coconut Water": {"price": 2.79, "availability": 0.7},
    "Trail Mix": {"price": 4.9, "availability": 0.1},
    "Lemon Cake": {"price": 3.9, "availability": 0.6},
}