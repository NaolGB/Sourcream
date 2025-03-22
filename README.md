# SAP Dataset Generator

A comprehensive tool for generating realistic SAP ERP data simulations for enterprise process analysis and testing.

## Overview

SAP Dataset Generator creates synthetic but realistic SAP data that mimics common enterprise processes. The generated datasets can be used for process mining, analytics testing, dashboard development, or machine learning model training without exposing sensitive production data.

## Key Features

- Simulates complete end-to-end business processes:
  - **Procure-to-Pay**: From purchase requisition to vendor payment
  - **Order-to-Cash**: From sales order to customer payment
- Creates interconnected SAP tables with realistic relationships
- Generates master data (materials, customers, vendors, etc.)
- Produces transaction data (orders, deliveries, invoices, etc.)
- Simulates common process variations and exceptions
- Configurable process parameters and business rules

## Project Structure

```
SAP-Dataset-Generator/
├── data/                           # Generated output data
│   ├── om/                         # Order Management (O2C) data
│   │   ├── master/                 # O2C master data tables
│   │   ├── sales-document/         # O2C sales document tables
│   │   └── text/                   # O2C text/configuration tables
│   └── p2p/                        # Procure-to-Pay data
│       ├── master/                 # P2P master data tables
│       ├── purchasing/             # P2P purchasing document tables
│       └── text/                   # P2P text/configuration tables
├── helpers/                        # Utility functions
│   ├── create_table_leanx.py       # Table structure definitions
│   └── helpers.py                  # Common helper functions
├── content_generators/             # Data generation modules
│   ├── master_data.py              # Master data generation
│   ├── purchasing_doc_data.py      # P2P document generation
│   ├── sales_doc_data.py           # O2C document generation
│   └── text_data.py                # Configuration data generation
├── process_simulators/             # Process simulation notebooks
│   ├── order-management.ipynb      # O2C process simulation
│   └── procurement.ipynb           # P2P process simulation
└── values/                         # Configuration values
    └── values_default.py           # Default parameter values
```

## Technical Requirements

- Python 3.8+
- Pandas 1.3+
- NumPy 1.20+
- Jupyter Notebook or JupyterLab
- BeautifulSoup4 (for table structure parsing)
- 16GB RAM recommended for large dataset generation

## Installation

1. Clone this repository:
```bash
git clone https://github.com/[yourusername]/SAP-Dataset-Generator.git
cd SAP-Dataset-Generator
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Verify the installation:
```bash
python -c "import pandas, numpy, bs4; print('Installation successful!')"
```

## Usage

### Quick Start

To generate a basic dataset with default parameters:

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Open either process simulator notebook:
   - `process_simulators/order-management.ipynb` for Order-to-Cash data
   - `process_simulators/procurement.ipynb` for Procure-to-Pay data

3. Run all cells in the notebook to generate the corresponding dataset

4. Find the generated data in the `data/` directory

### Generating Procurement Data (P2P)

Run the procurement simulation notebook:
```bash
jupyter notebook process_simulators/procurement.ipynb
```

This will simulate the procurement process and generate related data files in `data/p2p/`. You can adjust the simulation parameters within the notebook:

- Change the number of purchase documents to generate
- Modify transition probabilities between process steps
- Adjust automation rates and error rates
- Configure company codes, plants, and organizational units

### Generating Order Management Data (O2C)

Run the order management simulation notebook:
```bash
jupyter notebook process_simulators/order-management.ipynb
```

This will simulate the order management process and generate related data files in `data/om/`. You can adjust the simulation parameters within the notebook:

- Change the number of sales documents to generate
- Modify transition probabilities between process steps
- Adjust credit risk profiles and delivery performance
- Configure sales organizations and distribution channels

### Customizing Master Data

If you want to generate only master data without process simulation:

```python
from content_generators import master_data
from helpers import create_table_leanx as ctl
import pandas as pd
import os

# Generate master data
materials = master_data.materials()
customers = master_data.customers_and_vendors()

