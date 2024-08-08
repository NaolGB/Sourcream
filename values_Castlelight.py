mandt = 'CL'
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
            '10': 1,
            '20': 0.2,
            '30': 0.9,
            '40': 0.9,
            '50': 0.9
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
            '20': 0.5,
            '30': 1,
            '40': 1,
            '50': 1
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
            '10': 0.9,
            '20': 0.2,
            '30': 0.8,
            '40': 0.8,
            '50': 0.8
        }
    },
}


om_plants = {
    'PL01': {'country_key': 'ID', 'country_name': 'Indonesia', 'name': 'Jakarta Plant', 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL02': {'country_key': 'QA', 'country_name': 'Qatar', 'name': 'Doha Plant', 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL03': {'country_key': 'AE', 'country_name': 'United Arab Emirates', 'name': 'Dubai Plant', 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL04': {'country_key': 'IN', 'country_name': 'India', 'name': 'Bangalore Plant', 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL05': {'country_key': 'DE', 'country_name': 'Germany', 'name': 'Franfurt Plant', 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL06': {'country_key': 'AU', 'country_name': 'Australia', 'name': 'Australia Plant', 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL07': {'country_key': 'BE', 'country_name': 'Belgium', 'name': 'Belgium Plant', 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL08': {'country_key': 'CA', 'country_name': 'Canada', 'name': 'Canada Plant', 'sales_orgs': ['NAM'], 'high_value': True},
    'PL09': {'country_key': 'US', 'country_name': 'United States', 'name': 'Philadelphia Plant', 'sales_orgs': ['NAM'], 'high_value': True},
    'PL10': {'country_key': 'GB', 'country_name': 'Great Britain', 'name': 'Great Britain Plant', 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL11': {'country_key': 'HK', 'country_name': 'Hong Kong', 'name': 'Hong Kong Plant', 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL12': {'country_key': 'IE', 'country_name': 'Ireland', 'name': 'Ireland Plant', 'sales_orgs': ['EMEA'], 'high_value': False},	
    'PL13': {'country_key': 'MY', 'country_name': 'Malaysia', 'name': 'Kuala Lumpur Plant', 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL14': {'country_key': 'NZ', 'country_name': 'New Zealand', 'name': 'New Zealand Plant', 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL15': {'country_key': 'PH', 'country_name': 'Philippines', 'name': 'Manila Plant', 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL16': {'country_key': 'SG', 'country_name': 'Singapore', 'name': 'Singapore Plant', 'sales_orgs': ['JAPC'], 'high_value': False},	
    'PL17': {'country_key': 'US', 'country_name': 'United States', 'name': 'New York Plant', 'sales_orgs': ['NAM'], 'high_value': True},
    'PL18': {'country_key': 'ZA', 'country_name': 'South Africa', 'name': 'South Africa Plant', 'sales_orgs': ['EMEA'], 'high_value': False},	
}


om_valuation_areas = ['VA01']
om_company_codes = {
    'ID01': {'BUTXT': 'CastleLight ID01', 'plants': ['PL01']},
    'QA01': {'BUTXT': 'CastleLight QA01', 'plants': ['PL02']},
    'AE01': {'BUTXT': 'CastleLight AE01', 'plants': ['PL03']},
    'IN01': {'BUTXT': 'CastleLight IN01', 'plants': ['PL04']},
    'DE01': {'BUTXT': 'CastleLight DE01', 'plants': ['PL05']},
    'AU01': {'BUTXT': 'CastleLight AU01', 'plants': ['PL06']},
    'BE01': {'BUTXT': 'CastleLight BE01', 'plants': ['PL07']},
    'CA01': {'BUTXT': 'CastleLight CA01', 'plants': ['PL08']},
    'US02': {'BUTXT': 'CastleLight US02', 'plants': ['PL09']},
    'GB01': {'BUTXT': 'CastleLight GB01', 'plants': ['PL10']},
    'HK01': {'BUTXT': 'CastleLight HK01', 'plants': ['PL11']},
    'IE01': {'BUTXT': 'CastleLight IE01', 'plants': ['PL12']},
    'MY01': {'BUTXT': 'CastleLight MY01', 'plants': ['PL13']},
    'NZ01': {'BUTXT': 'CastleLight NZ01', 'plants': ['PL14']},
    'PH01': {'BUTXT': 'CastleLight PH01', 'plants': ['PL15']},
    'SG01': {'BUTXT': 'CastleLight SG01', 'plants': ['PL16']},
    'US01': {'BUTXT': 'CastleLight US01', 'plants': ['PL17']},
    'ZA01': {'BUTXT': 'CastleLight ZA01', 'plants': ['PL18']},
}
om_sales_doc_types = {
    'ZOR': 'Standard order',
    #'BV': 'Cash Sale',
    'ZDLR': 'Dealer Sales',
    'ZDIR': 'Direct Sales',
    #'ZDOM': 'Domestic Sales',
    #'SO': 'Rush Order',
    'ZDIS': 'Distributor Sales',
    'ZEXP': 'Export Sales',
    #'ZSCR': 'Scrap Sales',
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
    },
    '02': {
        'LIFSP': '02',
        'VTEXT': 'Customer'
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
    },
    '00': {
        'ABGRU': '00',
        'BEZEI': 'Too expensive'
    },
    '01': {
        'ABGRU': '01',
        'BEZEI': 'Delivery date too late'
    },
    'Z4': {
        'ABGRU': 'Z4',
        'BEZEI': 'Poor quality'
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
    'Infrastructure Hardware': {
        'MATKL001': {
            'name': 'Servers',
            'availability': 0.35,
            'materials': {
                'CPU (Intel Xeon E5)': {'price': 499.00},
                'RAM (32GB DDR4)': {'price': 199.00},
                'Storage Drive (1TB SSD)': {'price': 150.00},
                'Motherboard (ATX)': {'price': 150.00},
                'Network Interface Card (1Gbps)': {'price': 50.00}
            }
        },
        'MATKL002': {
            'name': 'Networking Equipment',
            'availability': 0.75,
            'materials': {
                'Router (Enterprise-grade)': {'price': 699.00},
                'Switch (48-port Gigabit)': {'price': 399.00},
                'Firewall (UTM Appliance)': {'price': 1599.00},
                'Load Balancer (Application Delivery Controller)': {'price': 3999.00},
                'Network Cable Tester': {'price': 99.00}
            }
        },
        'MATKL003': {
            'name': 'Storage Systems',
            'availability': 0.8,
            'materials': {
                'SAN Storage Array (20TB)': {'price': 7999.00},
                'NAS Device (10TB)': {'price': 3459.00},
                'Storage Area Network Switch (Fibre Channel)': {'price': 2799.00},
                'Storage Expansion Shelf': {'price': 1999.00},
                'Solid State Drive (1TB)': {'price': 500.00}
            }
        },
        'MATKL004': {
            'name': 'Power Infrastructure',
            'availability': 0.85,
            'materials': {
                'Uninterruptible Power Supply (10kVA)': {'price': 2699.00},
                'Power Distribution Unit (PDU)': {'price': 500.00},
                'Automatic Transfer Switch (ATS)': {'price': 1999.00},
                'Electrical Panel Upgrade': {'price': 4599.00},
                'Power Monitoring System': {'price': 1299.00}
            }
        },
        'MATKL005': {
            'name': 'Backup Power Generators',
            'availability': 0.55,
            'materials': {
                'Diesel Generator (100kW)': {'price': 19999.00},
                'Natural Gas Generator (50kW)': {'price': 13999.00},
                'Propane Generator (30kW)': {'price': 11999.00},
                'Generator Maintenance Service (per year)': {'price': 4999.00},
                'Emergency Fuel Delivery (per gallon)': {'price': 5.00}
            }
        }
    },
    'Facility Management': {
        'MATKL010': {
            'name': 'Cooling Systems',
            'availability': 0.6,
            'materials': {
                'Chiller Unit (20-ton)': {'price': 17999.00},
                'Air Conditioning Unit (5-ton)': {'price': 4999.00},
                'Cooling Tower (100-ton)': {'price': 24500.00},
                'Thermostat (Digital)': {'price': 100.00},
                'Cooling Fan (High CFM)': {'price': 50.00}
            }
        },
        'MATKL011': {
            'name': 'Environmental Controls',
            'availability': 0.7,
            'materials': {
                'Humidity Sensor': {'price': 159.00},
                'Temperature Probe': {'price': 89.00},
                'Air Quality Monitor': {'price': 150.00},
                'Gas Detection System': {'price': 469.00},
                'Climate Control System': {'price': 999.00}
            }
        },
        'MATKL012': {
            'name': 'Fire Suppression Systems',
            'availability': 0.1,
            'materials': {
                'Fire Alarm Panel': {'price': 1099.00},
                'Fire Extinguisher (CO2)': {'price': 200.00},
                'Smoke Detector': {'price': 50.00},
                'Sprinkler System': {'price': 4999.00},
                'Fireproof Doors': {'price': 899.00}
            }
        },
        'MATKL013': {
            'name': 'Security Systems',
            'availability': 0.2,
            'materials': {
                'Surveillance Camera (1080p)': {'price': 150.00},
                'Access Control System': {'price': 998.00},
                'Biometric Scanner (Fingerprint)': {'price': 500.00},
                'Intrusion Detection System': {'price': 1899.00},
                'Security Guard Services (per hour)': {'price': 50.00}
            }
        },
        'MATKL014': {
            'name': 'Biometric Access Control',
            'availability': 0.65,
            'materials': {
                'Fingerprint Scanner': {'price': 500.00},
                'Retina Scanner': {'price': 950.00},
                'Facial Recognition System': {'price': 1350.00},
                'Palm Vein Scanner': {'price': 1750.00},
                'Voice Recognition System': {'price': 875.00}
            }
        }
    },
    'Operations and Support': {
        'MATKL020': {
            'name': 'Monitoring and Management Tools',
            'availability': 0.67,
            'materials': {
                'Monitoring Software License (per node)': {'price': 100.00},
                'Network Analyzer Tool': {'price': 499.00},
                'Server Management Console': {'price': 1199.00},
                'Backup Software': {'price': 500.00},
                'Ticketing System': {'price': 200.00}
            }
        },
        'MATKL021': {
            'name': 'Cabling Infrastructure',
            'availability': 0.75,
            'materials': {
                'Ethernet Cable (Cat6, per meter)': {'price': 1},
                'Fiber Optic Cable (Single Mode, per meter)': {'price': 5},
                'Cable Management Rack': {'price': 100.00},
                'Patch Panels (48-port)': {'price': 200.00},
                'Cable Ties (Pack of 100)': {'price': 10.00}
            }
        },
        'MATKL022': {
            'name': 'Backup and Disaster Recovery Solutions',
            'availability': 0.88,
            'materials': {
                'Backup Server (RAID Array)': {'price': 1999.00},
                'Offsite Backup Storage (per TB/month)': {'price': 20.00},
                'Disaster Recovery Plan Consultation': {'price': 500.00},
                'Backup Generator (20kW)': {'price': 9999.00},
                'Cloud Backup Service (per GB/month)': {'price': 0.10}
            }
        },
        'MATKL023': {
            'name': 'Automation and Orchestration Tools',
            'availability': 0.87,
            'materials': {
                'Automation Software License (per user)': {'price': 500.00},
                'Configuration Management System': {'price': 650.00},
                'Orchestration Platform': {'price': 1480.00},
                'Scripting Tools': {'price': 99.00},
                'Workflow Automation Solution': {'price': 389.00}
            }
        },
        'MATKL024': {
            'name': 'Configuration Management Systems',
            'availability': 0.72,
            'materials': {
                'Configuration Management Software License (per node)': {'price': 500.00},
                'Automation Script Library': {'price': 899.00},
                'Compliance Management Module': {'price': 797.00},
                'Change Management Workflow': {'price': 1754.00},
                'Configuration Baseline Repository': {'price': 478.00}
            }
        }
    },
    'Hardware Support and Maintenance': {
        'MATKL030': {
            'name': 'Hardware Procurement',
            'availability': 0.90,
            'materials': {
                'Server Rack (42U)': {'price': 1267.00},
                'Network Switch (48-port Gigabit)': {'price': 500.00},
                'Storage Array Enclosure': {'price': 2199.00},
                'Power Distribution Unit (PDU)': {'price': 199.00},
                'Rack Mount Kit': {'price': 50.00}
            }
        },
        'MATKL031': {
            'name': 'Equipment Installation',
            'availability': 0.8,
            'materials': {
                'Installation Service (per hour)': {'price': 100.00},
                'Rack Mounting Service (per unit)': {'price': 20.00},
                'Networking Setup Service': {'price': 500.00},
                'Server Configuration Service': {'price': 200.00},
                'Storage System Integration Service': {'price': 300.00}
            }
        },
        'MATKL032': {
            'name': 'Routine Maintenance',
            'availability': 0.75,
            'materials': {
                'Preventive Maintenance Service (per visit)': {'price': 379.00},
                'Server Cleaning Kit': {'price': 50.00},
                'Network Cable Tester': {'price': 79.00},
                'Storage System Health Check': {'price': 279.00},
                'Power Quality Analysis': {'price': 159.00}
            }
        },
        'MATKL033': {
            'name': 'Hardware Upgrades',
            'availability': 0.75,
            'materials': {
                'RAM Upgrade (per module)': {'price': 50.00},
                'Storage Drive Replacement': {'price': 100.00},
                'Network Interface Card Upgrade': {'price': 200.00},
                'Power Supply Replacement': {'price': 150.00},
                'Motherboard Replacement': {'price': 299.00}
            }
        },
        'MATKL034': {
            'name': 'Equipment Decommissioning Services',
            'availability': 0.79,
            'materials': {
                'Data Sanitization Service (per drive)': {'price': 50.00},
                'Equipment Removal and Disposal Service': {'price': 200.00},
                'Asset Inventory and Documentation': {'price': 99.00},
                'Environmental Recycling Fee (per item)': {'price': 20.00},
                'Certification of Destruction': {'price': 99.00}
            }

        }
    },
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

prompt = {"""
I am writing a dummy data for a sales order. 
The company is a big food and beverages processing and packaging comapny. 
It buys raw materials, processes them into foods, packages them, and sells them. 
It's customers are wholesellers, big companies that further process and sell the products, big supermarkets. 
For each material I have, give me a reasonable theoretical average availabilit for these material groups.

for the following producsts give me a theoretical vailability form 0 to 1. Carbonated, Fruit Juices, 
Energy Drinks, Bottled Water, Coffee & Tea, Snacks & Chips, Canned Foods, Frozen Foods, Baked Goods, 
Breakfast Cereals, Sugar & Sweeteners, Flour & Grains, Dairy Products, Spices & Seasonings, Glass Bottles, 
Plastic Bottles, Aluminum Cans, Paper & Cardboard, Sealing Materials. 
"""
}

prompt = {
"""
How are the following attributes realted to ___ in the Order-to-Cash process?
(sales document type, sales organization, company code, customer, distribution channel, material, plant, material group, ) 

How are the following attributes realted to Touchless Order rate in the Order-to-Cash process?
(sales document type, sales organization, company code, customer, distribution channel) 
"""
}

om_customers = {
    "CloudScape Solutions": {"credit_risk": 0.91, 'payment_term': 'Z030', 'country': 'ID', 'region': 'JAPC', 'city': 'Jakarta', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "NetForge Technologies": {"credit_risk": 0.28, 'payment_term': 'Z030', 'country': 'QA', 'region': 'EMEA', 'city': 'Doha', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "DataNexis Systems": {"credit_risk": 0.35, 'payment_term': 'Z030', 'country': 'AE', 'region': 'EMEA', 'city': 'Dubai', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "OptiCore Data Centers": {"credit_risk": 0.68, 'payment_term': 'Z030', 'country': 'IN', 'region': 'JAPC', 'city': 'Bangalore', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Streamline Hosting Services": {"credit_risk": 0.21, 'payment_term': 'Z030', 'country': 'DE', 'region': 'EMEA', 'city': 'Frankfurt', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "DataWorks Innovations": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'AU', 'region': 'JAPC', 'city': 'Melbourne', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "SecureNet Data Centers": {"credit_risk": 0.29, 'payment_term': 'Z030', 'country': 'BE', 'region': 'EMEA', 'city': 'Brussels', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "NexusPoint Infrastructure": {"credit_risk": 0.21, 'payment_term': 'Z030', 'country': 'CA', 'region': 'NAM', 'city': 'Toronto', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "ByteVault Technologies": {"credit_risk": 0.13, 'payment_term': 'Z030', 'country': 'US', 'region': 'NAM', 'city': 'Philadelphia', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "GridGuardian Hosting": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'London', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "SilverLinx Data Centers": {"credit_risk": 0.35, 'payment_term': 'Z030', 'country': 'Ireland', 'region': 'EMEA', 'city': 'Dublin', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "NovaSphere Solutions": {"credit_risk": 0.54, 'payment_term': 'Z030', 'country': 'Malaysia', 'region': 'JAPC', 'city': 'Kuala Lumpur', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "TechHive Data Services": {"credit_risk": 0.52, 'payment_term': 'Z030', 'country': 'New Zealand', 'region': 'JAPC', 'city': 'Auckland', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "Synapse Secure Hosting": {"credit_risk": 0.91, 'payment_term': 'Z030', 'country': 'Philippines', 'region': 'JAPC', 'city': 'Manila', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "DataHaven Technologies": {"credit_risk": 0.78, 'payment_term': 'Z030', 'country': 'Singapore', 'region': 'JAPC', 'city': 'Singapore', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "InfiniteLoop Data": {"credit_risk": 0.37, 'payment_term': 'Z030', 'country': 'United States', 'region': 'EMEA', 'city': 'New York', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "TitanTech Hosting": {"credit_risk": 0.51, 'payment_term': 'Z030', 'country': 'South Africa', 'region': 'EMEA', 'city': 'Cape Town', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "QuantumCloud Solutions": {"credit_risk": 0.32, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "SkyNet Centers": {"credit_risk": 0.13, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "PeakGuardian Stream": {"credit_risk": 0.21, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "CloudGuard Nets": {"credit_risk": 0.43, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "DataFusion Galore": {"credit_risk": 0.44, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "SecureNex Tech": {"credit_risk": 0.47, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "NexusSphere Networks": {"credit_risk": 0.23, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "DataFortress": {"credit_risk": 0.1, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "SecureGrid Inc.": {"credit_risk": 0.52, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "NovaNex": {"credit_risk": 0.09, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "TitanCloud Nation": {"credit_risk": 0.12, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "ByteSphere Assembly": {"credit_risk": 0.38, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "EonNexSoft": {"credit_risk": 0.35, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'LDN', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1},
    "GridNova Inc.": {"credit_risk": 0.14, 'payment_term': 'Z030', 'country': 'UK', 'region': 'EMEA', 'city': 'Pyke', 'late_delivery_rate': 0.1, 'early_delivery_rate': 0.1}
}



