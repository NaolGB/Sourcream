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

om_zterms = [
    '01',
    '02',
    '03',
    '04',
    '05',
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

om_customers = {
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


om_users = {
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

om_materials = {
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