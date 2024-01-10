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
    'Z0': {
        'ABGRU': 'Z0',
        'BEZEI': 'Incorrect Sales Document Entries'
    },
    'Z1': {
        'ABGRU': 'Z1',
        'BEZEI': 'Invalid Sales Order'
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
    'Beverages': {
        'MATKL001': {
            'name': 'Carbonated Drinks',
            'materials': {
                'Coca Fizz 500ml': {},
                'Soda Stream 1L': {},
                'Bubbly Blast 750ml': {},
                'Fizz Pop 330ml': {},
                'Aero Sip 250ml': {}
            }
        },
        'MATKL002': {
            'name': 'Fruit Juices',
            'materials': {
                'Apple Blend 1L': {},
                'Berry Burst 500ml': {},
                'Citrus Splash 750ml': {},
                'Mango Mist 330ml': {},
                'Tropical Twist 250ml': {}
            }
        },
        'MATKL003': {
            'name': 'Energy Drinks',
            'materials': {
                'Power Punch 500ml': {},
                'Charge Up 1L': {},
                'Vigor Max 750ml': {},
                'Ener Gize 330ml': {},
                'Stamina Shot 250ml': {}
            }
        },
        'MATKL004': {
            'name': 'Bottled Water',
            'materials': {
                'Pure Drop 500ml': {},
                'Crystal Clear 1L': {},
                'Aqua Fresh 750ml': {},
                'Spring Splash 330ml': {},
                'Hydro Haven 250ml': {}
            }
        },
        'MATKL005': {
            'name': 'Coffee & Tea',
            'materials': {
                'Java Joy 500ml': {},
                'Tea Taste 1L': {},
                'Mocha Magic 750ml': {},
                'Espresso Express 330ml': {},
                'Chai Charm 250ml': {}
            }
        }
    },
    'Packaged Foods': {
        'MATKL010': {
            'name': 'Snacks & Chips',
            'materials': {
                'Chippy Crunch 50g': {},
                'Snack Bite 100g': {},
                'Potat oCrisp 75g': {},
                'Tortilla Twist 60g': {},
                'Rice Puff 40g': {}
            }
        },
        'MATKL011': {
            'name': 'Canned Foods',
            'materials': {
                'Bean Delight 400g': {},
                'Tomato Sauce 250ml': {},
                'Peach Halves 500ml': {},
                'Tuna Chunks 200g': {},
                'Chicken Soup 350ml': {}
            }
        },
        'MATKL012': {
            'name': 'Frozen Foods',
            'materials': {
                'Pizza Slice 200g': {},
                'Frozen Veggies 500g': {},
                'Chicken Nuggets 400g': {},
                'Fish Fillet 300g': {},
                'Ice CreamBar 100ml': {}
            }
        },
        'MATKL013': {
            'name': 'Baked Goods',
            'materials': {
                'Cocoa Muffin 150g': {},
                'Whole WheatBread 500g': {},
                'Croissant 100g': {},
                'Bagel 80g': {},
                'Doughnut Ring 120g': {}
            }
        },
        'MATKL014': {
            'name': 'Breakfast Cereals',
            'materials': {
                'Oat Flakes 250g': {},
                'Corn Flakes 300g': {},
                'Rice Crunch 400g': {},
                'Wheat Biscuit 350g': {},
                'Granola Mix 200g': {}
            }
        }
    },
    'Raw Ingredients': {
        'MATKL020': {
            'name': 'Sugar & Sweeteners',
            'materials': {
                'White Granular Sugar 1kg': {},
                'Liquid Glucose 5L': {},
                'Brown Sugar 500g': {},
                'Honey Syrup 750ml': {},
                'Corn Syrup 2L': {}
            }
        },
        'MATKL021': {
            'name': 'Flour & Grains',
            'materials': {
                'Wheat Flour 10kg': {},
                'Cornmeal 5kg': {},
                'Barley 1kg': {},
                'Rice 20kg': {},
                'Oatmeal 2kg': {}
            }
        },
        'MATKL022': {
            'name': 'Dairy Products',
            'materials': {
                'Whole Milk Powder 2kg': {},
                'Butter 500g': {},
                'Cheese Block 1kg': {},
                'Yogurt 1L': {},
                'Whey Protein 500g': {}
            }
        },
        'MATKL023': {
            'name': 'Spices & Seasonings',
            'materials': {
                'Black Pepper 100g': {},
                'Salt 5kg': {},
                'Garlic Powder 500g': {},
                'Cinnamon 200g': {},
                'Paprika 250g': {}
            }
        },
        'MATKL024': {
            'name': 'Oils & Fats',
            'materials': {
                'Vegetable Oil 5L': {},
                'Olive Oil 1L': {},
                'Palm Oil 10L': {},
                'Coconut Oil 2L': {},
                'Sunflower Oil 5L': {}
            }
        }
    },









    'Packaging Materials': {
        'groups': {
            'MATKL030': 'Glass Bottles',
            'MATKL031': 'Plastic Bottles',
            'MATKL032': 'Aluminum Cans',
            'MATKL033': 'Paper & Cardboard',
            'MATKL034': 'Sealing Materials'
        },
        'materials': {

        }
    },
    'Equipment & Machinery': {
        'groups': {
            'MATKL040': 'Processing Machines',
            'MATKL041': 'Packaging Machines',
            'MATKL042': 'Refrigeration Equipment',
            'MATKL043': 'Conveyors & Belts',
            'MATKL044': 'Cleaning Equipment'
        },
        'materials': {

        }
    },
    'Services & Miscellaneous': {
        'groups': {
            'MATKL050': 'Maintenance Services',
            'MATKL051': 'Logistics & Transportation',
            'MATKL052': 'Quality Control Services',
            'MATKL053': 'Consulting & Training',
            'MATKL054': 'Miscellaneous Supplies'
        },
        'materials': {

        }
    }
}

