mandt = 'SC'
credit_control_area = 'SC100'

document_type_texts = { 
    'AA' :	'Asset Posting',
    'AB' :	'Accounting Document',
    'AF' :	'Depreciation Pstngs',
    'AN' :	'Net Asset Posting',
    'CH' :	'Contract Settlement',
    'DA' :	'Customer Document',
    'DG' :	'Customer Credit Memo',
    'DR' :	'Customer Invoice',
    'DZ' :	'Customer Payment',
    'EU' :	'Euro Rounding Diff.',
    'EX' :	'External Number',
    'KA' :	'Vendor Document',
    'KG' :	'Vendor Credit Memo',
    'KN' :	'Net Vendors',
    'KP' :	'Account Maintenance',
    'KR' :	'Vendor Invoice',
    'KZ' :	'Vendor Payment',
    'M1' :	'MCA Journal',
    'M2' :	'FX Swap',
    'M3' :	'P&L Lock',
    'M4' :	'P&L Close',
    'M5' :	'P&L Transformation',
    'M6' :	'FX Valuation',
    'M7' :	'MAR & Restatement',
    'M8' :	'IFX Correction',
    'M9' :	'Reversal',
    'MD' :	'Data Load',
    'ML' :	'ML Settlement',
    'PR' :	'Price Change',
    'RA' :	'Sub.Cred.Memo Stlmt',
    'RB' :	'Reserve for Bad Debt',
    'RE' :	'Invoice - Gross',
    'RN' :	'Invoice - Net',
    'RV' :	'Billing Doc.Transfer',
    'SA' :	'G/L Account Document',
    'SB' :	'G/L Account Posting',
    'SK' :	'Cash Document',
    'SU' :	'Adjustment Document',
    'UE' :	'Data Transfer',
    'WA' :	'Goods Issue',
    'WE' :	'Goods Receipt',
    'WI' :	'Inventory Document',
    'WL' :	'Goods Issue/Delivery',
    'WN' :	'Net Goods Receipt',
    'ZC' :	'FICO -Reconciliation',
    'ZP' :	'Payment Posting',
    'ZR' :	'Bank Reconciliation',
    'ZS' :	'Payment by Check',
    'ZV' :	'Payment Clearing',
}

