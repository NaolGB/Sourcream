mandt = 'SC1'


om_sales_order_doc_types = ['C', 'I'] # Order, Order w/o charge

om_shipping_conditions = [
    '01',
    '02',
    '03',
    '04',
    '05',
]

om_distribution_channels = [
    '01',
    '02',
    '03',
    '04',
    '05',
]

om_inco1_terms = [
    '01',
    '02',
    '03',
    '04',
    '05',
]

om_inco2_terms = [
    'A',
    'B',
    'C',
    'D',
    'E',
]


om_sales_orgs = {
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

om_credit_control_areas = [
    '01',
    '02',
    '03',
    '04',
    '05',
]

om_plants = {
    "UK-1": {'country_key': 'UK', 'country_name': 'United Kingdom', 'plant_number': '0001'}
}

om_customers = {
    "Tasty Bites Co.": {"credit_risk": 0.61, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Brewmaster's Blend": {"credit_risk": 0.28, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Crispy Cravings": {"credit_risk": 0.85, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Sips & Savories": {"credit_risk": 0.68, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Gourmet Delights Inc.": {"credit_risk": 0.21, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Flavor Fusion Foods": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Café Elegance": {"credit_risk": 0.29, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "FreshNosh": {"credit_risk": 0.73, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "SodaStreamers": {"credit_risk": 0.48, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Sweets & Sips": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Gastronomy Galore": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Nectar Nook": {"credit_risk": 0.35, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Spice & Savor": {"credit_risk": 0.54, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Wholesome Treats": {"credit_risk": 0.52, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Munchies Magic": {"credit_risk": 0.71, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Siplicity Drinks": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Foodie Fantasy": {"credit_risk": 0.37, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Yummy Morsels": {"credit_risk": 0.51, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Baker's Bliss Co.": {"credit_risk": 0.67, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "ThirstQuencher": {"credit_risk": 0.13, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Epicurean Eats": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Gusto Gourmets": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Beverage Bliss": {"credit_risk": 0.44, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Taste Troupe": {"credit_risk": 0.77, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "ChocoCharm Confections": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "SavorStreet": {"credit_risk": 0.40, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Culinary Crafters": {"credit_risk": 0.70, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "BrewBurst Beverages": {"credit_risk": 0.09, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "NoshNation": {"credit_risk": 0.82, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Gastronomic Gather": {"credit_risk": 0.38, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'company_code': '0001'},
    "Greyjoy Foods Inc.": {"credit_risk": 0.63, 'payment_term': 'Z030', 'country': 'Westeros', 'region': 'Iron Islands', 'city': 'Pyke', 'company_code': '0001'},
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
    'Catelyn Stark': {'type': 'A', 'nation': 'Winter Fell'},
    "BATCH_JOB": {'type': 'B', 'nation': 'UK'},
}

om_materials = {
    "Rice": {"price": 2.99, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Coffee": {"price": 5.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Tea": {"price": 3.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Soda": {"price": 1.49, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Bottled Water": {"price": 0.99, "availability": 1.0, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Chips": {"price": 2.79, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Cookies": {"price": 3.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Candy": {"price": 1.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Ice Cream": {"price": 4.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Frozen Pizza": {"price": 5.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Canned Soup": {"price": 1.79, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Honey": {"price": 4.29, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Peanut Butter": {"price": 3.29, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Jam": {"price": 2.99, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Canned Vegetables": {"price": 1.69, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Frozen Vegetables": {"price": 2.49, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Olive Oil": {"price": 6.99, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Vinegar": {"price": 2.19, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Balsamic Vinegar": {"price": 4.99, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Wine": {"price": 9.99, "availability": 0.4, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Beer": {"price": 1.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Soy Sauce": {"price": 2.29, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Worcestershire Sauce": {"price": 2.79, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Pickles": {"price": 2.49, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Olives": {"price": 3.29, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Canned Tuna": {"price": 1.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Canned Salmon": {"price": 3.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Dried Fruits": {"price": 4.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Nuts": {"price": 5.99, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Hamburger Buns": {"price": 2.49, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Hot Dog Buns": {"price": 2.29, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Mustard": {"price": 1.79, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Barbecue Sauce": {"price": 2.99, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Salsa": {"price": 2.49, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Tortilla Chips": {"price": 2.79, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Sour Cream": {"price": 1.99, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Cottage Cheese": {"price": 3.29, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Pudding": {"price": 1.49, "availability": 0.95, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Cereal Bars": {"price": 3.49, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Oatmeal": {"price": 2.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Frozen Burritos": {"price": 4.49, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Frozen Dinners": {"price": 3.99, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Sausages": {"price": 5.49, "availability": 0.5, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Muffins": {"price": 2.79, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Bagels": {"price": 2.49, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Donuts": {"price": 1.99, "availability": 0.95, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Canned Fruit": {"price": 2.29, "availability": 0.9, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Fruit Cups": {"price": 2.99, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Almond Milk": {"price": 3.49, "availability": 0.8, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Coconut Water": {"price": 2.79, "availability": 0.7, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Trail Mix": {"price": 4.9, "availability": 0.1, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
    "Lemon Cake": {"price": 3.9, "availability": 0.6, 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7}, # type(E) = 'in house production
}

# procurement
p2p_users = {
    "John Doe": "A",
    "Jane Smith": "A",
    "Robert Johnson": "A",
    "Emily Davis": "A",
    "Michael Brown": "A",
    "Sarah Wilson": "A",
    "William Clark": "A",
    "Jessica Lee": "A",
    "David Miller": "A",
    "Jennifer Taylor": "A",
    "James Anderson": "A",
    "Laura Martinez": "A",
    "Joseph White": "A",
    "Amanda Harris": "A",
    "Daniel Thompson": "A",
    "Rachel Robinson": "A",
    "Christopher Lewis": "A",
    "Mary Garcia": "A",
    "Matthew Allen": "A",
    "Elizabeth Wright": "A",
    "Samwell Tarly": "A",
    "BATCH_JOB": 'B',
}

p2p_users_requesters = {
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

p2p_vendors = {
    "Fresh Farms Inc.": {},
    "Green Harvest Foods": {},
    "Nature's Bounty Co.": {},
    "Golden Grains Ltd.": {},
    "Prime Produce Partners": {},
    "Organic Oasis Foods": {},
    "SunnySide Agro Supplies": {},
    "Purely Organic Co.": {},
    "Farm Fresh Distributors": {},
    "AgriPro Ingredients": {},
    "Natural Nourish Ltd.": {},
    "Harvest Moon Foods": {},
    "EverGreen Suppliers": {},
    "BioBlend Foods": {},
    "Sustainable Sourcing Co.": {},
    "Terra Foods Inc.": {},
    "Vital Veggies Ltd.": {},
    "FreshPicks Distributors": {},
    "Wholesome Harvest Co.": {},
    "NutriField Suppliers": {},
    "EcoEssence Foods": {},
    "GoodEarth Ingredients": {},
    "CropCare Distributors": {},
    "FarmFirst Suppliers": {},
    "GreenLeaf Foods Inc.": {},
    "PureProduce Partners": {},
    "Nature's Best Ingredients": {},
    "Healthful Harvest Co.": {},
    "AgroAlliance Ltd.": {},
    "FreshlyPicked Suppliers": {},
    "GreenGro Distributors": {},
    "NutriNest Foods": {},
    "Vitality Vegetables Inc.": {},
    "Earthy Elements Suppliers": {},
    "TerraTop Ingredients": {},
    "Organix Suppliers": {},
    "NutriGreen Foods": {},
    "Pure Produce Distributors": {},
    "EverFresh Ingredients": {},
    "BioBounty Ltd.": {},
    "Natural Nutrients Co.": {},
    "GreenGuard Distributors": {},
    "FarmFusion Suppliers": {},
    "FreshFields Foods": {},
    "Nature's Nectar Inc.": {},
    "Earth Essence Distributors": {},
    "Harvest Haven Co.": {},
    "Organic Options Ltd.": {},
    "Vital Vines Suppliers": {},
    "PurePath Foods": {}
}

p2p_materials = {
    'Water': {"price": 0.06},  
    'Sugar': {"price": 0.80},  
    'Flour': {"price": 0.35},  
    'Salt': {"price": 0.12},   
    'Oil': {"price": 4.00},    
    'Corn': {"price": 0.22},   
    'Potatoes': {"price": 0.30},  
    'Milk': {"price": 2.50},   
    'Cream': {"price": 3.20},  
    'Eggs': {"price": 2.00},   
    'Tomatoes': {"price": 1.20},  
    'Peanuts': {"price": 1.60},  
    'Grapes': {"price": 2.00},   
    'Barley': {"price": 0.30},   
    'Hops': {"price": 16.00},    
    'Wheat': {"price": 0.50},    
    'Soybeans': {"price": 0.40},  
    'Rice': {"price": 0.60},     
    'Cocoa beans': {"price": 2.10},  
    'Tea leaves': {"price": 7.50},  
    'Coffee beans': {"price": 4.50},  
    'Fish': {"price": 6.00},      
    'Meat': {"price": 7.00},      
    'Fruits': {"price": 1.70},    
    'Vegetables': {"price": 1.20},  
    'Cucumbers': {"price": 0.80},   
    'Olives': {"price": 2.50},     
    'Nuts': {"price": 3.20},       
    'Cornmeal': {"price": 0.52},   
    'Yeast': {"price": 4.30},      
    'Vinegar': {"price": 1.70},    
    'Honey': {"price": 6.00},      
    'Pectin': {"price": 8.00},     
    'Herbs': {"price": 2.50},      
    'Spices': {"price": 4.20},     
    'Cheese': {"price": 10.00},    
    'Butter': {"price": 3.30},     
    'Corn starch': {"price": 0.75},  
    'Potato starch': {"price": 1.10}, 
    'Tamarind': {"price": 2.50},   
    'Anchovies': {"price": 7.00},  
    'Tuna': {"price": 5.20},       
    'Wheat germ': {"price": 1.20}, 
    'Citric acid': {"price": 16.00}, 
    'Balsamic vinegar': {"price": 13.00}, 
    'Alcohol': {"price": 17.00},   
    'Cocoa powder': {"price": 3.40},  
    'Lemon juice': {"price": 2.70},   
    'Lime juice': {"price": 2.70},    
    'Garlic': {"price": 1.50}, 
}

p2p_orgs = {
    'A': {
        'offices': ['01', '02', '03'],
    },
    'B': {
        'offices': ['01', '02', '03'],
    },
    'C': {
        'offices': ['01', '02', '03'],
    },
    'D': {
        'offices': ['01', '02', '03'],
    },
    'E': {
        'offices': ['01', '02', '03'],
    },
}