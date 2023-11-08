import pandas as pd
import create_sap_table.create_table_leanx as sap_table

VBAK = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBAK')])
VBAP = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBAP')])
BSAD = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='BSAD')])
TCURF = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TCURF')])
TCURR = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TCURR')])
VBFA = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBFA')])
CDHDR = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='CDHDR')])
CDPOS = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='CDPOS')])
LIPS = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='LIPS')])
USR02 = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='USR02')])
LIKP = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='LIKP')])
JCDS = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='JCDS')])
TJ02T = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TJ02T')])
TVLST = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVLST')])
TVFST = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVFST')])
TCURX = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TCURX')])
VBEP = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBEP')])
VBUK = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBUK')])
DD07T = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='DD07T')])
MKPF = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='MKPF')])
VBRP = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBRP')])
VBRK = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBRK')])
NAST = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='NAST')])
T685T = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='T685T')])
VTTP = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VTTP')])
BKPF = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='BKPF')])
TVAKT = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVAKT')])
TVKOT = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVKOT')])
TVTWT = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TCURF')])
TVKBT = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TCURF')])
T014T = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='T014T')])
TVAK = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVAK')])
TVFST = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVFST')])
MAKT = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='MAKT')])
T001W = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='T001W')])
T001L = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='T001L')])
TVSTT = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVSTT')])
TVKMT = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVKMT')])
TVAPT = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVAPT')])
TVAGT = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVAGT')])
T023T = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='T023T')])
T179T = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='T179T')])
TVRO = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='TVRO')])
KNKK = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='KNKK')])
MARC = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='MARC')])
KNB1 = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='KNB1')])
KNA1 = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='KNA1')])
VBUK = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBUK')])
VBUP = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBUP')])
VBKD = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBKD')])
DD03M = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='DD03M')])
DD02T = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='DD02T')])

all_tables = [
{'VBAK': VBAK,},
{'VBAP': VBAP,},
{'BSAD': BSAD,},
{'TCURF': TCURF,},
{'TCURR': TCURR,},
{'VBFA': VBFA,},
{'CDHDR': CDHDR,},
{'CDPOS': CDPOS,},
{'LIPS': LIPS,},
{'USR02': USR02,},
{'LIKP': LIKP,},
{'JCDS': JCDS,},
{'TJ02T': TJ02T,},
{'TVLST': TVLST,},
{'TVFST': TVFST,},
{'TCURX': TCURX,},
{'VBEP': VBEP,},
{'VBUK': VBUK,},
{'DD07T': DD07T,},
{'MKPF': MKPF,},
{'VBRP': VBRP,},
{'VBRK': VBRK,},
{'NAST': NAST,},
{'T685T': T685T,},
{'VTTP': VTTP,},
{'BKPF': BKPF,},
{'TVAKT': TVAKT,},
{'TVKOT': TVKOT,},
{'TVTWT': TVTWT,},
{'TVKBT': TVKBT,},
{'T014T': T014T,},
{'TVAK': TVAK,},
{'TVFST': TVFST,},
{'MAKT': MAKT,},
{'T001W': T001W,},
{'T001L': T001L,},
{'TVSTT': TVSTT,},
{'TVKMT': TVKMT,},
{'TVAPT': TVAPT,},
{'TVAGT': TVAGT,},
{'T023T': T023T,},
{'T179T': T179T,},
{'TVRO': TVRO,},
{'KNKK': KNKK,},
{'MARC': MARC,},
{'KNB1': KNB1,},
{'KNA1': KNA1,},
{'VBUK': VBUK,},
{'VBUP': VBUP,},
{'VBKD': VBKD,},
{'DD03M': DD03M,},
{'DD02T': DD02T,},
]