release_indicators = {
    '1': {
        'FRGKZ': '1',
        'FKZTX': 'Request for quotation'
    },
    'B': {
        'FRGKZ': 'B',
        'FKZTX': 'Fixed RFQ/purchase order'
    },
    '4': {
        'FRGKZ': '4',
        'FKZTX': 'RFQ/PO no changes'
    },
    '2': {
        'FRGKZ': '2',
        'FKZTX': 'RFQ/purchase order'
    },
    'A': {
        'FRGKZ': 'A',
        'FKZTX': 'Fixed RFQ'
    },
    '3': {
        'FRGKZ': '3',
        'FKZTX': 'RFQ/PO no change of date'
    },
    'X': {
        'FRGKZ': 'X',
        'FKZTX': 'Blocked'
    },
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

shipping_conditions = {
    'SS': 'Standard Shipping',
    'ES': 'Express Shipping'
}

proc_doc_types = {
    'A': 'Request for quotation',
    'B': 'Purchase requisition',
    'F': 'Purchase order',
    'I': 'Info record',
    'K': 'Contract',
    'L': 'Scheduling agreement',
    'Q': 'Service entry sheet',
    'W': 'Source list',
}

proc_purchasing_orgs = {
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
            '10': 'Direct Sales',
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
            '10': 'Direct Sales',
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

om_material_groups = {
    'Beverages': {
        'MATKL000': {
            'name': 'Carbonated Drinks',
            'availability': 0.9,
            'has_contract_probability': 0.79,
            'materials': {
                'Coca Fizz 500ml': {'price': 0.50},
                'Soda Stream 1L': {'price': 0.80},
                'Bubbly Blast 750ml': {'price': 0.70},
                'Fizz Pop 330ml': {'price': 0.40},
                'Aero Sip 250ml': {'price': 0.30}
            }
        },
        'MATKL001': {
            'name': 'Fruit Juices',
            'availability': 0.9,
            'has_contract_probability': 0.86,
            'materials': {
                'Apple Blend 1L': {'price': 0.60},
                'Berry Burst 500ml': {'price': 0.45},
                'Citrus Splash 750ml': {'price': 0.55},
                'Mango Mist 330ml': {'price': 0.35},
                'Tropical Twist 250ml': {'price': 0.25}
            }
        },
        'MATKL002': {
            'name': 'Energy Drinks',
            'availability': 0.9,
            'has_contract_probability': 0.78,
            'materials': {
                'Power Punch 500ml': {'price': 0.70},
                'Charge Up 1L': {'price': 1.00},
                'Vigor Max 750ml': {'price': 0.90},
                'Ener Gize 330ml': {'price': 0.50},
                'Stamina Shot 250ml': {'price': 0.40}
            }
        },
        'MATKL003': {
            'name': 'Bottled Water',
            'availability': 0.9,
            'has_contract_probability': 0.73,
            'materials': {
                'Pure Drop 500ml': {'price': 0.30},
                'Crystal Clear 1L': {'price': 0.50},
                'Aqua Fresh 750ml': {'price': 0.40},
                'Spring Splash 330ml': {'price': 0.25},
                'Hydro Haven 250ml': {'price': 0.20}
            }
        },
        'MATKL004': {
            'name': 'Coffee & Tea',
            'availability': 0.9,
            'has_contract_probability': 0.71,
            'materials': {
                'Java Joy 500ml': {'price': 1.00},
                'Tea Taste 1L': {'price': 0.80},
                'Mocha Magic 750ml': {'price': 0.90},
                'Espresso Express 330ml': {'price': 0.60},
                'Chai Charm 250ml': {'price': 0.50}
            }
        }
    },
    'Packaged Foods': {
        'MATKL010': {
            'name': 'Snacks & Chips',
            'availability': 0.8,
            'has_contract_probability': 0.8,
            'materials': {
                'Chippy Crunch 50g': {'price': 0.50},  # per unit cost in bulk
                'Snack Bite 100g': {'price': 0.80},  # per unit cost in bulk
                'Potato Crisp 75g': {'price': 0.70},  # per unit cost in bulk
                'Tortilla Twist 60g': {'price': 0.60},  # per unit cost in bulk
                'Rice Puff 40g': {'price': 0.40}  # per unit cost in bulk
            }
        },
        'MATKL011': {
            'name': 'Canned Foods',
            'availability': 0.6,
            'has_contract_probability': 0.81,
            'materials': {
                'Bean Delight 400g': {'price': 1.00},  # per unit cost in bulk
                'Tomato Sauce 250ml': {'price': 0.70},  # per unit cost in bulk
                'Peach Halves 500ml': {'price': 1.20},  # per unit cost in bulk
                'Tuna Chunks 200g': {'price': 2.50},  # per unit cost in bulk
                'Chicken Soup 350ml': {'price': 0.90}  # per unit cost in bulk
            }
        },
        'MATKL012': {
            'name': 'Frozen Foods',
            'availability': 0.6,
            'has_contract_probability': 0.85,
            'materials': {
                'Pizza Slice 200g': {'price': 1.20},  # per unit cost in bulk
                'Frozen Veggies 500g': {'price': 1.50},  # per unit cost in bulk
                'Chicken Nuggets 400g': {'price': 2.00},  # per unit cost in bulk
                'Fish Fillet 300g': {'price': 3.50},  # per unit cost in bulk
                'Ice CreamBar 100ml': {'price': 0.90}  # per unit cost in bulk
            }
        },
        'MATKL013': {
            'name': 'Baked Goods',
            'availability': 0.6,
            'has_contract_probability': 0.87,
            'materials': {
                'Cocoa Muffin 150g': {'price': 0.80},  # per unit cost in bulk
                'Whole Wheat Bread 500g': {'price': 1.50},  # per unit cost in bulk
                'Croissant 100g': {'price': 0.70},  # per unit cost in bulk
                'Bagel 80g': {'price': 0.60},  # per unit cost in bulk
                'Doughnut Ring 120g': {'price': 0.85}  # per unit cost in bulk
            }
        },
        'MATKL014': {
            'name': 'Breakfast Cereals',
            'availability': 0.6,
            'has_contract_probability': 0.89,
            'materials': {
                'Oat Flakes 250g': {'price': 1.50},  # per unit cost in bulk
                'Corn Flakes 300g': {'price': 1.20},  # per unit cost in bulk
                'Rice Crunch 400g': {'price': 1.80},  # per unit cost in bulk
                'Wheat Biscuit 350g': {'price': 1.60},  # per unit cost in bulk
                'Granola Mix 200g': {'price': 2.00}  # per unit cost in bulk
            }
        }
    },
    'Raw Ingredients': {
        'MATKL020': {
            'name': 'Sugar & Sweeteners',
            'availability': 0.2,
            'has_contract_probability': 0.47,
            'materials': {
                'White Granular Sugar 1kg': {'price': 1.00},  # Wholesalers might pay around $1.00 for a 1kg pack of white granular sugar.
                'Liquid Glucose 5L': {'price': 10.00},  # For 5 liters of liquid glucose, the wholesale price might be approximately $10.00.
                'Brown Sugar 500g': {'price': 1.25},  # The cost for 500g of brown sugar for wholesalers could be around $1.25.
                'Honey Syrup 750ml': {'price': 5.00},  # For a 750ml bottle of honey syrup, wholesalers might pay around $5.00.
                'Corn Syrup 2L': {'price': 8.00}  # Wholesalers might pay about $8.00 for a 2-liter bottle of corn syrup.
            }
        },
        'MATKL021': {
            'name': 'Flour & Grains',
            'availability': 0.1,
            'has_contract_probability': 0.45,
            'materials': {
                'Wheat Flour 10kg': {'price': 8.00},  # Wholesalers might pay around $8.00 for a 10kg bag of wheat flour.
                'Cornmeal 5kg': {'price': 4.50},  # For 5kg of cornmeal, the wholesale price might be approximately $4.50.
                'Barley 1kg': {'price': 1.50},  # The cost for 1kg of barley for wholesalers could be around $1.50.
                'Rice 20kg': {'price': 15.00},  # For a 20kg bag of rice, wholesalers might pay around $15.00.
                'Oatmeal 2kg': {'price': 3.00}  # Wholesalers might pay about $3.00 for a 2kg bag of oatmeal.
            }
        },
        'MATKL022': {
            'name': 'Dairy Products',
            'availability': 0.1,
            'has_contract_probability': 0.50,
            'materials': {
                'Whole Milk Powder 2kg': {'price': 12.00},  # The price for 2kg of whole milk powder for wholesalers might be around $12.00.
                'Butter 500g': {'price': 4.50},  # Butter's price can fluctuate, but for wholesalers, it might be around $4.50 for 500g.
                'Cheese Block 1kg': {'price': 8.00},  # A 1kg block of cheese might cost wholesalers approximately $8.00.
                'Yogurt 1L': {'price': 2.50},  # For a liter of yogurt, wholesalers might pay around $2.50.
                'Whey Protein 500g': {'price': 15.00}  # Whey protein can be pricier; wholesalers might pay around $15.00 for 500g.
            }
        },
        'MATKL023': {
            'name': 'Spices & Seasonings',
            'availability': 0.1,
            'has_contract_probability': 0.57,
            'materials': {
                'Black Pepper 100g': {'price': 2.50},  # Price per 100g for wholesalers might be around $2.50, but this could vary.
                'Salt 5kg': {'price': 2.00},  # The cost of bulk salt for wholesalers can be quite low, around $2.00 for 5kg.
                'Garlic Powder 500g': {'price': 4.00},  # Garlic powder's price for wholesalers might be around $4.00 for 500g.
                'Cinnamon 200g': {'price': 3.50},  # Cinnamon is a bit pricier; wholesalers might pay around $3.50 for 200g.
                'Paprika 250g': {'price': 2.75}  # Paprika's price for wholesalers might be approximately $2.75 for 250g.
            }
        },
        'MATKL024': {
            'name': 'Oils & Fats',
            'availability': 0.1,
            'has_contract_probability': 0.47,
            'materials': {
                'Vegetable Oil 5L': {'price': 10.00},       # per unit (for 5-liter container)
                'Olive Oil 1L': {'price': 8.00},            # per unit (for 1-liter bottle)
                'Palm Oil 10L': {'price': 15.00},           # per unit (for 10-liter container)
                'Coconut Oil 2L': {'price': 6.00},          # per unit (for 2-liter bottle)
                'Sunflower Oil 5L': {'price': 9.00}         # per unit (for 5-liter container)
            }
        }
    },
    'Packaging Materials': {
        'MATKL030': {
            'name': 'Glass Bottles',
            'availability': 0.6,
            'has_contract_probability': 0.9,
            'materials': {
                'Clear Glass 500ml': {'price': 0.15},      # per unit (for 500ml capacity)
                'Green Glass 750ml': {'price': 0.20},      # per unit (for 750ml capacity)
                'Blue Glass 330ml': {'price': 0.18},       # per unit (for 330ml capacity)
                'Amber Glass 250ml': {'price': 0.14},      # per unit (for 250ml capacity)
                'Flint Glass 1L': {'price': 0.25}          # per unit (for 1-liter capacity)
            }
        },
        'MATKL031': {
            'name': 'Plastic Bottles',
            'availability': 0.6,
            'has_contract_probability': 0.83,
            'materials': {
                'PET Clear 500ml': {'price': 0.08},          # per unit (for 500ml capacity)
                'HDPE White 1L': {'price': 0.10},            # per unit (for 1-liter capacity)
                'LDPE Transparent 750ml': {'price': 0.09},   # per unit (for 750ml capacity)
                'PP Black 330ml': {'price': 0.07},           # per unit (for 330ml capacity)
                'PVC Blue 250ml': {'price': 0.06}            # per unit (for 250ml capacity)
            }
        },
        'MATKL032': {
            'name': 'Aluminum Cans',
            'availability': 0.6,
            'has_contract_probability': 0.83,
            'materials': {
                'Aluminum Silver 330ml': {'price': 0.10},        # per unit (for 330ml capacity)
                'Aluminum Gold 500ml': {'price': 0.12},          # per unit (for 500ml capacity)
                'Aluminum Matte Black 355ml': {'price': 0.11},    # per unit (for 355ml capacity)
                'Aluminum Red 250ml': {'price': 0.09},           # per unit (for 250ml capacity)
                'Aluminum Blue 500ml': {'price': 0.13}           # per unit (for 500ml capacity)
            }
        },
        'MATKL033': {
            'name': 'Paper & Cardboard',
            'availability': 0.6,
            'has_contract_probability': 0.83,
            'materials': {
                'White Cardboard 1L': {'price': 0.15},       # per unit (for 1-liter capacity)
                'Kraft Paper 500ml': {'price': 0.10},        # per unit (for 500ml capacity)
                'Recycled Cardboard 750ml': {'price': 0.13}, # per unit (for 750ml capacity)
                'Paperboard 330ml': {'price': 0.08},         # per unit (for 330ml capacity)
                'Brown Cardstock 250ml': {'price': 0.06}     # per unit (for 250ml capacity)
            }
        },
        'MATKL034': {
            'name': 'Sealing Materials',
            'availability': 0.6,
            'has_contract_probability': 0.9,
            'materials': {
                'Aluminum Foil Rolls': {'price': 0.20},  
                'Polyethylene Seals': {'price': 0.05},   
                'Tamper Evident Bands': {'price': 0.03}, 
                'PVC Shrink Bands': {'price': 0.04},     
                'Laminated Sealing Films': {'price': 0.15}
            }

        }
    },
}

om_users = {
    "Alex Johnson": {'type': 'A', 'nation': 'ID'},
    "Bailey Smith": {'type': 'A', 'nation': 'QA'},
    "Carmen Davis": {'type': 'A', 'nation': 'AE'},
    "Darnell Williams": {'type': 'A', 'nation': 'IN'},
    "Evelyn Brown": {'type': 'A', 'nation': 'DE'},
    "Francis Taylor": {'type': 'A', 'nation': 'AU'},
    "Gabriel Moore": {'type': 'A', 'nation': 'BE'},
    "Harper Clark": {'type': 'A', 'nation': 'CA'},
    "Ibrahim Lewis": {'type': 'A', 'nation': 'US'},
    "Jaden Hall": {'type': 'A', 'nation': 'GB'},
    "Kai Lee": {'type': 'A', 'nation': 'HK'},
    "Logan Mitchell": {'type': 'A', 'nation': 'IE'},
    "Morgan Anderson": {'type': 'A', 'nation': 'MY'},
    "Nathan Harris": {'type': 'A', 'nation': 'NZ'},
    "Olive White": {'type': 'A', 'nation': 'PH'},
    "Peyton Turner": {'type': 'A', 'nation': 'SG'},
    "Quinn Martin": {'type': 'A', 'nation': 'US'},
    "Riley Walker": {'type': 'A', 'nation': 'UK'},
    "Sasha Baker": {'type': 'A', 'nation': 'UK'},
    "Taylor Turner": {'type': 'A', 'nation': 'UK'},
    'Catelyn Stark': {'type': 'A', 'nation': 'WS'},
    "Bilbo Baggins": {'type': 'A', 'nation': 'BE'},
    "BATCH_JOB": {'type': 'B', 'nation': 'UK'},
}

om_sales_doc_rejection_reasons = {
        'Z0': {
        'ABGRU': 'Z0',
        'BEZEI': 'Incorrect Sales Document Entries'
    },
    'Z1': {
        'ABGRU': 'Z1',
        'BEZEI': 'Invalid Sales Order'
    },
    '10': {
        'ABGRU': '10',
        'BEZEI': 'Unreasonable request'
    },
    '11': {
        'ABGRU': '11',
        'BEZEI': 'Cust.to receive replacement'
    },
    '03': {
        'ABGRU': '03',
        'BEZEI': 'Too expensive'
    },
    '01': {
        'ABGRU': '01',
        'BEZEI': 'Delivery date too late'
    },
    '02': {
        'ABGRU': '02',
        'BEZEI': 'Poor quality'
    }
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

om_delivery_blocks = {
    '01': {
        'LIFSP': '01',
        'VTEXT': 'Standard Delivery Block'
    },
    '02': {
        'LIFSP': '02',
        'VTEXT': 'Customer Block'
    }
}

om_billing_blocks = {
    '01': {
        'FAKSP': '01',
        'VTEXT': 'Quality Assurance'
    },
    '02': {
        'FAKSP': '02',
        'VTEXT': 'Customer'
    }
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
}

om_company_codes = {
    'ID01': {'BUTXT': 'HotelChocolat ID01', 'plants': ['PL01'], 'free_text_pr_probability': 0.9, 'incorrect_qty_prbobability': 0.6},
    'QA01': {'BUTXT': 'HotelChocolat QA01', 'plants': ['PL02'], 'free_text_pr_probability': 0.9, 'incorrect_qty_prbobability': 0.6},
    'AE01': {'BUTXT': 'HotelChocolat AE01', 'plants': ['PL03'], 'free_text_pr_probability': 0.9, 'incorrect_qty_prbobability': 0.2},
    'IN01': {'BUTXT': 'HotelChocolat IN01', 'plants': ['PL04'], 'free_text_pr_probability': 0.9, 'incorrect_qty_prbobability': 0.4},
    'DE01': {'BUTXT': 'HotelChocolat DE01', 'plants': ['PL05'], 'free_text_pr_probability': 0.9, 'incorrect_qty_prbobability': 0.3},
    'AU01': {'BUTXT': 'HotelChocolat AU01', 'plants': ['PL06'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.6},
    'BE01': {'BUTXT': 'HotelChocolat BE01', 'plants': ['PL07'], 'free_text_pr_probability': 0.1, 'incorrect_qty_prbobability': 0.6},
    'CA01': {'BUTXT': 'HotelChocolat CA01', 'plants': ['PL08'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.1},
    'US02': {'BUTXT': 'HotelChocolat US02', 'plants': ['PL09'], 'free_text_pr_probability': 0.1, 'incorrect_qty_prbobability': 0.3},
    'GB01': {'BUTXT': 'HotelChocolat GB01', 'plants': ['PL10'], 'free_text_pr_probability': 0.1, 'incorrect_qty_prbobability': 0.5},
    'HK01': {'BUTXT': 'HotelChocolat HK01', 'plants': ['PL11'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.6},
    'IE01': {'BUTXT': 'HotelChocolat IE01', 'plants': ['PL12'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.1},
    'MY01': {'BUTXT': 'HotelChocolat MY01', 'plants': ['PL13'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.9},
    'NZ01': {'BUTXT': 'HotelChocolat NZ01', 'plants': ['PL14'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.9},
    'PH01': {'BUTXT': 'HotelChocolat PH01', 'plants': ['PL15'], 'free_text_pr_probability': 0.1, 'incorrect_qty_prbobability': 0.9},
    'SG01': {'BUTXT': 'HotelChocolat SG01', 'plants': ['PL16'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.8},
    'US01': {'BUTXT': 'HotelChocolat US01', 'plants': ['PL17'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.7},
    'ZA01': {'BUTXT': 'HotelChocolat ZA01', 'plants': ['PL18'], 'free_text_pr_probability': 0.1, 'incorrect_qty_prbobability': 0.9},
}

om_valuation_areas = ['VA01']

proc_material_groups = {
        "Proc Raw Ingredients": {
            "MATKL101": {
                "name": "Sugar & Sweeteners",
                "availability": 0.8,
                "materials": {
                    "White Sugar 1kg": {
                        "price": 1.2
                    },
                    "Brown Sugar 1kg": {
                        "price": 1.5
                    },
                    "Liquid Glucose 5L": {
                        "price": 8.0
                    },
                    "Honey Syrup 750ml": {
                        "price": 6.0
                    },
                    "Corn Syrup 2L": {
                        "price": 5.5
                    }
                }
            },
            "MATKL102": {
                "name": "Dairy Products",
                "availability": 0.6,
                "materials": {
                    "Milk Powder 1kg": {
                        "price": 10.0
                    },
                    "Cream 1L": {
                        "price": 4.0
                    },
                    "Butter 500g": {
                        "price": 3.5
                    },
                    "Yogurt 1L": {
                        "price": 2.5
                    },
                    "Cheese 1kg": {
                        "price": 8.0
                    }
                }
            },
            "MATKL103": {
                "name": "Flavors & Additives",
                "availability": 0.7,
                "materials": {
                    "Vanilla Essence 100ml": {
                        "price": 2.0
                    },
                    "Chocolate Syrup 500ml": {
                        "price": 4.0
                    },
                    "Fruit Flavoring 250ml": {
                        "price": 3.0
                    },
                    "Caramel Color 1L": {
                        "price": 5.0
                    },
                    "Citric Acid 500g": {
                        "price": 3.5
                    }
                }
            }
        },
        "Packaging Materials": {
            "MATKL110": {
                "name": "Glass Bottles",
                "availability": 0.9,
                "materials": {
                    "Clear Glass Bottle 500ml": {
                        "price": 0.15
                    },
                    "Amber Glass Bottle 330ml": {
                        "price": 0.12
                    },
                    "Green Glass Bottle 750ml": {
                        "price": 0.2
                    },
                    "Blue Glass Bottle 1L": {
                        "price": 0.25
                    },
                    "Flint Glass Bottle 250ml": {
                        "price": 0.1
                    }
                }
            },
            "MATKL111": {
                "name": "Plastic Bottles",
                "availability": 0.85,
                "materials": {
                    "PET Bottle 500ml": {
                        "price": 0.08
                    },
                    "HDPE Bottle 1L": {
                        "price": 0.1
                    },
                    "LDPE Bottle 750ml": {
                        "price": 0.09
                    },
                    "PVC Bottle 330ml": {
                        "price": 0.07
                    },
                    "PP Bottle 250ml": {
                        "price": 0.06
                    }
                }
            },
            "MATKL112": {
                "name": "Caps & Closures",
                "availability": 0.75,
                "materials": {
                    "Plastic Caps 500pcs": {
                        "price": 5.0
                    },
                    "Metal Caps 500pcs": {
                        "price": 6.0
                    },
                    "Tamper Evident Seals 100pcs": {
                        "price": 2.5
                    },
                    "Screw Caps 100pcs": {
                        "price": 3.0
                    },
                    "Flip Tops 100pcs": {
                        "price": 4.0
                    }
                }
            }
        },
        "Utilities": {
            "MATKL120": {
                "name": "Cleaning Supplies",
                "availability": 0.6,
                "materials": {
                    "Bottle Brushes": {
                        "price": 1.5
                    },
                    "Sanitizer 5L": {
                        "price": 12.0
                    },
                    "Detergent Powder 1kg": {
                        "price": 3.0
                    },
                    "Glass Cleaner 1L": {
                        "price": 2.5
                    },
                    "Disinfectant 5L": {
                        "price": 10.0
                    }
                }
            },
            "MATKL121": {
                "name": "Machinery Maintenance",
                "availability": 0.7,
                "materials": {
                    "Lubricant Oil 1L": {
                        "price": 8.0
                    },
                    "Conveyor Belts": {
                        "price": 50.0
                    },
                    "Sealing Machine Parts": {
                        "price": 30.0
                    },
                    "Pump Filters": {
                        "price": 15.0
                    },
                    "Cooling Fans": {
                        "price": 20.0
                    }
                }
            },
            "MATKL122": {
                "name": "Safety Equipment",
                "availability": 0.9,
                "materials": {
                    "Safety Gloves 10pairs": {
                        "price": 5.0
                    },
                    "Face Masks 50pcs": {
                        "price": 10.0
                    },
                    "Protective Goggles": {
                        "price": 3.5
                    },
                    "Aprons 5pcs": {
                        "price": 12.0
                    },
                    "Safety Boots": {
                        "price": 25.0
                    }
                }
            }
        }
    }

dd07t_combinations = {
    'VBAK': [
        {'DOMVALUE_L': 'C', 'DOMNAME': 'VBTYP', 'DDTEXT': 'Order'},
        {'DOMVALUE_L': 'I', 'DOMNAME': 'VBTYP', 'DDTEXT': 'Order w/o charge'},
    ],
    'TVAK': [
        {'DOMVALUE_L': 'D', 'DOMNAME': 'KLIMP', 'DDTEXT': 'D'},  # TODO add custom values -- attached to TVAK.KLIMP
    ],
    'TVAK_CUSTOM': [
        {'DOMVALUE_L': 'X', 'DOMNAME': 'KLIMP', 'DDTEXT': 'Custom Value X'},
        {'DOMVALUE_L': 'Y', 'DOMNAME': 'KLIMP', 'DDTEXT': 'Custom Value Y'},
    ]
}

proc_vendors = {
    "Tasty Bites Co.": {'payment_term': 'Z030', 'country': 'ID', 'region': 'EMEA', 'city': 'Jakarta', 'payment_term_stsability': 0.9},
    "Brewmaster's Blend": {'payment_term': 'Z030', 'country': 'QA', 'region': 'EMEA', 'city': 'Doha', 'payment_term_stsability': 0.9},
    "Crispy Cravings": {'payment_term': 'Z030', 'country': 'AE', 'region': 'EMEA', 'city': 'Dubai', 'payment_term_stsability': 0.9},
    "Sips & Savories": {'payment_term': 'Z030', 'country': 'IN', 'region': 'JAPC', 'city': 'Bangalore', 'payment_term_stsability': 0.9},
    "Gourmet Delights Inc.": {'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'payment_term_stsability': 0.9},
    "Flavor Fusion Foods": {'payment_term': 'Z030', 'country': 'AU', 'region': 'JAPC', 'city': 'Sydney', 'payment_term_stsability': 0.9},
    "Café Elegance": {'payment_term': 'Z030', 'country': 'BE', 'region': 'EMEA', 'city': 'Belgium', 'payment_term_stsability': 0.9},
    "SodaStreamers": {'payment_term': 'Z030', 'country': 'CA', 'region': 'NAM', 'city': 'Toronto', 'payment_term_stsability': 0.9},
    "Sweets & Sips": {'payment_term': 'Z030', 'country': 'US', 'region': 'NAM', 'city': 'Philadelphia', 'payment_term_stsability': 0.9},
    "Gastronomy Galore": {'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'payment_term_stsability': 0.9},
    "Nectar Nook": {'payment_term': 'Z030', 'country': 'IE', 'region': 'EMEA', 'city': 'Dublin', 'payment_term_stsability': 0.9},
    "Spice & Savor": {'payment_term': 'Z030', 'country': 'MY', 'region': 'JAPC', 'city': 'Kuala Lumpur', 'payment_term_stsability': 0.9},
    "Wholesome Treats": {'payment_term': 'Z030', 'country': 'NZ', 'region': 'JAPC', 'city': 'New Zealand', 'payment_term_stsability': 0.9},
    "Munchies Magic": {'payment_term': 'Z030', 'country': 'PH', 'region': 'JAPC', 'city': 'Manila', 'payment_term_stsability': 0.1},
    "Siplicity Drinks": {'payment_term': 'Z030', 'country': 'HK', 'region': 'JAPC', 'city': 'Hong Kong', 'payment_term_stsability': 0.9},
    "Foodie Fantasy": {'payment_term': 'Z030', 'country': 'GB', 'region': 'EMEA', 'city': 'London', 'payment_term_stsability': 0.9},
    "Yummy Morsels": {'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'payment_term_stsability': 0.9},
    "Baker's Bliss Co.": {'payment_term': 'Z030', 'country': 'BE', 'region': 'EMEA', 'city': 'Belgium', 'payment_term_stsability': 0.9},
    "Thirst Quencher": {'payment_term': 'Z030', 'country': 'GB', 'region': 'EMEA', 'city': 'London', 'payment_term_stsability': 0.9},
    "Epicurean Eats": {'payment_term': 'Z030', 'country': 'GB', 'region': 'EMEA', 'city': 'London', 'payment_term_stsability': 0.9},
    "Gusto Gourmets": {'payment_term': 'Z030', 'country': 'HK', 'region': 'JAPC', 'city': 'Hong Kong', 'payment_term_stsability': 0.9},
    "Beverage Bliss": {'payment_term': 'Z030', 'country': 'HK', 'region': 'JAPC', 'city': 'Hong Kong', 'payment_term_stsability': 0.9},
    "Taste Troupe": {'payment_term': 'Z030', 'country': 'IE', 'region': 'EMEA', 'city': 'Dublin', 'payment_term_stsability': 0.9},
    "ChocoCharm Confections": {'payment_term': 'Z030', 'country': 'IE', 'region': 'EMEA', 'city': 'Dublin', 'payment_term_stsability': 0.9},
    "SavorStreet": {'payment_term': 'Z030', 'country': 'MY', 'region': 'JAPC', 'city': 'Kuala Lumpur', 'payment_term_stsability': 0.9},
    "Culinary Crafters": {'payment_term': 'Z030', 'country': 'MY', 'region': 'JAPC', 'city': 'Kuala Lumpur', 'payment_term_stsability': 0.9},
    "Brew Burst Beverages": {'payment_term': 'Z030', 'country': 'NZ', 'region': 'JAPC', 'city': 'New Zealand', 'payment_term_stsability': 0.9},
    "Nosh Nation": {'payment_term': 'Z030', 'country': 'NZ', 'region': 'JAPC', 'city': 'New Zealand', 'payment_term_stsability': 0.9},
    "Gastronomic Gather": {'payment_term': 'Z030', 'country': 'PH', 'region': 'JAPC', 'city': 'Manila', 'payment_term_stsability': 0.1},
    "Fresh Nosh": {'payment_term': 'Z030', 'country': 'PH', 'region': 'JAPC', 'city': 'Manila', 'payment_term_stsability': 0.1},
    "Basti's Bakery": {'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'payment_term_stsability': 0.1},
    "Greyjoy Foods Inc.": {'payment_term': 'Z030', 'country': 'Westeros', 'region': 'Iron Islands', 'city': 'Pyke', 'payment_term_stsability': 0.9},
    "Pure Ingredients Co.": {'payment_term': 'Z030', 'country': 'ID', 'region': 'EMEA', 'city': 'Jakarta', 'payment_term_stsability': 0.9},
    "Beverage Base Suppliers": {'payment_term': 'Z030', 'country': 'ID', 'region': 'EMEA', 'city': 'Jakarta', 'payment_term_stsability': 0.9},
    "Liquid Essentials": {'payment_term': 'Z030', 'country': 'QA', 'region': 'EMEA', 'city': 'Doha', 'payment_term_stsability': 0.9},
    "Hydration Hub": {'payment_term': 'Z030', 'country': 'QA', 'region': 'EMEA', 'city': 'Doha', 'payment_term_stsability': 0.9},
    "Arabian Flavors Ltd.": {'payment_term': 'Z030', 'country': 'AE', 'region': 'EMEA', 'city': 'Dubai', 'payment_term_stsability': 0.9},
    "TasteCraft Ingredients": {'payment_term': 'Z030', 'country': 'AE', 'region': 'EMEA', 'city': 'Dubai', 'payment_term_stsability': 0.9},
    "Bangalore Beverage Solutions": {'payment_term': 'Z030', 'country': 'IN', 'region': 'JAPC', 'city': 'Bangalore', 'payment_term_stsability': 0.9},
    "FizzFlow Supplies": {'payment_term': 'Z030', 'country': 'IN', 'region': 'JAPC', 'city': 'Bangalore', 'payment_term_stsability': 0.9},
    "Sweeteners Unlimited": {'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'payment_term_stsability': 0.9},
    "Flavor Fields GmbH": {'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'payment_term_stsability': 0.9},
    "Aussie Essence Supplies": {'payment_term': 'Z030', 'country': 'AU', 'region': 'JAPC', 'city': 'Sydney', 'payment_term_stsability': 0.9},
    "Oceanic Syrups Co.": {'payment_term': 'Z030', 'country': 'AU', 'region': 'JAPC', 'city': 'Sydney', 'payment_term_stsability': 0.9},
    "Belgian Beverage Basics": {'payment_term': 'Z030', 'country': 'BE', 'region': 'EMEA', 'city': 'Belgium', 'payment_term_stsability': 0.9},
    "Raw Refreshments": {'payment_term': 'Z030', 'country': 'BE', 'region': 'EMEA', 'city': 'Belgium', 'payment_term_stsability': 0.9},
    "Maple Syrup Masters": {'payment_term': 'Z030', 'country': 'CA', 'region': 'NAM', 'city': 'Toronto', 'payment_term_stsability': 0.9},
    "Toronto Beverage Ingredients": {'payment_term': 'Z030', 'country': 'CA', 'region': 'NAM', 'city': 'Toronto', 'payment_term_stsability': 0.9},
    "American Beverage Makers": {'payment_term': 'Z030', 'country': 'US', 'region': 'NAM', 'city': 'Philadelphia', 'payment_term_stsability': 0.9},
    "SipStream Supplies": {'payment_term': 'Z030', 'country': 'US', 'region': 'NAM', 'city': 'Philadelphia', 'payment_term_stsability': 0.9},
    "UK Beverage Essentials": {'payment_term': 'Z030', 'country': 'GB', 'region': 'EMEA', 'city': 'London', 'payment_term_stsability': 0.9},
    "London Liquid Logistics": {'payment_term': 'Z030', 'country': 'GB', 'region': 'EMEA', 'city': 'London', 'payment_term_stsability': 0.9},
    "Hong Kong Beverage Supplies": {'payment_term': 'Z030', 'country': 'HK', 'region': 'JAPC', 'city': 'Hong Kong', 'payment_term_stsability': 0.9},
    "Asia Beverage Essentials": {'payment_term': 'Z030', 'country': 'HK', 'region': 'JAPC', 'city': 'Hong Kong', 'payment_term_stsability': 0.9},
    "Emerald Isle Ingredients": {'payment_term': 'Z030', 'country': 'IE', 'region': 'EMEA', 'city': 'Dublin', 'payment_term_stsability': 0.9},
    "Dublin Drink Distributors": {'payment_term': 'Z030', 'country': 'IE', 'region': 'EMEA', 'city': 'Dublin', 'payment_term_stsability': 0.9},
    "Tropical Beverages Co.": {'payment_term': 'Z030', 'country': 'MY', 'region': 'JAPC', 'city': 'Kuala Lumpur', 'payment_term_stsability': 0.9},
    "Kuala Lumpur Flavor Works": {'payment_term': 'Z030', 'country': 'MY', 'region': 'JAPC', 'city': 'Kuala Lumpur', 'payment_term_stsability': 0.9},
    "New Zealand Beverage Co.": {'payment_term': 'Z030', 'country': 'NZ', 'region': 'JAPC', 'city': 'New Zealand', 'payment_term_stsability': 0.9},
    "Kiwi Beverage Essentials": {'payment_term': 'Z030', 'country': 'NZ', 'region': 'JAPC', 'city': 'New Zealand', 'payment_term_stsability': 0.9},
    "Manila Mixer Supplies": {'payment_term': 'Z030', 'country': 'PH', 'region': 'JAPC', 'city': 'Manila', 'payment_term_stsability': 0.1},
    "Philippine Beverage Co.": {'payment_term': 'Z030', 'country': 'PH', 'region': 'JAPC', 'city': 'Manila', 'payment_term_stsability': 0.1},
    "Frankfurt Beverage Traders": {'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'payment_term_stsability': 0.1},
    "Iron Island Refreshments": {'payment_term': 'Z030', 'country': 'Westeros', 'region': 'Iron Islands', 'city': 'Pyke', 'payment_term_stsability': 0.9},
}

om_customers = {
    "Tasty Bites Co.": {"credit_risk": 0.91, 'payment_term': 'Z030', 'country': 'ID', 'region': 'JAPC', 'city': 'Jakarta', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Brewmaster's Blend": {"credit_risk": 0.28, 'payment_term': 'Z030', 'country': 'QA', 'region': 'EMEA', 'city': 'Doha', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Crispy Cravings": {"credit_risk": 0.85, 'payment_term': 'Z030', 'country': 'AE', 'region': 'EMEA', 'city': 'Dubai', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Sips & Savories": {"credit_risk": 0.68, 'payment_term': 'Z030', 'country': 'IN', 'region': 'JAPC', 'city': 'Bangalore', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Gourmet Delights Inc.": {"credit_risk": 0.21, 'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Flavor Fusion Foods": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'AU', 'region': 'JAPC', 'city': 'Melbourne', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Café Elegance": {"credit_risk": 0.29, 'payment_term': 'Z030', 'country': 'BE', 'region': 'EMEA', 'city': 'Brussels', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "SodaStreamers": {"credit_risk": 0.48, 'payment_term': 'Z030', 'country': 'CA', 'region': 'NAM', 'city': 'Toronto', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Sweets & Sips": {"credit_risk": 0.13, 'payment_term': 'Z030', 'country': 'US', 'region': 'NAM', 'city': 'Philadelphia', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Gastronomy Galore": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Nectar Nook": {"credit_risk": 0.35, 'payment_term': 'Z030', 'country': 'IE', 'region': 'EMEA', 'city': 'Dublin', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Spice & Savor": {"credit_risk": 0.54, 'payment_term': 'Z030', 'country': 'MY', 'region': 'JAPC', 'city': 'Kuala Lumpur', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Wholesome Treats": {"credit_risk": 0.52, 'payment_term': 'Z030', 'country': 'NZ', 'region': 'JAPC', 'city': 'Auckland', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Munchies Magic": {"credit_risk": 0.91, 'payment_term': 'Z030', 'country': 'PH', 'region': 'JAPC', 'city': 'Manila', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Siplicity Drinks": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'SG', 'region': 'JAPC', 'city': 'Singapore', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Foodie Fantasy": {"credit_risk": 0.37, 'payment_term': 'Z030', 'country': 'US', 'region': 'NAM', 'city': 'New York', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Yummy Morsels": {"credit_risk": 0.51, 'payment_term': 'Z030', 'country': 'ZA', 'region': 'EMEA', 'city': 'Cape Town', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Baker's Bliss Co.": {"credit_risk": 0.67, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "ThirstQuencher": {"credit_risk": 0.13, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Epicurean Eats": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Gusto Gourmets": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Beverage Bliss": {"credit_risk": 0.44, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Taste Troupe": {"credit_risk": 0.77, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "ChocoCharm Confections": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "SavorStreet": {"credit_risk": 0.1, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Culinary Crafters": {"credit_risk": 0.70, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "BrewBurst Beverages": {"credit_risk": 0.09, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "NoshNation": {"credit_risk": 0.82, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Gastronomic Gather": {"credit_risk": 0.38, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "FreshNosh": {"credit_risk": 0.73, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Greyjoy Foods Inc.": {"credit_risk": 0.63, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'Pyke', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
}

om_plants = {
    'PL01': {'country_key': 'ID', 'country_name': 'Indonesia', 'name': 'Jakarta Plant', 'purchasing_orgs': ['JAPC'], 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL02': {'country_key': 'QA', 'country_name': 'Qatar', 'name': 'Doha Plant', 'purchasing_orgs': ['EMEA'], 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL03': {'country_key': 'AE', 'country_name': 'United Arab Emirates', 'name': 'Dubai Plant', 'purchasing_orgs': ['EMEA'], 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL04': {'country_key': 'IN', 'country_name': 'India', 'name': 'Bangalore Plant', 'purchasing_orgs': ['JAPC'], 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL05': {'country_key': 'DE', 'country_name': 'Germany', 'name': 'Franfurt Plant', 'purchasing_orgs': ['EMEA'], 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL06': {'country_key': 'AU', 'country_name': 'Australia', 'name': 'Australia Plant', 'purchasing_orgs': ['JAPC'], 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL07': {'country_key': 'BE', 'country_name': 'Belgium', 'name': 'Belgium Plant', 'purchasing_orgs': ['EMEA'], 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL08': {'country_key': 'CA', 'country_name': 'Canada', 'name': 'Canada Plant', 'purchasing_orgs': ['NAM'], 'sales_orgs': ['NAM'], 'high_value': True},
    'PL09': {'country_key': 'US', 'country_name': 'United States', 'name': 'Philadelphia Plant', 'purchasing_orgs': ['NAM'], 'sales_orgs': ['NAM'], 'high_value': True},
    'PL10': {'country_key': 'GB', 'country_name': 'Great Britain', 'name': 'Great Britain Plant', 'purchasing_orgs': ['EMEA'], 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL11': {'country_key': 'HK', 'country_name': 'Hong Kong', 'name': 'Hong Kong Plant', 'purchasing_orgs': ['JAPC'], 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL12': {'country_key': 'IE', 'country_name': 'Ireland', 'name': 'Ireland Plant', 'purchasing_orgs': ['EMEA'], 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL13': {'country_key': 'MY', 'country_name': 'Malaysia', 'name': 'Kuala Lumpur Plant', 'purchasing_orgs': ['JAPC'], 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL14': {'country_key': 'NZ', 'country_name': 'New Zealand', 'name': 'New Zealand Plant', 'purchasing_orgs': ['JAPC'], 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL15': {'country_key': 'PH', 'country_name': 'Philippines', 'name': 'Manila Plant', 'purchasing_orgs': ['JAPC'], 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL16': {'country_key': 'SG', 'country_name': 'Singapore', 'name': 'Singapore Plant', 'purchasing_orgs': ['JAPC'], 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL17': {'country_key': 'US', 'country_name': 'United States', 'name': 'New York Plant', 'purchasing_orgs': ['NAM'], 'sales_orgs': ['NAM'], 'high_value': True},
    'PL18': {'country_key': 'ZA', 'country_name': 'South Africa', 'name': 'South Africa Plant', 'purchasing_orgs': ['EMEA'], 'sales_orgs': ['EMEA'], 'high_value': False},	
}

om_sales_orgs = {
    'EMEA': {
        'distribution_channels': {
            '10': 'Direct Sales',
            '20': 'Dealers Sales',
            '30': 'Distributor Sales',
            '40': 'Standard order',
            '50': 'Exports Sales'
        },
        'sales_offices': {
            'UK01': 'London, Holborn',
            'SP01': 'Madrid, Pl. de Manuel Gómez-Moreno',
            'GR01': 'Munich, Theresienstr',
        },
        'Automation_rate': {
            '10': 0.8,
            '20': 0.6,
            '30': 0.7,
            '40': 0.5,
            '50': 0.4
        }
    },
    'NAM': {
        'distribution_channels': {
            '10': 'Direct Sales',
            '20': 'Dealers Sales',
            '30': 'Distributor Sales',
            '40': 'Standard order',
            '50': 'Exports Sales'
        },
        'sales_offices': {
            'US01': 'New York, One World Trade Center',
            'US02': 'Raleigh, 223 S. West',
            'US03': 'San Francisco, 28 2nd',
        },
        'Automation_rate': {
            '10': 1,
            '20': 0.8,
            '30': 0.9,
            '40': 0.7,
            '50': 0.6
        }
    },
    'JAPC': {
        'distribution_channels': {
            '10': 'Direct Sales',
            '20': 'Dealers Sales',
            '30': 'Distributor Sales',
            '40': 'Standard order',
            '50': 'Exports Sales'
        },
        'sales_offices': {
            'JP01': 'Tokyo, Marunouchi Kitaguchi',
            'IN01': 'Bengaluru, The Pavilion 62/63',
        },
        'Automation_rate': {
            '10': 0.6,
            '20': 0.4,
            '30': 0.5,
            '40': 0.3,
            '50': 0.25
        }
    },
}
