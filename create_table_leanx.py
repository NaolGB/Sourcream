import requests
from bs4 import BeautifulSoup

# data types description found at https://www.ibm.com/docs/en/iis/11.3?topic=types-sql-syntax-data-values
data_types = {
    'ACCP' : 'TIMESTAMP',
    'CHAR' : 'VARCHAR(254)',
    'CLNT' : 'VARCHAR(20)',
    'CUKY' : 'VARCHAR(20)',
    'CURR' : 'FLOAT',
    'DATS' : 'TIMESTAMP',
    'DEC' : 'FLOAT',
    'FLTP' : 'FLOAT',
    'INT1' : 'INT',
    'INT2' : 'INT',
    'INT4' : 'INT',
    'LANG' : 'VARCHAR(20)',
    'LCHR' : 'VARCHAR(20)',
    'LRAW' : 'VARCHAR(20)',
    'NUMC' : 'FLOAT',
    'QUAN' : 'FLOAT',
    'RAW' : 'VARCHAR(254)',
    'TIMS' : 'TIMESTAMP',
    'UNIT' : 'VARCHAR(20)',
}

# list of required columns 
required_table_columns = {
    'BSEG' : ['MANDT', 'BUKRS', 'AUGBL', 'AUGGJ', 'AUGDT', 'KOART', 'BUZEI', 'GJAHR', 'SHKZG', 'BELNR', 'ZLSCH', 'ZBD1T', 'ZBD2T', 'ZBD3T', 'ZBD1P', 'ZBD2P', 'SGTXT', 'WRBTR', 'WSKTO', 'SKFBT', 'ZTERM', 'ZFBDT', 'LIFNR', 'MATNR', 'BSCHL', 'ZLSPR', 'KUNNR', 'MANSP', 'MANST'],
    'VBAP' : ['POSNR', 'OBJNR', 'VBELN', 'MANDT', 'NETWR', 'WAERK', 'ABGRU', 'FKREL', 'PSTYV', 'BRGEW', 'GEWEI', 'NTGEW', 'VRKME', 'KWMENG', 'KDMAT', 'ERNAM', 'NETPR', 'MATNR', 'WERKS', 'ERDAT', 'ERZET', 'KPEIN', 'ROUTE', 'VGTYP', 'VGPOS', 'VGBEL', 'FAKSP'],
    'VBFA' : ['POSNV', 'VBELV', 'POSNN', 'VBTYP_V', 'VBTYP_N', 'MANDT', 'VBELN' ],
    'LIPS' : ['POSNR', 'VBELN', 'VGPOS', 'VGTYP', 'MANDT', 'VGBEL', 'LFIMG', 'VRKME', 'NTGEW', 'GEWEI', 'VOLUM', 'VOLEH', 'LGORT', 'ERNAM', 'MATNR', 'WERKS', 'ERDAT', 'ERZET' ],
    'VBRP' : ['MANDT', 'VBELN', 'POSNR', 'ERNAM', 'MATNR', 'WERKS', 'ERDAT', 'ERZET', 'MANDT', 'VBELN', 'POSNR', 'ERNAM', 'MATNR', 'WERKS', 'AUPOS', 'ERDAT', 'ERZET', 'AUBEL', 'VGTYP'],
    'VBEP' : ['MANDT', 'ETENR', 'POSNR', 'VBELN', 'BMENG', 'MEINS', 'MBDAT', 'WADAT', 'EDATU', 'LMENG'],
    'EKBE' : ['WRBTR', 'WAERS', 'MENGE', 'BUZEI', 'MANDT', 'BELNR', 'GJAHR', 'VGABE'],
    'EBAN' : ['LOEKZ', 'AFNAM', 'WAERS', 'MENGE', 'MEINS', 'STATU', 'FRGKZ', 'TXZ01', 'MANDT', 'BANFN', 'BNFPO', 'ERNAM', 'LIFNR', 'PREIS', 'KTPNR', 'MATNR', 'WERKS', 'PEINH', 'KONNR', 'BSTYP', 'BADAT', 'ESTKZ'],
    'EKKO' : ['LOEKZ', 'WAERS', 'ZTERM', 'FRGSX', 'ZBD1T', 'ZBD2T', 'ZBD3T', 'ZBD1P', 'ZBD2P', 'BSART', 'BUKRS', 'RESWK', 'FRGGR', 'EKORG', 'FRGKE', 'STATU', 'BSTYP', 'EBELN', 'MANDT', 'LIFNR', 'ERNAM', 'AEDAT', 'FRGZU', 'KONNR', 'KDATE', 'KDATB'],
    'EKPO' : ['LOEKZ', 'NETWR', 'MENGE', 'MEINS', 'TXZ01', 'WEPOS', 'BUKRS', 'BPRME', 'REPOS', 'KONNR', 'KTPNR', 'EBELN', 'EBELP', 'MANDT', 'UEBTO', 'WEBRE', 'NETPR', 'WERKS', 'MATNR', 'DPDAT', 'AFNAM', 'AEDAT', 'PEINH', 'BSTYP', 'KTMNG', 'ZWERT', 'BNFPO', 'BANFN'],
    'NAST' : ['TCODE', 'ERUHR', 'MANDT', 'USNAM', 'ERDAT', 'DATVR', 'UHRVR', 'KSCHL', 'PARVW', 'KAPPL', 'PARNR', 'AENDE', 'OBJKY', 'SPRAS'],
    'MSEG' : ['ERFME', 'MEINS', 'LGORT', 'LBKUM', 'MANDT', 'MBLNR', 'ZEILE', 'USNAM_MKPF', 'MENGE', 'EBELP', 'LFBJA', 'SMBLP', 'LIFNR', 'MATNR', 'WERKS', 'MJAHR', 'CPUDT_MKPF', 'CPUTM_MKPF', 'EBELN', 'LFBNR', 'SJAHR', 'BWART', 'SHKZG', 'SMBLN', 'VBELP_IM', 'KDPOS', 'VBELN_IM', 'KDAUF'],
    'EKBE' : ['WRBTR', 'WAERS', 'MENGE', 'BUZEI', 'MANDT', 'BELNR', 'GJAHR', 'VGABE'],
    'RBKP' : ['GJAHR', 'BELNR', 'MANDT', 'BUKRS', 'ZTERM', 'ZLSPR', 'ZLSCH', 'ZBD1T', 'ZBD2T', 'ZBD3T', 'ZBD1P', 'ZBD2P', 'SGTXT', 'USNAM', 'BLDAT', 'ZFBDT', 'LIFNR', 'CPUDT', 'CPUTM', 'VGART', 'WAERS', 'STJAH', 'STBLG' ],
    'RSEG' : ['MENGE', 'BSTME', 'WRBTR', 'MANDT', 'BELNR', 'BUZEI', 'GJAHR', 'EBELP', 'LFPOS', 'MATNR', 'WERKS', 'BUKRS', 'LIFNR', 'EBELN', 'LFGJA', 'LFBNR'],
    'EKET' : ['WEMNG', 'MENGE', 'MANDT', 'EBELN', 'EBELP', 'ETENR', 'EINDT'],
    'CDHDR' : ['UDATE', 'UTIME', 'USERNAME', 'OBJECTID', 'OBJECTCLAS', 'MANDANT', 'CHANGENR', 'TCODE'],
    'CDPOS' : ['MANDANT', 'TABKEY', 'OBJECTID', 'CHNGIND', 'OBJECTCLAS', 'FNAME', 'CHANGENR', 'TABNAME', 'VALUE_OLD', 'VALUE_NEW'],
    'MARC' : ['AUSDT', 'BESKZ', 'BSTMI', 'DISGR', 'DISMM', 'DISPO', 'DZEIT', 'EISBE', 'LGRAD', 'MANDT', 'MATNR', 'MMSTD', 'NFMAT', 'PLIFZ', 'STRGR', 'WEBAZ', 'WERKS'],
    'LFB1' : ['BUKRS', 'ERDAT', 'ERNAM', 'LIFNR', 'MANDT', 'ZTERM'],
    'LFA1' : ['ERNAM', 'LAND1', 'LIFNR', 'MANDT', 'NAME1', 'ORT01', 'VBUND'],
    'KNB1' : ['MANDT', 'ZTERM', 'BUKRS', 'ERDAT', 'KUNNR', 'ERNAM']
}

