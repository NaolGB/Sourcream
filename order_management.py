from datetime import datetime, timedelta
import uuid
import values, helpers
import random
import pandas as pd
import numpy as np
import create_sap_table.create_table_leanx as sap_table

# required tables
VBAK = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBAK')])
VBAP = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBAP')])

LIKP = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='LIKP')])
LIPS = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='LIPS')])

MKPF = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='MKPF')])
MSEG = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='MSEG')])

# VBRK = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBRK')])
# VBRP = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBRP')])

BKPF = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='BKPF')])
BSEG = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='BSEG')])

VBFA = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='VBFA')])

CDHDR = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='CDHDR')])
CDPOS = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='CDPOS')])

USR02 = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='USR02')])
MARA = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='MARA')])
KNA1 = pd.DataFrame(columns=[col[0] for col in sap_table.fetch_table(table_name='KNA1')])


class User:
    def __init__(self, bname, ustyp, mandt=values.mandt) -> None:
        self.mandt = mandt
        self.bname = bname
        self.ustyp = ustyp

class Material:
    def __init__(self, matnr, price, mandt=values.mandt) -> None:
        self.mandt = mandt
        self.matnr = matnr
        self.price = price

class Customer:
    def __init__(self, kunnr, erdat, mandt=values.mandt) -> None:
        self.mandt = mandt
        self.kunnr = kunnr
        self.erdat = erdat
        
class SalesOrderItem:
    def __init__(self, vbeln, posnr, mandt=values.mandt) -> None:
        self.mandt = mandt
        self.vbeln = vbeln
        self.posnr = posnr

# insert tables and create objects list
USERS = []
for k, v in values.users.items():
    users_last_index = len(USR02)
    USR02.loc[users_last_index, 'MANDT'] = values.mandt
    USR02.loc[users_last_index, 'BNAME'] = k
    USR02.loc[users_last_index, 'USTYP'] = v

    USERS.append(User(bname=k, ustyp=v))

CUSTOMERS = []
for k, v in values.customers.items():
    kna1_last_index = len(KNA1)
    rand_kunnr = uuid.uuid4()
    rand_erdat = helpers.generate_random_datetime(start_date=datetime(2009, 1, 1), end_date=datetime(2010, 1, 1))

    KNA1.loc[kna1_last_index, 'MANDT'] = values.mandt
    KNA1.loc[kna1_last_index, 'KUNNR'] = rand_kunnr

    CUSTOMERS.append(Customer(kunnr=rand_kunnr, erdat=rand_erdat))

MATERIALS = []
for k, v in values.materials.items():
    mara_last_index = len(MATERIALS)
    rand_matnr = uuid.uuid4()

    MARA.loc[mara_last_index, 'MANDT'] = values.mandt
    MARA.loc[mara_last_index, 'MATNR'] = rand_matnr

    MATERIALS.append(Material(matnr=rand_matnr, price=v['price']))