# Save to files
for table_dict in [materials, customers]:
    for k, v in table_dict.items():
        table_name = k.split('_')[0]
        all_cols = pd.DataFrame(columns=[c[0] for c in ctl.fetch_table(table_name)])
        df = pd.concat([all_cols, pd.DataFrame(v.values())])
        
        directory = os.path.dirname(f'data/custom/master/{table_name}.csv')
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        df.to_csv(f'data/custom/master/{table_name}.csv', index=False)
```

## Data Description

The generator creates data for standard SAP tables including:

### Master Data Tables

**Materials**:
- MARA: Material general data
- MARC: Material plant data
- MAKT: Material descriptions
- MBEW: Material valuation
- MARM: Material units of measure

**Business Partners**:
- KNA1: Customer master general data
- KNB1: Customer master company code data
- KNKK: Customer credit management
- LFA1: Vendor master general data
- LFB1: Vendor master company code data

**Company Information**:
- BUKRS: Company codes
- WERKS: Plants
- T001W: Plant information
- T001: Company code information

### Transaction Data Tables

**Sales Documents**:
- VBAK: Sales document headers
- VBAP: Sales document items
- VBEP: Sales document schedule lines
- VBKD: Sales document business data
- VBUK: Sales document status

**Deliveries**:
- LIKP: Delivery headers
- LIPS: Delivery items

**Billing Documents**:
- VBRK: Billing document headers
- VBRP: Billing document items

**Purchase Documents**:
- EKKO: Purchase document headers
- EKPO: Purchase document items
- EBAN: Purchase requisitions
- EKES: Purchase order confirmations
- EKET: Purchase order schedule lines

**Accounting Documents**:
- BKPF: Accounting document headers
- BSEG: Accounting document line items
- RBKP: Vendor invoice headers
- RSEG: Vendor invoice line items

**Material Movements**:
- MSEG: Material movement data
- EKBE: Purchase history

**Change Document Tables**:
- CDHDR: Change document headers
- CDPOS: Change document items

**Configuration Tables**:
- Text and code tables for:
  - Document types
  - Material groups
  - Payment terms
  - Plants
  - Sales organizations
  - Purchasing organizations
  - Status codes

## Data Relationships

The data generated maintains key relationships that are critical for accurate process mining and analysis:

**Document Flow Relationships**:
- Sales order → Delivery → Goods issue → Invoice
- Purchase requisition → Purchase order → Goods receipt → Invoice

**Master Data Relationships**:
- Materials → Plants → Valuation areas
- Customers → Company codes → Credit areas
- Vendors → Company codes → Payment terms

**Change Documents**:
- Each status change or document modification is tracked
- User responsible for each change is recorded
- Timestamps for all process steps are maintained

## Configuration

Process parameters and business rules can be configured in the `values/values_default.py` file. Key configuration areas include:

### Master Data Configuration

```python
# Material Groups
om_material_groups = {
    'direct': {
        'MG01': {
            'name': 'Raw Materials',
            'availability': 0.7,
            'has_contract_probability': 0.8,
            'materials': {
                'Steel Sheet': {'price': 75.0},
                'Aluminum Bar': {'price': 92.0},
                # Add or modify materials
            }
        },
        # Add or modify material groups
    }
}

# Customer Configuration
om_customers = {
    'Customer A': {
        'country': 'DE',
        'region': 'NRW',
        'city': 'Cologne',
        'credit_risk': 0.2,
        'payment_term': 'Z030'
    },
    # Add or modify customers
}
```

### Process Variation Configuration

```python
# Company code characteristics
om_company_codes = {
    'CC01': {
        'BUTXT': 'Company 01',
        'plants': ['PL01', 'PL02'],
        'free_text_pr_probability': 0.05,
        'incorrect_qty_prbobability': 0.15
    },
    # Add or modify company codes
}

# Plant characteristics
om_plants = {
    'PL01': {
        'name': 'Plant 01',
        'country_key': 'DE',
        'country_name': 'Germany',
        'high_value': True,
        'sales_orgs': ['EMEA'],
        'purchasing_orgs': ['GLOBAL']
    },
    # Add or modify plants
}
```

## Common Use Cases

### Process Mining and Analysis
Generate data for training process mining algorithms or testing process analysis tools:
- Process Discovery: Use the generated event logs to discover business process models
- Conformance Checking: Compare process executions against expected process models
- Performance Analysis: Analyze durations between process steps

### ERP Implementation and Testing
- System Configuration Testing: Test SAP customization settings with realistic data
- Integration Testing: Test interfaces between SAP and other systems
- User Acceptance Testing: Provide realistic test data for UAT phases

### Machine Learning and AI
- Predictive Analytics: Train ML models to predict process outcomes or delays
- Anomaly Detection: Train models to identify unusual process patterns
- Process Automation: Develop RPA or AI solutions for process automation

## Troubleshooting

### Common Issues

**Memory Errors**:
- Reduce number of documents generated in the simulation
- Run with higher RAM or on a more powerful machine

**Missing Table Columns**:
- Check if new SAP tables or columns need to be added to `create_table_leanx.py`

**Unrealistic Data Patterns**:
- Adjust transition probabilities in the simulation notebooks
- Modify configuration values in `values_default.py`

### Getting Help

If you encounter any issues or have questions:
- Check existing issues on GitHub
- Create a new issue with detailed information about your problem
- Include error messages and steps to reproduce the issue

## Advanced Usage

### Extending with New Tables

To add support for additional SAP tables:

```python
def fetch_table(table_name):
    # ...existing code...
    
    if table_name == 'YOUR_NEW_TABLE':
        return [
            ('COLUMN1', 'datatype'),
            ('COLUMN2', 'datatype'),
            # Add all needed columns
        ]
```

### Custom Process Simulation

To create a custom process variant:
1. Copy one of the existing simulation notebooks
2. Modify the transition probability matrix to reflect your process
3. Add or remove process steps as needed
4. Adjust parameters to match your business scenario

### Scaling for Big Data Testing

For generating very large datasets:
- Modify the loop counters in the simulation notebooks
- Consider running in batches and appending results
- Use distributed processing for extremely large datasets

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Write or update tests if applicable
5. Run any existing tests to ensure nothing was broken
6. Commit your changes (`git commit -am 'Add your feature'`)
7. Push to the branch (`git push origin feature/your-feature`)
8. Create a new Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write docstrings for all functions and classes
- Add comments for complex logic
- Update the README if adding new features or changing existing ones

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by real-world SAP implementations and process mining challenges
- Thanks to all contributors who have helped improve this tool