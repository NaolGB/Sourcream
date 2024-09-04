mandt = 'ME'

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
    'PL01': {'country_key': 'ID', 'country_name': 'Indonesia', 'name': 'Jakarta Plant', 'purchasing_orgs': ['JAPC'], 'high_value': False},	
    'PL02': {'country_key': 'QA', 'country_name': 'Qatar', 'name': 'Doha Plant', 'purchasing_orgs': ['EMEA'], 'high_value': False},	
    'PL03': {'country_key': 'AE', 'country_name': 'United Arab Emirates', 'name': 'Dubai Plant', 'purchasing_orgs': ['EMEA'], 'high_value': False},	
    'PL04': {'country_key': 'IN', 'country_name': 'India', 'name': 'Bangalore Plant', 'purchasing_orgs': ['JAPC'], 'high_value': False},	
    'PL05': {'country_key': 'DE', 'country_name': 'Germany', 'name': 'Franfurt Plant', 'purchasing_orgs': ['EMEA'], 'high_value': False},	
    'PL06': {'country_key': 'AU', 'country_name': 'Australia', 'name': 'Australia Plant', 'purchasing_orgs': ['JAPC'], 'high_value': False},	
    'PL07': {'country_key': 'BE', 'country_name': 'Belgium', 'name': 'Belgium Plant', 'purchasing_orgs': ['EMEA'], 'high_value': False},	
    'PL08': {'country_key': 'CA', 'country_name': 'Canada', 'name': 'Canada Plant', 'purchasing_orgs': ['NAM'], 'high_value': True},
    'PL09': {'country_key': 'US', 'country_name': 'United States', 'name': 'Philadelphia Plant', 'purchasing_orgs': ['NAM'], 'high_value': True},
    'PL10': {'country_key': 'GB', 'country_name': 'Great Britain', 'name': 'Great Britain Plant', 'purchasing_orgs': ['EMEA'], 'high_value': False},	
    'PL11': {'country_key': 'HK', 'country_name': 'Hong Kong', 'name': 'Hong Kong Plant', 'purchasing_orgs': ['JAPC'], 'high_value': False},	
    'PL12': {'country_key': 'IE', 'country_name': 'Ireland', 'name': 'Ireland Plant', 'purchasing_orgs': ['EMEA'], 'high_value': False},	
    'PL13': {'country_key': 'MY', 'country_name': 'Malaysia', 'name': 'Kuala Lumpur Plant', 'purchasing_orgs': ['JAPC'], 'high_value': False},	
    'PL14': {'country_key': 'NZ', 'country_name': 'New Zealand', 'name': 'New Zealand Plant', 'purchasing_orgs': ['JAPC'], 'high_value': False},	
    'PL15': {'country_key': 'PH', 'country_name': 'Philippines', 'name': 'Manila Plant', 'purchasing_orgs': ['JAPC'], 'high_value': False},	
    'PL16': {'country_key': 'SG', 'country_name': 'Singapore', 'name': 'Singapore Plant', 'purchasing_orgs': ['JAPC'], 'high_value': False},	
    'PL17': {'country_key': 'US', 'country_name': 'United States', 'name': 'New York Plant', 'purchasing_orgs': ['NAM'], 'high_value': True},
    'PL18': {'country_key': 'ZA', 'country_name': 'South Africa', 'name': 'South Africa Plant', 'purchasing_orgs': ['EMEA'], 'high_value': False},	
}
om_valuation_areas = ['VA01']
om_company_codes = {
    'ID01': {'BUTXT': 'Meritor ID01', 'plants': ['PL01'], 'free_text_pr_probability': 0.9, 'incorrect_qty_prbobability': 0.6},
    'QA01': {'BUTXT': 'Meritor QA01', 'plants': ['PL02'], 'free_text_pr_probability': 0.9, 'incorrect_qty_prbobability': 0.6},
    'AE01': {'BUTXT': 'Meritor AE01', 'plants': ['PL03'], 'free_text_pr_probability': 0.9, 'incorrect_qty_prbobability': 0.2},
    'IN01': {'BUTXT': 'Meritor IN01', 'plants': ['PL04'], 'free_text_pr_probability': 0.9, 'incorrect_qty_prbobability': 0.4},
    'DE01': {'BUTXT': 'Meritor DE01', 'plants': ['PL05'], 'free_text_pr_probability': 0.9, 'incorrect_qty_prbobability': 0.3},
    'AU01': {'BUTXT': 'Meritor AU01', 'plants': ['PL06'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.6},
    'BE01': {'BUTXT': 'Meritor BE01', 'plants': ['PL07'], 'free_text_pr_probability': 0.1, 'incorrect_qty_prbobability': 0.6},
    'CA01': {'BUTXT': 'Meritor CA01', 'plants': ['PL08'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.1},
    'US02': {'BUTXT': 'Meritor US02', 'plants': ['PL09'], 'free_text_pr_probability': 0.1, 'incorrect_qty_prbobability': 0.3},
    'GB01': {'BUTXT': 'Meritor GB01', 'plants': ['PL10'], 'free_text_pr_probability': 0.1, 'incorrect_qty_prbobability': 0.5},
    'HK01': {'BUTXT': 'Meritor HK01', 'plants': ['PL11'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.6},
    'IE01': {'BUTXT': 'Meritor IE01', 'plants': ['PL12'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.1},
    'MY01': {'BUTXT': 'Meritor MY01', 'plants': ['PL13'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.9},
    'NZ01': {'BUTXT': 'Meritor NZ01', 'plants': ['PL14'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.9},
    'PH01': {'BUTXT': 'Meritor PH01', 'plants': ['PL15'], 'free_text_pr_probability': 0.1, 'incorrect_qty_prbobability': 0.9},
    'SG01': {'BUTXT': 'Meritor SG01', 'plants': ['PL16'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.8},
    'US01': {'BUTXT': 'Meritor US01', 'plants': ['PL17'], 'free_text_pr_probability': 0.2, 'incorrect_qty_prbobability': 0.7},
    'ZA01': {'BUTXT': 'Meritor ZA01', 'plants': ['PL18'], 'free_text_pr_probability': 0.1, 'incorrect_qty_prbobability': 0.9},
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
om_status = {
    'apprive_sales_order': {
        'ISTAT': 'I0002',
        'TXT30': 'Approve'
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
om_delivery_blocks = {
    '01': {
        'LIFSP': '01',
        'VTEXT': 'Standard Delivery Block'
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
        'MBBEZ': 'Automobile'
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
om_material_groups = {
    'Chassis Components': {
        'MATKL001': {
            'name': 'Frame Rails',
            'availability': 0.9,
            'has_contract_probability': 0.7,
            'materials': {
                'Steel Frame Rails (per meter)': {'price': 100.00},
                'Aluminum Frame Rails (per meter)': {'price': 150.00},
                'Carbon Fiber Frame Rails (per meter)': {'price': 500.00},
                'Composite Frame Rails (per meter)': {'price': 200.00},
                'Reinforced Steel Frame Rails (per meter)': {'price': 120.00}
            }
        },
        'MATKL002': {
            'name': 'Crossmembers',
            'availability': 0.9,
            'has_contract_probability': 0.4,
            'materials': {
                'Steel Crossmembers (each)': {'price': 50.00},
                'Aluminum Crossmembers (each)': {'price': 80.00},
                'Composite Crossmembers (each)': {'price': 60.00},
                'Reinforced Steel Crossmembers (each)': {'price': 70.00},
                'Galvanized Steel Crossmembers (each)': {'price': 55.00}
            }
        },
        'MATKL003': {
            'name': 'Suspension',
            'availability': 0.9,
            'has_contract_probability': 0.7,
            'materials': {
                'Leaf Springs (per set)': {'price': 300.00},
                'Air Springs (each)': {'price': 200.00},
                'Shock Absorbers (each)': {'price': 150.00},
                'Coil Springs (per set)': {'price': 250.00},
                'Suspension Bushings (per set)': {'price': 50.00}
            }
        },
        'MATKL004': {
            'name': 'Steering',
            'availability': 0.9,
            'has_contract_probability': 0.5,
            'materials': {
                'Steering Column Assembly (each)': {'price': 200.00},
                'Steering Gear (each)': {'price': 300.00},
                'Tie Rods (per set)': {'price': 100.00},
                'Steering Wheel (each)': {'price': 50.00},
                'Power Steering Pump (each)': {'price': 150.00}
            }
        },
        'MATKL005': {
            'name': 'Brackets and Mounts',
            'availability': 0.9,
            'has_contract_probability': 0.6,
            'materials': {
                'Steel Brackets (each)': {'price': 20.00},
                'Aluminum Brackets (each)': {'price': 30.00},
                'Metal Mounts (each)': {'price': 25.00},
                'Composite Brackets (each)': {'price': 25.00},
                'Reinforced Steel Mounts (each)': {'price': 35.00}
            }
        }
    },
    'Powertrain Components': {
        'MATKL010': {
            'name': 'Engine Assembly',
            'availability': 0.6,
            'has_contract_probability': 0.8,
            'materials': {
                'Engine Block (each)': {'price': 1000.00},
                'Cylinder Heads (each)': {'price': 500.00},
                'Pistons (per set)': {'price': 300.00},
                'Crankshaft (each)': {'price': 700.00},
                'Camshaft (each)': {'price': 400.00}
            }
        },
        'MATKL011': {
            'name': 'Transmission Assembly',
            'availability': 0.6,
            'has_contract_probability': 0.6,
            'materials': {
                'Transmission Housing (each)': {'price': 800.00},
                'Transmission Gears (per set)': {'price': 400.00},
                'Clutch Kit (per set)': {'price': 300.00},
                'Shift Forks (per set)': {'price': 200.00},
                'Bearings (per set)': {'price': 100.00}
            }
        },
        'MATKL012': {
            'name': 'Drivetrain Components',
            'availability': 0.6,
            'has_contract_probability': 0.7,
            'materials': {
                'Driveshaft (each)': {'price': 200.00},
                'Differential (each)': {'price': 500.00},
                'Axles (per set)': {'price': 600.00},
                'Universal Joints (per set)': {'price': 50.00},
                'CV Joints (per set)': {'price': 150.00}
            }
        },
        'MATKL013': {
            'name': 'Exhaust System',
            'availability': 0.6,
            'has_contract_probability': 0.8,
            'materials': {
                'Exhaust Manifold (each)': {'price': 150.00},
                'Catalytic Converter (each)': {'price': 300.00},
                'Muffler (each)': {'price': 200.00},
                'Exhaust Pipes (per meter)': {'price': 50.00},
                'Exhaust Gaskets (per set)': {'price': 20.00}
            }
        },
        'MATKL014': {
            'name': 'Fuel Injection',
            'availability': 0.6,
            'has_contract_probability': 0.8,
            'materials': {
                'Fuel Injectors (each)': {'price': 150.00},
                'Fuel Rail (each)': {'price': 100.00},
                'Throttle Body (each)': {'price': 200.00},
                'Fuel Pressure Regulator (each)': {'price': 50.00},
                'Fuel Pump (each)': {'price': 150.00}
            }
        }
    },
    'Body Components': {
        'MATKL020': {
            'name': 'Cab Structure',
            'availability': 0.2,
            'has_contract_probability': 0.2,
            'materials': {
                'Cab Shell (each)': {'price': 5000.00},
                'Doors (each)': {'price': 1000.00},
                'Windows (each)': {'price': 200.00},
                'Roof Panel (each)': {'price': 300.00},
                'Floor Panel (each)': {'price': 400.00}
            }
        },
        'MATKL021': {
            'name': 'Interior Components',
            'availability': 0.1,
            'has_contract_probability': 0.1,
            'materials': {
                'Seats (each)': {'price': 500.00},
                'Dashboard (each)': {'price': 300.00},
                'Controls (per set)': {'price': 200.00},
                'Carpeting (per square meter)': {'price': 50.00},
                'Trim Panels (per piece)': {'price': 100.00}
            }
        },
        'MATKL022': {
            'name': 'Bed or Cargo Area',
            'availability': 0.1,
            'has_contract_probability': 0.2,
            'materials': {
                'Truck Bed (each)': {'price': 1000.00},
                'Cargo Box (each)': {'price': 800.00},
                'Tailgate (each)': {'price': 200.00},
                'Bed Liner (each)': {'price': 300.00},
                'Tie-Down Hooks (per set)': {'price': 50.00}
            }
        },
        'MATKL023': {
            'name': 'Exterior Panels',
            'availability': 0.1,
            'has_contract_probability': 0.3,
            'materials': {
                'Fenders (each)': {'price': 300.00},
                'Hood (each)': {'price': 400.00},
                'Grille (each)': {'price': 200.00},
                'Side Panels (per set)': {'price': 500.00},
                'Bumpers (each)': {'price': 300.00}
            }
        },
        'MATKL024': {
            'name': 'Lights and Electrical Components',
            'availability': 0.1,
            'has_contract_probability': 0.1,
            'materials': {
                'Headlights (each)': {'price': 100.00},
                'Taillights (each)': {'price': 80.00},
                'Wiring Harness (each)': {'price': 50.00},
                'Turn Signal Indicators (each)': {'price': 30.00},
                'Interior Dome Light (each)': {'price': 20.00}
            }
        }
    },
    'Auxiliary Components': {
        'MATKL030': {
            'name': 'Suspension System',
            'availability': 0.6,
            'has_contract_probability': 0.1,
            'materials': {
                'Control Arms (each)': {'price': 100.00},
                'Sway Bar (each)': {'price': 80.00},
                'Struts (each)': {'price': 150.00},
                'Ball Joints (per set)': {'price': 50.00},
                'Bushings (per set)': {'price': 30.00}
            }
        },
        'MATKL031': {
            'name': 'Cooling System',
            'availability': 0.6,
            'has_contract_probability': 0.6,
            'materials': {
                'Radiator (each)': {'price': 400.00},
                'Cooling Fan (each)': {'price': 150.00},
                'Water Pump (each)': {'price': 100.00},
                'Thermostat (each)': {'price': 50.00},
                'Coolant (per liter)': {'price': 5.00}
            }
        },
        'MATKL032': {
            'name': 'Air Intake System',
            'availability': 0.6,
            'has_contract_probability': 0.7,
            'materials': {
                'Air Filter (each)': {'price': 20.00},
                'Intake Manifold (each)': {'price': 150.00},
                'Turbocharger (each)': {'price': 500.00},
                'Intercooler (each)': {'price': 300.00},
                'Throttle Body (each)': {'price': 100.00}
            }
        },
        'MATKL033': {
            'name': 'Brake System',
            'availability': 0.6,
            'has_contract_probability': 0.8,
            'materials': {
                'Brake Calipers (each)': {'price': 150.00},
                'Brake Pads (per set)': {'price': 50.00},
                'Brake Lines (per meter)': {'price': 20.00},
                'Brake Rotors (each)': {'price': 100.00},
                'Brake Fluid (per liter)': {'price': 10.00}
            }
        },
        'MATKL034': {
            'name': 'Electrical System',
            'availability': 0.6,
            'has_contract_probability': 0.6,
            'materials': {
                'Battery (each)': {'price': 100.00},
                'Alternator (each)': {'price': 200.00},
                'Starter Motor (each)': {'price': 150.00},
                'Ignition Coil (each)': {'price': 50.00},
                'Spark Plugs (per set)': {'price': 20.00}
            }

        }
    },
}
om_customers = {
    "DAF Trucks": {"credit_risk": 0.91, 'payment_term': 'Z030', 'country': 'ID', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "IVECO Trucks": {"credit_risk": 0.28, 'payment_term': 'Z030', 'country': 'QA', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Volvo Trucks": {"credit_risk": 0.85, 'payment_term': 'Z030', 'country': 'AE', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Freightliner Trucks": {"credit_risk": 0.68, 'payment_term': 'Z030', 'country': 'IN', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Kenworth Trucks": {"credit_risk": 0.21, 'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Western Star Trucks": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'AU', 'region': 'AU', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "MAN Truck & Bus": {"credit_risk": 0.29, 'payment_term': 'Z030', 'country': 'BE', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Scania Trucks": {"credit_risk": 0.48, 'payment_term': 'Z030', 'country': 'CA', 'region': 'NAM', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Mercedes-Denz Trucks": {"credit_risk": 0.13, 'payment_term': 'Z030', 'country': 'US', 'region': 'NAM', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "International Trucks": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Mack Trucks": {"credit_risk": 0.35, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Peterbilt Motors Company": {"credit_risk": 0.54, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Hino Trucks": {"credit_risk": 0.52, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Isuzu Commercial Truck of America": {"credit_risk": 0.91, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Mitsubishi Fuso Trucks": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Navistar International Corporation": {"credit_risk": 0.37, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "PACCAR Inc.": {"credit_risk": 0.51, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Penske Truck Leasing": {"credit_risk": 0.67, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Ryder System, Inc.": {"credit_risk": 0.13, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Schneider National, Inc.": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "JB Hunt Transport Inc.": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Werner Enterprises Inc.": {"credit_risk": 0.44, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Swift Transportation Company": {"credit_risk": 0.77, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "CR England, Inc.": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Knight-Swift Holdings Inc.": {"credit_risk": 0.1, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "US Xpress Inc.": {"credit_risk": 0.70, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Old Dominion Freight Inc.": {"credit_risk": 0.09, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "YRC Worldwide Inc.": {"credit_risk": 0.82, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "XPO Logistics Inc.": {"credit_risk": 0.38, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "ABF Freight System, Inc.": {"credit_risk": 0.73, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Greyjoy Motors Inc.": {"credit_risk": 0.63, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'Pyke', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
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
proc_vendors = {
    "TruckTech Supplies": {'payment_term': 'Z030', 'country': 'ID', 'region': 'EMEA', 'city': 'Jakarta', 'payment_term_stsability': 0.9},
    "RoadMaster Parts Co.": {'payment_term': 'Z030', 'country': 'ID', 'region': 'EMEA', 'city': 'Jakarta', 'payment_term_stsability': 0.9},
    "GearHaul Solutions": {'payment_term': 'Z030', 'country': 'QA', 'region': 'EMEA', 'city': 'Doha', 'payment_term_stsability': 0.9},
    "DriveLine Depot": {'payment_term': 'Z030', 'country': 'QA', 'region': 'EMEA', 'city': 'Doha', 'payment_term_stsability': 0.9},
    "AxleCrafters": {'payment_term': 'Z030', 'country': 'AE', 'region': 'EMEA', 'city': 'Dubai', 'payment_term_stsability': 0.9},
    "PowerTruck Components": {'payment_term': 'Z030', 'country': 'AE', 'region': 'EMEA', 'city': 'Dubai', 'payment_term_stsability': 0.9},
    "TrailBlaze Truck Parts": {'payment_term': 'Z030', 'country': 'IN', 'region': 'JAPC', 'city': 'Bangalore', 'payment_term_stsability': 0.9},
    "TurboTrek Automotive": {'payment_term': 'Z030', 'country': 'IN', 'region': 'JAPC', 'city': 'Bangalore', 'payment_term_stsability': 0.9},
    "TransMission Masters": {'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'payment_term_stsability': 0.9},
    "BrakeForce Distribution": {'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'payment_term_stsability': 0.9},
    "ClutchCraft Industries": {'payment_term': 'Z030', 'country': 'AU', 'region': 'JAPC', 'city': 'Sydney', 'payment_term_stsability': 0.9},
    "TruckTread Components": {'payment_term': 'Z030', 'country': 'AU', 'region': 'JAPC', 'city': 'Sydney', 'payment_term_stsability': 0.9},
    "HighwayHero Parts": {'payment_term': 'Z030', 'country': 'BE', 'region': 'EMEA', 'city': 'Belgium', 'payment_term_stsability': 0.9},
    "Diesel Dynamics": {'payment_term': 'Z030', 'country': 'BE', 'region': 'EMEA', 'city': 'Belgium', 'payment_term_stsability': 0.9},
    "BigRig Repairs & Parts": {'payment_term': 'Z030', 'country': 'CA', 'region': 'NAM', 'city': 'Toronto', 'payment_term_stsability': 0.9},
    "TruckSpan Solutions": {'payment_term': 'Z030', 'country': 'CA', 'region': 'NAM', 'city': 'Toronto', 'payment_term_stsability': 0.9},
    "WheelWorks Warehouse": {'payment_term': 'Z030', 'country': 'US', 'region': 'NAM', 'city': 'Philadelphia', 'payment_term_stsability': 0.9},
    "TruckTech Innovations": {'payment_term': 'Z030', 'country': 'US', 'region': 'NAM', 'city': 'Philadelphia', 'payment_term_stsability': 0.9},
    "HitchHub Enterprises": {'payment_term': 'Z030', 'country': 'GB', 'region': 'EMEA', 'city': 'London', 'payment_term_stsability': 0.9},
    "DriveSafe Auto Parts": {'payment_term': 'Z030', 'country': 'GB', 'region': 'EMEA', 'city': 'London', 'payment_term_stsability': 0.9},
    "GearGiant Solutions": {'payment_term': 'Z030', 'country': 'HK', 'region': 'JAPC', 'city': 'Hong Kong', 'payment_term_stsability': 0.9},
    "TruckTrack Technologies": {'payment_term': 'Z030', 'country': 'HK', 'region': 'JAPC', 'city': 'Hong Kong', 'payment_term_stsability': 0.9},
    "AxleXpert Parts Co.": {'payment_term': 'Z030', 'country': 'IE', 'region': 'EMEA', 'city': 'Dublin', 'payment_term_stsability': 0.9},
    "PowerPulse Componentss": {'payment_term': 'Z030', 'country': 'IE', 'region': 'EMEA', 'city': 'Dublin', 'payment_term_stsability': 0.9},
    "TrailBlazer Truck Supplies": {'payment_term': 'Z030', 'country': 'MY', 'region': 'JAPC', 'city': 'Kuala Lumpur', 'payment_term_stsability': 0.9},
    "TurboTrek Auto Parts": {'payment_term': 'Z030', 'country': 'MY', 'region': 'JAPC', 'city': 'Kuala Lumpur', 'payment_term_stsability': 0.9},
    "TransMission Tech": {'payment_term': 'Z030', 'country': 'NZ', 'region': 'JAPC', 'city': 'New Zealand', 'payment_term_stsability': 0.1},
    "BrakeCraft Industries": {'payment_term': 'Z030', 'country': 'NZ', 'region': 'JAPC', 'city': 'New Zealand', 'payment_term_stsability': 0.1},
    "ClutchMaster Components": {'payment_term': 'Z030', 'country': 'PH', 'region': 'JAPC', 'city': 'Manila', 'payment_term_stsability': 0.1},
    "TruckTrek Inc.": {'payment_term': 'Z030', 'country': 'PH', 'region': 'JAPC', 'city': 'Manila', 'payment_term_stsability': 0.1},
    "Basti's Trucking Smarts": {'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'payment_term_stsability': 0.1},
    "Alex Trucking Parts": {'payment_term': 'Z030', 'country': 'Westeros', 'region': 'Iron Islands', 'city': 'Pyke', 'payment_term_stsability': 0.9},
}

shipping_conditions = {
    'SS': 'Standard Shipping',
    'ES': 'Express Shipping'
}
goods_movement_types = { # TODO check codes
    'GoodsIssue': {'code': '601', 'is_reverse': None},
    'ReverseGoodsReceipt': {'code': '102', 'is_reverse': 'X'},
    'ReturnGoodsReceipt': {'code': '651', 'is_reverse': 'X'},
    'ReturnDeliveryToVendor': {'code': '122', 'is_reverse': 'X'},
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