class SalesOrder:
    def __init__(self, ernam, erdat, vbtyp, agreed_delivery_time: datetime) -> None:
        self.mandt = values.mandt
        self.vbeln = uuid.uuid4()
        self.erdat = erdat
        self.ernam = ernam
        self.vbtyp = vbtyp
        self.netwr = 0
        self.delco = agreed_delivery_time

        self.vbaps = []
        self.likp_id = uuid.uuid4()
        self.mkpf_mblnr = uuid.uuid4()
        self.vbrk_id = uuid.uuid4()

        self.activity_create_sales_order()

    def activity_create_sales_order(self):
        vbak_last_index = len(VBAK)
        VBAK.loc[vbak_last_index, 'MANDT'] = self.mandt
        VBAK.loc[vbak_last_index, 'VBELN'] = self.vbeln
        VBAK.loc[vbak_last_index, 'ERNAM'] = self.ernam
        VBAK.loc[vbak_last_index, 'ERDAT'] = self.erdat
        VBAK.loc[vbak_last_index, 'VBTYP'] = self.vbtyp
    
    def activity_create_sales_order_item(self, materials: list):
        for i, mat in enumerate(materials):
            quantity = random.randint(25, 150)
            vbap_last_index = len(VBAP)

            VBAP.loc[vbap_last_index, 'MANDT'] = self.mandt
            VBAP.loc[vbap_last_index, 'VBELN'] = self.vbeln
            VBAP.loc[vbap_last_index, 'POSNR'] = i+1
            VBAP.loc[vbap_last_index, 'MATNR'] = mat.matnr
            VBAP.loc[vbap_last_index, 'KWMENG'] = quantity # Cumulative Order Quantity in Sales Units
            VBAP.loc[vbap_last_index, 'NETWR'] = mat.price * 12 * 12 * quantity # calculated as a box which usually contains 12 dozens
            VBAP.loc[vbap_last_index, 'VBELN'] = self.vbeln

            self.netwr += mat.price * 12 * 12 * quantity
            self.vbaps.append(SalesOrderItem(vbeln=self.vbeln, posnr=i))

    def activity_generate_delivery_doc(self, delivery_doc_created_at: datetime, activity_by: User):        
        # generate the delivery document
        likp_last_index = len(LIKP)
        
        LIKP.loc[likp_last_index, 'MANDT'] = self.mandt
        LIKP.loc[likp_last_index, 'VBELN'] = self.likp_id
        LIKP.loc[likp_last_index, 'ERDAT'] = delivery_doc_created_at
        LIKP.loc[likp_last_index, 'ERNAM'] = activity_by

        # record LIPS
        for vbap in self.vbaps:
            lips_last_index = len(LIPS)

            LIPS.loc[lips_last_index, 'MANDT'] = self.mandt
            LIPS.loc[lips_last_index, 'VBELN'] = self.likp_id
            LIPS.loc[lips_last_index, 'POSNR'] = vbap.posnr

            # record the document flow
            vbfa_last_index = len(vbfa_last_index)
            VBFA.loc[vbfa_last_index, 'MANDT'] = self.mandt
            VBFA.loc[vbfa_last_index, 'VBELV'] = vbap.vbeln
            VBFA.loc[vbfa_last_index, 'POSNV'] = vbap.posnr
            VBFA.loc[vbfa_last_index, 'VBTYP_V'] = 'C' # Order
            VBFA.loc[vbfa_last_index, 'VBELN'] = self.likp_id
            VBFA.loc[vbfa_last_index, 'POSNN'] = vbap.posnr
            VBFA.loc[vbfa_last_index, 'VBTYP_N'] = 'J'

    def activity_release_delivery(self, delivery_released_at: datetime, activity_by: User):
        # https://leanx.eu/en/sap/table/lips.html
        
        # TODO include VBLB table for release type in conneciton with VBAK, VBAP, VBUK, VBUP
        # record LIPS
        for lips_index in LIPS[LIPS['VBELN'] == self.likp_id].index.values:
            rand_change_nr = uuid.uuid4()
            cdpos_last_index = len(CDPOS)
            value_old = LIPS.loc[lips_index, 'ABART']
            LIPS.loc[lips_index, 'ABART'] = 6

            # record change CDPOS
            CDPOS.loc[cdpos_last_index, 'MANDANT'] = self.mandt
            CDPOS.loc[cdpos_last_index, 'OBJECTCLAS'] = "LIPS"
            CDPOS.loc[cdpos_last_index, 'OBJECTID'] = f"{self.mandt}{LIPS.loc[lips_index, 'VBELN']}{LIPS.loc[lips_index, 'POSNR']}"
            CDPOS.loc[cdpos_last_index, 'CHANGENR'] = rand_change_nr
            CDPOS.loc[cdpos_last_index, 'TABNAME'] = "LIPS"
            CDPOS.loc[cdpos_last_index, 'TABKEY'] = f"{self.mandt}{LIPS.loc[lips_index, 'VBELN']}"
            CDPOS.loc[cdpos_last_index, 'FNAME'] = 'ABART'
            CDPOS.loc[cdpos_last_index, 'CHNGIND'] ='U'
            CDPOS.loc[cdpos_last_index, 'VALUE_OLD'] = value_old
            CDPOS.loc[cdpos_last_index, 'VALUE_NEW'] = LIPS.loc[lips_index, 'ABART']

        # record change CDHDR
        cdhdr_last_index = len(CDHDR)
        CDHDR.loc[cdhdr_last_index, 'MANDANT'] = self.mandt
        CDHDR.loc[cdhdr_last_index, 'OBJECTCLAS'] = "LIPS"
        CDHDR.loc[cdhdr_last_index, 'OBJECTID'] = self.likp_id
        CDHDR.loc[cdhdr_last_index, 'CHANGENR'] = rand_change_nr
        CDHDR.loc[cdhdr_last_index, 'USERNAME'] = activity_by
        CDHDR.loc[cdhdr_last_index, 'UDATE'] = delivery_released_at

    def activity_ship_goods(self, shipped_at: datetime, activity_by: User):
        # record new MKPF
        mkpf_last_index = len(MKPF)

        MKPF.loc[mkpf_last_index, 'MANDT'] = self.mandt
        MKPF.loc[mkpf_last_index, 'MBLNR'] = self.mkpf_mblnr
        MKPF.loc[mkpf_last_index, 'SPE_BUDAT_UHR'] = shipped_at
        MKPF.loc[mkpf_last_index, 'USNAM'] = activity_by

        # record new MSEG
        for vbap in self.vbaps:
            mseg_last_index = len(MSEG)

            MSEG.loc[mseg_last_index, 'MANDT'] = self.mandt
            MSEG.loc[mseg_last_index, 'MBLNR'] = self.mkpf_mblnr
            MSEG.loc[mseg_last_index, 'ZEILE'] = vbap.posnr

        # record the document flow
        for lips_index in LIPS[LIPS['VBELN'] == self.likp_id].index.values:
            vbfa_last_index = len(VBFA)
            VBFA.loc[vbfa_last_index, 'MANDT'] = self.mandt
            VBFA.loc[vbfa_last_index, 'VBELV'] = LIPS.loc[lips_index, 'VBELN']
            VBFA.loc[vbfa_last_index, 'POSNV'] = LIPS.loc[lips_index, 'POSNR']
            VBFA.loc[vbfa_last_index, 'VBTYP_V'] = 'J' # Delivery
            VBFA.loc[vbfa_last_index, 'VBELN'] = self.mkpf_mblnr
            VBFA.loc[vbfa_last_index, 'POSNN'] = LIPS.loc[lips_index, 'POSNR'] # TODO change to MSEG POSNR
            VBFA.loc[vbfa_last_index, 'VBTYP_N'] = 'R' # Goods movement
    
    # def activity_create_billing_document(self, invoice_sent_at: datetime, activity_by: User):
    #     # record new VBRK
    #     vbrk_last_index = len(VBRK)
    #     VBRK.loc[vbrk_last_index, 'MANDT'] = self.mandt
    #     VBRK.loc[vbrk_last_index, 'VBELN'] = self.vbrk_id
    #     VBRK.loc[vbrk_last_index, 'ERNAM'] = activity_by
    #     VBRK.loc[vbrk_last_index, 'ERDAT'] = invoice_sent_at

    #     # create VBRP
    #     for vbap in self.vbaps:
    #         vbrp_last_index = len(VBRP)
    #         VBRP.loc[vbrp_last_index, 'MANDT'] = self.mandt
    #         VBRP.loc[vbrp_last_index, 'VBELN'] = self.vbrk_id
    #         VBRP.loc[vbrp_last_index, 'POSNR'] = vbap.posnr

    #     # record VBFA
    #     for mseg_index in MSEG[MSEG['MBLNR'] == self.mkpf_mblnr].index.values:
    #         vbfa_last_index = len(VBFA)
    #         VBFA.loc[vbfa_last_index, 'MANDT'] = self.mandt
    #         VBFA.loc[vbfa_last_index, 'VBELV'] = MSEG.loc[mseg_index, 'MBLNR']
    #         VBFA.loc[vbfa_last_index, 'POSNV'] = MSEG.loc[mseg_index, 'ZEILE']
    #         VBFA.loc[vbfa_last_index, 'VBTYP_V'] = 'R' # Goods movement
    #         VBFA.loc[vbfa_last_index, 'VBELN'] = self.vbrk_id
    #         VBFA.loc[vbfa_last_index, 'POSNN'] = MSEG.loc[mseg_index, 'POSNR'] # TODO change to VBRP POSNR
    #         VBFA.loc[vbfa_last_index, 'VBTYP_N'] = 'M' # Invoice

    def activity_create_invoice(self):
        pass

    def activity_receive_delivery_confirmation(self, actual_delivery_at: datetime, delivery_confirmation_received_at: datetime, activity_by: User):
        # update delivery document header
        likp_index = LIKP[LIKP['VBELN'] == self.likp_id].index.values[0]
        
        value_old = LIKP.loc[likp_index, 'SPE_ACC_APP_STS']
        LIKP.loc[likp_index, 'SPE_ACC_APP_STS'] = 'C'
        LIKP.loc[likp_index, 'LFUHR'] = actual_delivery_at

        rand_change_nr = uuid.uuid4()
        cdpos_last_index = len(CDPOS)

        # record change CDPOS
        CDPOS.loc[cdpos_last_index, 'MANDANT'] = self.mandt
        CDPOS.loc[cdpos_last_index, 'OBJECTCLAS'] = "LIKP"
        CDPOS.loc[cdpos_last_index, 'OBJECTID'] = f"{self.mandt}{self.likp_id}"
        CDPOS.loc[cdpos_last_index, 'CHANGENR'] = rand_change_nr
        CDPOS.loc[cdpos_last_index, 'TABNAME'] = "LIKP"
        CDPOS.loc[cdpos_last_index, 'TABKEY'] = f"{self.mandt}{self.likp_id}"
        CDPOS.loc[cdpos_last_index, 'FNAME'] = 'SPE_ACC_APP_STS'
        CDPOS.loc[cdpos_last_index, 'CHNGIND'] ='U'
        CDPOS.loc[cdpos_last_index, 'VALUE_OLD'] = value_old
        CDPOS.loc[cdpos_last_index, 'VALUE_NEW'] = LIKP.loc[likp_index, 'SPE_ACC_APP_STS']

        # record change CDHDR
        cdhdr_last_index = len(CDHDR)
        CDHDR.loc[cdhdr_last_index, 'MANDANT'] = self.mandt
        CDHDR.loc[cdhdr_last_index, 'OBJECTCLAS'] = "LIKP"
        CDHDR.loc[cdhdr_last_index, 'OBJECTID'] = self.likp_id
        CDHDR.loc[cdhdr_last_index, 'CHANGENR'] = rand_change_nr
        CDHDR.loc[cdhdr_last_index, 'USERNAME'] = activity_by
        CDHDR.loc[cdhdr_last_index, 'UDATE'] = delivery_confirmation_received_at

    def activity_clear_invoice(self):
        pass