prompt = {"""
I am writing a dummy data for a sales order. 
The company is a big food and beverages processing and packaging comapny. 
It buys raw materials, processes them into foods, packages them, and sells them. 
It's customers are wholesellers, big companies that further process and sell the products, big supermarkets. 
For each material group I have, give me 5 product/material names. 
This data is going into SAP MM tables so make it sound corporate/industrial.
Use fairly generic names, do not have brand names that are in the real world. 
Include the specific scale when possible, like this: 'Coca Fizz 500ml'.
Don't forget to use spaces in the material names.
          


for each one use a format like this. 
 'MATKL001': {
     'name': 'Carbonated Drinks',
     'materials': {
        material_name_with_spaces: {}
     }
 }
"""
}


om_materials = {
    "Banana Chips": {'price': 0.075, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Beef Lasagna Frozen Dinner": {'price': 3.25, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Beef Stew": {'price': 2.25, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Berry Blast Smoothie": {'price': 2.25, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Berry Medley Frozen Fruit": {'price': 0.15, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Black Bean Salsa": {'price': 0.30, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Blueberry Greek Yogurt": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Butter Biscuits": {'price': 0.15, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Cajun Seasoning Blend": {'price': 0.075, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Cashew Nuts": {'price': 0.15, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Chia Seeds": {'price': 0.25, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Chicken Alfredo Instant Noodles": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Chicken Tikka Masala Frozen Dinner": {'price': 3.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Chili Powder": {'price': 0.05, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Chocolate Chip Granola Bars": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Chocolate Fudge Brownie Ice Cream": {'price': 1.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Chocolate Milk": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Chocolate Protein Bars": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Chunky Tomato Soup": {'price': 1.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Classic Cola": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Classic Margarine Tub": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Classic Marinara Sauce": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Classic Potato Chips": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Coconut Oil": {'price': 0.30, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Cornflakes Cereal": {'price': 0.40, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Cranberry Juice": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Creamy Butter": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Creamy Peanut Butter": {'price': 1.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Creamy Ranch Dressing": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Crispy Apple Chips": {'price': 0.30, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Crunchy Pretzels": {'price': 0.30, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Cumin Seasoning Blend": {'price': 0.075, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Curry Instant Noodles": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Dark Roast Ground Coffee": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Double Chocolate Cookies": {'price': 0.40, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Dried Blueberries": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Dried Cranberries": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Earl Grey Tea Bags": {'price': 0.10, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Extra Virgin Olive Oil": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "French Vanilla Ice Cream": {'price': 1.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Frozen Pea Packs": {'price': 0.40, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Garlic Bread": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Garlic Mayonnaise": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Green Bean Cans": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Green Tea Bags": {'price': 0.10, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Hearty Beef Chili": {'price': 2.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Honey Mustard Dressing": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Iced Tea Mix": {'price': 0.20, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Instant Classic Coffee": {'price': 0.20, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Italian Seasoning Blend": {'price': 0.075, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Lemonade": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Mango Juice": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Medium Salsa": {'price': 0.30, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Mint Chocolate Chip Ice Cream": {'price': 1.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Mixed Nuts": {'price': 0.20, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Mixed Vegetable Frozen Mix": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Multigrain Crackers": {'price': 0.40, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Oatmeal Cookies": {'price': 0.40, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Pancake Mix": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Peach Halves in Syrup": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Peanut Protein Bars": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Pepper Jack Cheese": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Pepperoni Frozen Pizza": {'price': 3.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Pitted Black Olives": {'price': 0.30, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Protein Shakes": {'price': 1.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Pumpkin Seeds": {'price': 0.20, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Pure Orange Juice": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Refresh Bottled Water": {'price': 0.20, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Roasted Almonds": {'price': 0.20, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Rye Bread": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Salted Butter": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Salted Tortilla Chips": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Sesame Oil": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Sharp Cheddar Cheese Block": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Shortbread Cookies": {'price': 0.40, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Smoked Gouda Cheese": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Sourdough Bread": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Spaghetti Carbonara Ready Meal": {'price': 3.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Spicy Dill Pickles": {'price': 0.30, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Stir-Fry Vegetables": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Strawberry Banana Smoothie": {'price': 2.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Strawberry Jam": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Strawberry Yogurt": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Sunflower Seeds": {'price': 0.20, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Sweet Gherkin Pickles": {'price': 0.30, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Taco Seasoning Blend": {'price': 0.075, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Tangy Mayonnaise": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Thunder Energy Drink": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Tropical Fruit Snacks": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Vanilla Bean Yogurt": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Vanilla Ice Cream": {'price': 1.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Vanilla Sports Nutrition Shake": {'price': 2.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Waffle Mix": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Wheat Crackers": {'price': 0.40, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Whipped Cream": {'price': 0.75, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Whole Wheat Bread Loaf": {'price': 1.00, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
    "Zesty Relish": {'price': 0.50, 'availability': 0., 'type': 'E', 'delivery_takes_days': 7, 'goods_receipt_processing_days': 7},
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