def fetch_table(table_name: str):
    # validate
    table_name = table_name.strip()
    table_name = table_name.lower()

    url = f"https://www.leanx.eu/en/sap/table/{table_name}.html"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    # get table by class name, change class name if neccessary
    # built for the class name and html structure on October 5, 2023
    table = soup.find('table', attrs={'class':'table table-condensed table-striped'})
    table_body = table.find('tbody')
    rows = table_body.findAll(lambda tag: tag.name=='tr')

    data = []
    for row in rows:
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text)
        
        # to avoid tables under 'possible value' button
        if len(row_data) >= 6:
            data.append(row_data)

    fileds = []
    for d in data:
        fileds.append([d[0], d[4]])
    
    assert len(fileds) > 0, f'No fields returned for the given table name `{table_name}`. Please check if the table exists on https://www.leanx.eu/en/sap/table/search. If problem persists, please get in touch @n.basaye'
    return fileds

def write_query(table_name: str, fileds: list):
    # validate
    table_name = table_name.strip()
    table_name = table_name.upper()

    query_data_types = ''
    for f in fileds:
        query_data_types += f"{f[0]} {data_types[f[1]]}, \n\t"

    # query_data_types ends with ', \n' so '_CELONIS_CHANGE_DATE TIME' is being added to a new line
    query = f"DROP TABLE IF EXISTS {table_name};\n"
    query += f"CREATE TABLE {table_name} (\n"
    query += f"\t{query_data_types}_CELONIS_CHANGE_DATE TIME\n);"

    with open(f'create_{table_name}.sql', 'w') as f:
        try:
            f.write(query)
            print(f"Script generated successfully. File create_{table_name}.sql created.")
        except:
            print("Failed, please check if the table exists on https://www.leanx.eu/en/sap/table/search. If problem persists, please get in touch @n.basaye")

def clean_columns(columns_df,tablename): 
    # Check if table in dict and remove unnecessary columns from df 
    if tablename in required_table_columns:
        columns_required = required_table_columns[tablename]
        for name in columns_df.items():
            if name[0] not in columns_required:
                columns_df = columns_df.drop(name[0], axis=1)
    return columns_df

def get_query(table_name: str):
    fields = fetch_table(table_name=table_name)
    write_query(table_name=table_name, fileds=fields)

def get_raw_query_as_str(table_name: str):
    fields = fetch_table(table_name=table_name)

    # validate
    table_name = table_name.strip()
    table_name = table_name.upper()

    query_data_types = ''
    for f in fields:
        query_data_types += f'"{f[0]}" {data_types[f[1]]},'

    # query_data_types ends with ', \n' so '_CELONIS_CHANGE_DATE TIME' is being added to a new line
    query = f"DROP TABLE IF EXISTS {table_name};"
    query += f"CREATE TABLE {table_name} ("
    query += f"{query_data_types[:-1]});" # NOTE remove the last comma

    return query