import uuid
import random
from datetime import datetime, timedelta
from helpers import helpers
from values import values_default as values

class Purchasing:
    def __init__(self, params, start_date, index) -> None:
        self.index = index
        self.purchase_req_number = f'{str(uuid.uuid4())[-5:]}{self.index}' # HACK to avoid overflow - short ids are used, to maintain uniqueness - index is used
        #self.has_pr = True if random.random() > 0.11 else False
        self.purchase_order_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.mat_doc_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.unit = values.om_units[random.choice(list(values.om_units.keys()))]['MSEHI']
        self.pr_req_date = start_date
        self.inv_due_date = self.pr_req_date + helpers.ONE_TO_TWOMONTHS() + helpers.ONE_TO_TWOMONTHS() + helpers.UPTO_MONTH()
        self.fy = int(start_date.year)
        self.beleg_number_vendorcredit = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.beleg_number_vendordebit = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.beleg_number_invoice = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.beleg_number_creditmemo = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.clearing_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.incoming_material_document_item_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.params = params

        self.tables = {
            'BKPF_json': {},
            'BSEG_json': {},
            'EBAN_json': {}, 
            'CDHDR_json': {},
            'CDPOS_json': {},
            'EKES_json':{},
            'EKKO_json': {},
            'EKPO_json': {},
            'NAST_json': {},
            'MSEG_json': {},
            'EKBE_json': {},
            'RBKP_json': {},
            'RSEG_json': {},
            'EKET_json': {},
        }

    def changes(self, objid, objclas, udate, uname, chngid, fname, tabkey, tabname, valold, valnew, utime, tcode='DEFAULT'):
        changenr = f'{str(uuid.uuid4())[-5:]}{self.index}'
        # HACK one-to-one mapping between CDHDR adn CDPOS even for line items

        self.tables['CDHDR_json'][str(uuid.uuid4())] = {
            "CHANGENR": changenr,
            "MANDANT": values.mandt,
            "OBJECTCLAS": objclas,
            "OBJECTID": objid,
            "TCODE": tcode,
            "UDATE": udate,
            "USERNAME": uname,
            "UTIME": utime,
            # "VALUE_NEW": valnew, #TEMP TEST
            # "VALUE_OLD": valold, #TEMP TEST
            # "CHNGIND": chngid, #TEMP TEST
            # "FNAME": fname, #TEMP TEST
            # "TABKEY": tabkey, #TEMP TEST
            # "TABNAME": tabname, #TEMP TEST
        }

        self.tables['CDPOS_json'][str(uuid.uuid4())] = {
            "CHANGENR": changenr,
            "CHNGIND": chngid,
            "FNAME": fname,
            "MANDANT": values.mandt,
            "OBJECTCLAS": objclas,
            "OBJECTID": objid,
            "TABKEY": tabkey,
            "TABNAME": tabname,
            "VALUE_NEW": valnew,
            "VALUE_OLD": valold,
        }

    def create_contract(self, aedat, ernam):
        header_time = helpers.generate_random_time()
        # if self.params['has_contract']:
        # if random.random() < 0.85: 
        self.tables['EKKO_json'][str(uuid.uuid4())] = {
            'AEDAT': aedat,
            'BSART': 'F',
            'BSTYP': 'K', # type: Contract
            'BUKRS': self.params['company_code'],
            'EBELN': self.params['konnr'], # Contract's EBELN
            'EKORG': self.params['purchasing_org'],
            'ERNAM': ernam,
            'FRGGR': 'D', # TODO add custom value
            'FRGKE': '2',
            'FRGSX': 'D', # TODO add custom value
            'FRGZU': 'X', # TODO check the effects of this
            'KDATB': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
            'KDATE': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
            'KONNR': self.params['konnr'],
            'LIFNR': self.params['lifnr'],
            'LOEKZ': 'D',
            'MANDT': values.mandt,
            'RESWK': None, # HACK
            'STATU': 'B',
            'WAERS': 'EUR',
            'ZBD1P': self.params['cashdiscount'],
            'ZBD1T': self.params['paymentdays'],
            'ZBD2P': 0,
            'ZBD2T': 0,
            'ZBD3T': 0,
            'ZTERM': self.params['payment_term'],
        }
        self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=aedat, 
                utime=header_time,
                uname=ernam, 
                chngid='I', 
                fname='KEY', 
                tabkey=f'{values.mandt}{self.params["konnr"]}', 
                tabname='EKKO', 
                valold=None,
                valnew=None,
            )
        for i in range(len(self.params['matnrs'])):
            # if self.params['item_has_contract'][i]:
            # if random.random() < 0.85: 
            self.tables['EKPO_json'][str(uuid.uuid4())] = {
                'AEDAT': aedat,
                'AFNAM': self.params['requested_by'],
                'BPRME': 1,
                'BSTYP': 'K',
                'BUKRS': self.params['company_code'],
                'DPDAT': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
                'EBELN': self.params['konnr'],
                'EBELP': i,
                'KONNR': self.params['konnr'],
                'KTMNG': self.params['quantities'][i],
                'KTPNR': i, # NOTE matches with EBAN
                'LOEKZ': 'D', # HACK
                'MANDT': values.mandt,
                'MATNR': self.params['matnrs'][i],
                'MEINS': self.unit,
                'MENGE': 0, #self.params['quantities'][i],
                'NETPR': self.params['prices'][i],
                'NETWR': 0.00, #round(self.params['prices'][i]*self.params['quantities'][i], 2),
                'PEINH': 1,
                'REPOS': None, # Invoice not recieved
                "TXZ01": self.params['matnrs'][i],
                'UEBTO': 0,
                'WEBRE': None,
                'WEPOS': None, # Goods receipt indicator
                'WERKS': self.params['plant'],
                'ZWERT': round((self.params['prices'][i]*self.params['quantities'][i]) * (self.params['cashdiscount']/100), 2),
            }
            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=aedat, 
                utime=helpers.add_time(header_time, helpers.UPTO_3_HOURS()),
                uname=ernam, 
                chngid='I', 
                fname='KEY', 
                tabkey=f'{values.mandt}{self.params["konnr"]}{i}', 
                tabname='EKPO', 
                valold=None,
                valnew=None,
            )

    def create_purchase_requisition_item(self, badat, ernam):
        #if self.has_pr == True:
        for i in range(len(self.params['matnrs'])):
            self.tables['EBAN_json'][str(uuid.uuid4())] = {
                "AFNAM": self.params['requested_by'],
                "BADAT": badat,
                "BANFN": self.purchase_req_number,
                "BNFPO": i,
                "BSTYP": 'B',
                "ERNAM": ernam,
                "ESTKZ": 'B' if ernam == 'BATCH_JOB' else 'D', # Direct procurement if not from material planning
                "FRGKZ": '2', # 'RFQ/purchase order' in values.release_indicators
                "KONNR": self.params['konnr'] if self.params['item_has_contract'][i] and self.params['has_contract'] else None, #TEMP TO CHECK
                "KTPNR": i if self.params['item_has_contract'][i] else None, # HACK -1 not None so as to make pd not consider this a float and add .0 to all
                "LIFNR": self.params['lifnr'],
                "LOEKZ": 'D', # TODO add custom value
                "MANDT": values.mandt,
                "MATNR": None if self.params['is_free_text'] else self.params['matnrs'][i],
                "MEINS": self.unit,
                "MENGE": self.params['quantities'][i],
                "PEINH": 1, # NOTE assumnig price is per item (pcs)
                #"PREIS": self.params['prices'][i],
                "PREIS": round(self.params['prices'][i] if self.params['item_has_contract'][i] else self.params['priceifnocontract'][i],3),
                "STATU": 'N', # NOTE not edited (RFQ not yet created)
                "TXZ01": self.params['free_text_materials'][i] if self.params['is_free_text'] else self.params['matnrs'][i],
                "WAERS": 'EUR',
                "WERKS": self.params['plant'],
            }

            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='BANF', 
                udate=badat, 
                uname=ernam, 
                utime=helpers.generate_random_time(),
                chngid='I', 
                fname='KEY', 
                tabkey=f'{values.mandt}{self.purchase_req_number}{i}', 
                tabname='EBAN', 
                valold=None,
                valnew=None,
            )

    def create_purchase_order(self, aedat, ernam, utime):
        header_time = helpers.generate_random_time()
        self.tables['EKKO_json'][str(uuid.uuid4())] = {
            'AEDAT': aedat,
            'BSART': 'F',
            'BSTYP': 'F',
            'BUKRS': self.params['company_code'],
            'EBELN': self.purchase_order_number,
            'EKORG': self.params['purchasing_org'],
            'ERNAM': ernam,
            'FRGGR': 'D', # TODO add custom value
            'FRGKE': '2',
            'FRGSX': 'D', # TODO add custom value
            'FRGZU': None, # No Approval needed
            'KDATB': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
            'KDATE': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
            'KONNR': self.params['konnr'] if self.params['has_contract'] else None, # TODO check what the effect of using has_contract is vs having multiple POs for contracts
            'LIFNR': self.params['lifnr'],
            'LOEKZ': 'D', # DeletionIndicator
            'MANDT': values.mandt,
            'RESWK': None, # HACK
            'STATU': 'B',
            'WAERS': 'EUR',
            'ZBD1P': self.params['cashdiscount'],#random.uniform(0.1, 0.3), #if random.random() > 0.5 else None, # test
            'ZBD1T': self.params['paymentdays'], # test
            'ZBD2P': 0, #random.uniform(0.1, 0.4), #if random.random() > 0.5 else None, # test
            'ZBD2T': 0, # test
            'ZBD3T': 0, # test
            'ZTERM': self.params['payment_term'],
        }
        self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=aedat, 
                utime=utime,
                uname=ernam, 
                chngid='I', 
                fname='KEY', 
                tabkey=f'{values.mandt}{self.purchase_order_number}', 
                tabname='EKKO', 
                valold=None,
                valnew=None,
            )
        for i in range(len(self.params['matnrs'])):
            randnom = random.random()
            #priceifnocontract = self.params['prices'][i] * (random.uniform(1.1, 1.5))
            self.tables['EKPO_json'][str(uuid.uuid4())] = {
                'AEDAT': aedat,
                'AFNAM': self.params['requested_by'],
                "BANFN": self.purchase_req_number if self.params['has_pr'] == True else None,
                "BNFPO": i if self.params['has_pr'] == True else None,
                'BPRME': 1,
                'BSTYP': 'F',
                'BUKRS': self.params['company_code'],
                'DPDAT': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
                'EBELN': self.purchase_order_number,
                'EBELP': i,
                'KONNR': self.params['konnr'] if self.params['item_has_contract'][i] and self.params['has_contract'] else None,
                'KTMNG': None, # contract amount
                'KTPNR': i if self.params['item_has_contract'][i] else None, # HACK -1 not None so as to make pd not consider this a float and add .0 to all
                'LOEKZ': 'D', # DeletionIndicator
                'MANDT': values.mandt,
                "MATNR": None if self.params['is_free_text'] and randnom > 0.3 else self.params['matnrs'][i],
                'MEINS': self.unit,
                'MENGE': self.params['quantities'][i],
                'NETPR': round(self.params['prices'][i] * ((100 - self.params['cashdiscount'])/100) if self.params['item_has_contract'][i] else self.params['priceifnocontract'][i] * ((100 - self.params['cashdiscount'])/100),3),
                'NETWR': round((self.params['prices'][i]*self.params['quantities'][i]) * ((100 - self.params['cashdiscount'])/100), 3) if self.params['item_has_contract'][i] else round((self.params['priceifnocontract'][i] * self.params['quantities'][i]) * ((100 - self.params['cashdiscount'])/100), 3) , #netamount
                'PEINH': 1, # unit of measure
                'REPOS': None, # InvoiceReceiptIndicator
                "TXZ01": self.params['free_text_materials'][i] if self.params['is_free_text'] and randnom > 0.3 else self.params['matnrs'][i],
                'UEBTO': 0,
                'WEBRE': None, # InvoiceAfterGoodsReceiptIndicator
                'WEPOS': None, # Goods receipt indicator
                'WERKS': self.params['plant'],
                'ZWERT': round((self.params['prices'][i]*self.params['quantities'][i]) * (self.params['cashdiscount']/100), 2),
            }
            self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=aedat, 
                utime=helpers.add_time(utime, helpers.UPTO_3_HOURS()),
                uname=ernam, 
                chngid='I', 
                fname='KEY', 
                tabkey=f'{values.mandt}{self.purchase_order_number}{i}', 
                tabname='EKPO', 
                valold=None,
                valnew=None,
            )

            self.set_confirmed_poitem_deliverydate(aedat=aedat, ernam=ernam, utime=utime, item_pos=i)


    def set_confirmed_poitem_deliverydate(self, aedat, ernam, utime, item_pos):
        self.tables['EKES_json'][str(uuid.uuid4())] = {
            'EBELN': self.purchase_order_number, # = "EKKO"."EBELN" and "EKPO"."EBELN"
            'EBELP': item_pos, # = "EKPO"."EBELP"
            'EBTYP': 'LO', # "EKES"."EBTYP" LIKE 'L%' # ConfirmationCategory
            'EINDT': aedat, # ConfirmationDeliveryDate
            'ERDAT': aedat, # CreationDate 
            'ETENS': item_pos, # DatabasePurchaseOrderVendorConfirmationNumber
            'EZEIT': '1', # CreationTime
            'MANDT': values.mandt, 
            'MENGE': '1', 
        }

        self.changes(
        objid=str(uuid.uuid4()), 
        objclas='EINKBELEG', 
        udate=aedat, 
        utime=utime,
        uname=ernam, 
        chngid='U', 
        fname='EINDT', # or EBTYP for  Confirmation Category
        tabkey=f'{values.mandt}{self.purchase_order_number}{item_pos}{item_pos}', 
        tabname='EKES', 
        valold=None,
        valnew=aedat,
    )




    def send_purchase_order(self, usnam, erdat):
        self.tables['NAST_json'][str(uuid.uuid4())] = {
            'AENDE': None,
            'DATVR': erdat,
            'ERDAT': erdat,
            'ERUHR': helpers.generate_random_time(),
            'KAPPL': 'EF',
            'KSCHL': 'NEU',
            'MANDT': values.mandt,
            'OBJKY': self.purchase_order_number,
            'PARNR': 'D', # TODO add custom value
            'PARVW': 'D', # TODO add custom value
            'SPRAS': 'E',
            'TCODE': 'D', # TODO add custom value
            'UHRVR': helpers.generate_random_time(),
            'USNAM': usnam,
        }

    def goods_receipt(self, cpudt, usnam, atime, udate, utime):
        for i in range(len(self.params['matnrs'])):
            for k, v in self.tables['EKPO_json'].items():
                if( v['EBELN'] == self.purchase_order_number) and (v['EBELP'] == i):
                    self.tables['EKPO_json'][k]['WEPOS'] = 'X' # Goods Receipt Indicator

            delivered_quanity = self.params['quantities'][i] # scheduled quantity
            scheduled_quanity = self.params['quantities'][i] # scheduled quantity

           

            if self.params['delivery_status'][i] < 0:
                if random.random() < 0.3: # If early, then there is a chance it is not in full (Still open) -- by Naol Basaye
                    delivered_quanity -= delivered_quanity*random.random()

            
            self.post_goods_receipt(cpudt=cpudt, usnam=usnam, atime=atime, item_position=i, delivered_quanity=delivered_quanity)
            
            receiptdate = cpudt - timedelta(days=self.params['delivery_status'][i])
            self.create_purchase_order_schedule_line(eindt=receiptdate, creation_date=udate, creation_time=utime, ernam=usnam, ebelp=i, scheduled_quanity=scheduled_quanity, delivered_quanity=delivered_quanity, item_position=i)

    def post_goods_receipt(self, cpudt, usnam, atime, item_position, delivered_quanity):
        temp_uuid = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.tables['MSEG_json'][str(uuid.uuid4())] = {
            'BWART': '101',
            'CPUDT_MKPF': cpudt,
            'CPUTM_MKPF': atime,
            'EBELN': self.purchase_order_number,
            'EBELP': item_position,
            'ERFME': self.unit,
            'KDAUF': self.purchase_order_number,
            'KDPOS': item_position,
            'LBKUM': round(self.params['prices'][item_position]*delivered_quanity, 4),
            'LFBJA': self.fy,
            'LFBNR': temp_uuid,
            'LGORT': 'D', # TODO add custom value,
            'LIFNR': self.params['lifnr'],
            'MANDT': values.mandt,
            'MATNR': self.params['matnrs'][item_position],
            'MBLNR': self.mat_doc_number,
            'MEINS': self.unit,
            'MENGE': delivered_quanity,
            'MJAHR': self.fy,
            'SHKZG': 'S',
            'SJAHR': self.fy,
            'SMBLN': self.mat_doc_number,
            'SMBLP': None, # NOTE is not a reversal
            'USNAM_MKPF': usnam,
            'VBELN_IM': None,
            'VBELP_IM': None,
            'WERKS': self.params['plant'],
            'ZEILE': item_position,
        }
        self.tables['EKBE_json'][str(uuid.uuid4())] = { # TODO check how this affects OutgoingMaterialDocument (in OM/sales_doc_data)
            'BELNR': self.mat_doc_number,
            'BUZEI': item_position,
            'CPUDT': cpudt,
            'GJAHR': self.fy,
            'MANDT': values.mandt,
            'MENGE': delivered_quanity,
            'VGABE': '1',
            'WAERS': 'EUR',
            'WRBTR': round(self.params['prices'][item_position]*delivered_quanity, 4),
        }

    def create_purchase_order_schedule_line(self, eindt, creation_date, creation_time, ernam, ebelp, scheduled_quanity, delivered_quanity, item_position):
        self.tables['EKET_json'][str(uuid.uuid4())] = {
            'BEDAT': creation_date,
            'EBELN': self.purchase_order_number,
            'EBELP': ebelp,
            'EINDT': eindt,
            'ETENR': ebelp, # Delivery Schedule Line Counter
            'MANDT': values.mandt,
            'MENGE': scheduled_quanity, # Quatity Scheduled
            'WEMNG': delivered_quanity, # Quantity of goods received
        }
        self.changes(
            objid = str(uuid.uuid4()), 
            objclas =str(uuid.uuid4()), 
            udate = creation_date, 
            utime=creation_time,
            uname = ernam, 
            chngid = 'I', #'I' then CreationTime, 'D' DeletionTime 
            fname = 'KEY', 
            tabkey = f'{values.mandt}{self.purchase_order_number}{ebelp}{ebelp}', 
            tabname = 'EKET', 
            valold = None, 
            valnew = None
        )

    def create_vendor_invoice(self, ernam, cpudt):
        self.tables['RBKP_json'][str(uuid.uuid4())] = {
            'BELNR': self.beleg_number_invoice,
            'BLDAT': cpudt, # document date in document
            'BUKRS': self.params['company_code'],
            'CPUDT': cpudt, # Day on which accounting doc was entered
            'CPUTM': helpers.generate_random_time(),
            'GJAHR': self.fy,
            'LIFNR': self.params['lifnr'],
            'MANDT': values.mandt,
            'SGTXT': f'Vendor invoice {self.beleg_number_invoice}', # TODO add custom value
            'STBLG': None,
            'STJAH' : None,
            'USNAM': ernam,
            'VGART': 'RD', #Logistics Invoice (requirement)
            'WAERS': 'EUR',
            'XRECH' : 'X', # new field version 2.0 Post invoice, possible values are NULL . for no or X for yes
            'ZBD1P': self.params['cashdiscount'],
            'ZBD1T': self.params['paymentdays'],
            'ZBD2P': 0,
            'ZBD2T': 0,
            'ZBD3T': 0,
            'ZFBDT': self.inv_due_date, # Baseline Date for Due Date Calculation
            'ZLSCH': 'D', # TODO add custom value
            'ZLSPR': 'D', # TODO add custom value
            'ZTERM': self.params['payment_term']  # TODO see if this needs to match when self.change_payment_term is called
        }

        for i in range(len(self.params['matnrs'])):
            self.tables['RSEG_json'][str(uuid.uuid4())] = {
                'BELNR': self.beleg_number_invoice,
                'BSTME': self.unit, #Unit of Measurement
                'BUKRS': self.params['company_code'],
                'BUZEI': i, #Document Item in Invoice Document
                'EBELN': self.purchase_order_number,
                'EBELP': i,
                'GJAHR': self.fy,
                'LFBNR': self.mat_doc_number,
                'LFGJA': self.fy,
                'LFPOS': i, #item of reference document
                'LIFNR': self.params['lifnr'],
                'MANDT': values.mandt,
                'MATNR': self.params['matnrs'][i],
                'MENGE': self.params['quantities'][i],
                'WERKS': self.params['plant'],
                'SHKZG': 'S', # S for debit , H for credit new field version 2.0 
                #'WRBTR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
                'WRBTR': round(self.params['prices'][i]*self.params['quantities'][i], 2) if self.params['item_has_contract'][i] else round(self.params['priceifnocontract'][i] * self.params['quantities'][i], 2) ,
            }
        
            for k, v in self.tables['EKPO_json'].items():
                    if (v['EBELN'] == self.purchase_order_number) and (v['EBELP'] == i):
                        self.tables['EKPO_json'][k]['REPOS'] = 'X'

    def create_vendor_creditmemo(self, ernam, cpudt):
        self.tables['RBKP_json'][str(uuid.uuid4())] = {
            'BELNR': self.beleg_number_creditmemo,
            'BLDAT': cpudt, # document date in document
            'BUKRS': self.params['company_code'],
            'CPUDT': cpudt, # Day on which accounting doc was entered
            'CPUTM': helpers.generate_random_time(),
            'GJAHR': self.fy,
            'LIFNR': self.params['lifnr'],
            'MANDT': values.mandt,
            'STBLG': None,
            'STJAH' : None,
            'SGTXT': f'Invoice Reduction {self.beleg_number_creditmemo}', # TODO add custom value
            'USNAM': ernam,
            'VGART': 'RD', #Credit Memo  alternative RS but that activates invoice cancellation item too
            'WAERS': 'EUR',
            'XRECH' : None, # new field version 2.0 Post invoice, possible values are NULL . for no or X for yes
            'ZBD1P': self.params['cashdiscount'],
            'ZBD1T': self.params['paymentdays'],
            'ZBD2P': 0,
            'ZBD2T': 0,
            'ZBD3T': 0,
            'ZFBDT': self.inv_due_date, # Baseline Date for Due Date Calculation
            'ZLSCH': 'T', # TODO add custom value
            'ZLSPR': None, 
            'ZTERM': self.params['payment_term']  # TODO see if this needs to match when self.change_payment_term is called
        }

        for i in range(len(self.params['matnrs'])):
            #if random.random() > 0.7: # choosing random when to have credit memo for now. 
            self.tables['RSEG_json'][str(uuid.uuid4())] = {
                'BELNR': self.beleg_number_creditmemo,
                'BSTME': self.unit, #Unit of Measurement
                'BUKRS': self.params['company_code'],
                'BUZEI': i, #Document Item in Invoice Document
                'EBELN': self.purchase_order_number,
                'EBELP': i,
                'GJAHR': self.fy,
                'LFBNR': self.mat_doc_number,
                'LFGJA': self.fy,
                'LFPOS': i, #item of reference document
                'LIFNR': self.params['lifnr'],
                'MANDT': values.mandt,
                'MATNR': self.params['matnrs'][i],
                'MENGE': self.params['quantities'][i],
                'WERKS': self.params['plant'],
                'SHKZG': 'H', # S for debit , H for credit new field version 2.0 
                #'WRBTR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
                'WRBTR': (round(self.params['prices'][i]*self.params['quantities'][i], 2) * 0.05) if self.params['item_has_contract'][i] else (round(self.params['priceifnocontract'][i] * self.params['quantities'][i], 2) * 0.05) ,
            }
    
    def approve_purchase_order(self, aedat, ernam):
        new_value = 'X'        
        self.changes(
            objid=str(uuid.uuid4()), 
            objclas='EINKBELEG', 
            udate=aedat, 
            uname= ernam, 
            utime=helpers.generate_random_time(),
            chngid='U', 
            fname='FRGZU', 
            tabkey=f'{values.mandt}{self.purchase_order_number}', 
            tabname='EKKO', 
            valold=None,
            valnew=new_value,
        )
        for k, v in self.tables['EKKO_json'].items():
            if( v['EBELN'] == self.purchase_order_number):
                self.tables['EKKO_json'][k]['FRGZU'] = new_value

    def change_payment_term(self, udate, ernam):
        new_value = self.params['new_payment_term']
        self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=udate, 
                utime=helpers.generate_random_time(),
                uname=ernam, 
                chngid='U', 
                fname='ZTERM',
                tabkey=f'{values.mandt}{self.purchase_order_number}', 
                tabname='EKKO', 
                valold=None,
                valnew=new_value,
            )
        
        for k, v in self.tables['EKKO_json'].items():
            if v['EBELN'] == self.purchase_order_number:
                self.tables['EKKO_json'][k]['ZTERM'] = new_value

    def change_vendor(self, udate, ernam):
        new_value = self.params['new_vendor']
        self.changes(
                objid=str(uuid.uuid4()), 
                objclas='EINKBELEG', 
                udate=udate, 
                utime=helpers.generate_random_time(),
                uname=ernam, 
                chngid='U', 
                fname='LIFNR',
                tabkey=f'{values.mandt}{self.purchase_order_number}', 
                tabname='EKKO', 
                valold=None, # HACK using none instead of the old EKKO.LIFNR because it is not a requirement in the transformation
                valnew=new_value,
            )
        
        for k, v in self.tables['EKKO_json'].items():
            if v['EBELN'] == self.purchase_order_number:
                self.tables['EKKO_json'][k]['LIFNR'] = new_value
    
    def change_quantity(self, badat, ernam, line_numbers, line_quantities):
        for i, item_position in enumerate(line_numbers):
            self.changes(
                objid = str(uuid.uuid4()), 
                objclas ='EINKBELEG', 
                udate = badat, 
                utime=helpers.generate_random_time(),
                uname = ernam, 
                chngid = 'U', 
                fname = 'MENGE', 
                tabkey = f'{values.mandt}{self.purchase_order_number}{item_position}', 
                tabname = 'EKPO', 
                valold = None, 
                valnew = line_quantities[i]
            )

            # change line 
            for k, v in self.tables['EKPO_json'].items():
                if (v['EBELN'] == self.purchase_order_number) and (v['EBELP'] == item_position):
                    self.tables['EKPO_json'][k]['MENGE'] = line_quantities[i]
                    self.tables['EKPO_json'][k]['NETWR']  = round((self.params['prices'][i]*self.params['quantities'][i]) * ((100 - self.params['cashdiscount'])/100), 3) if self.params['item_has_contract'][i] else round((self.params['priceifnocontract'][i] * self.params['quantities'][i]) * ((100 - self.params['cashdiscount'])/100), 3) , # quick check if this is issue. 


    def PostVendorAccountCreditItem(self, usnam, cpudt, tcode='DEFAULT'): # includes clearing 
        self.tables['BKPF_json'][str(uuid.uuid4())] = {
            'AWKEY' : f'{self.beleg_number_invoice}{self.fy}' , # = "RBKP"."BELNR" || "RBKP"."GJAHR"
            'AWTYP' :  'RMRP', # PurchaseOrderRelated
            'BELNR' : self.beleg_number_vendorcredit , # "BSEG"."BELNR"
            'BLART' : 'ZV' , # DocumentType "BKPF"."BLART"
            'BLDAT' :  cpudt, # DocumentDate
            'BUKRS' : self.params['company_code'] , #  = "BSEG"."BUKRS"
            'CPUDT' : cpudt , # CreationTime
            'CPUTM' : helpers.generate_random_time() , # CreationTime
            'GJAHR' : self.fy ,
            'MANDT' :  values.mandt,
            'TCODE' : tcode,
            'USNAM' :  usnam,
            'WAERS' :  'EUR', # Currency
            'XBLNR' :  '1', # ReferenceDocumentNumber
            'XREVERSAL' : None , # 1 or 2 if reversal document 
        }
        cleardate = self.inv_due_date + timedelta(days=random.randint(-3, 11))
        for i in range(len(self.params['matnrs'])):
            cashdiscounttaken = random.uniform(0.6, 1)
            self.tables['BSEG_json'][str(uuid.uuid4())] = {
                'AUGBL' : self.beleg_number_vendorcredit , #part of clearing ID
                'AUGDT' : cleardate, # ClearingDate
                'AUGGJ' : self.fy, # part of clearing ID
                'BELNR' : self.beleg_number_vendorcredit , # number to join with BKPF and RBKP?
                'BSCHL' : '31' , # invoice
                'BUKRS' : self.params['company_code'] , # part of VendorMasterCompanyCode
                'BUZEI' : i , # SystemAccountingDocumentItemNumber
                'GJAHR' : self.fy ,
                'KOART' : 'K' ,
                'KUNNR' : None ,
                'LIFNR' : self.params['lifnr'] ,
                'MANDT' : values.mandt ,
                'MANSP' : None ,
                'MANST' : None ,
                'MATNR' : self.params['matnrs'][i] ,
                'SGTXT' : 'D' , #  ItemText TO DO adjust  
                'SHKZG' : 'H' ,
                'SKFBT' : round(self.params['prices'][i]*self.params['quantities'][i], 4)  , # CashDiscountEligibleAmount
                'WRBTR' : round(self.params['prices'][i]*self.params['quantities'][i], 4) , # Amount
                'WSKTO' : (self.params['cashdiscount'] * 0.01 * cashdiscounttaken) * (round(self.params['prices'][i]*self.params['quantities'][i], 4)) , # CashDiscountTakenAmount
                'ZBD1P' : self.params['cashdiscount'] , # CashDiscountPercentage1
                'ZBD2P' : 0,
                'ZBD1T' : self.params['paymentdays'] ,
                'ZBD2T' : 0,
                'ZBD3T' : 0,
                'ZFBDT' : self.inv_due_date, #Baseline date
                'ZLSCH' : 'T' , # PaymentMethod T for Bank transfer, P for custom digital setup, 
                'ZLSPR' : 'R' if random.random() > 0.8 else None , # PaymentBlock
                'ZTERM' : 'Z030',
        }
            

    def PostVendorAccountDebitItem(self, usnam, cpudt, tcode='DEFAULT'): # includes clearing 
        self.tables['BKPF_json'][str(uuid.uuid4())] = {
            'AWKEY' : f'{self.beleg_number_creditmemo}{self.fy}' , # = "RBKP"."BELNR" || "RBKP"."GJAHR"
            'AWTYP' :  'RMRP', # PurchaseOrderRelated
            'BELNR' : self.beleg_number_vendordebit , # "BSEG"."BELNR"
            'BLART' : 'ZV' , # DocumentType "BKPF"."BLART"
            'BLDAT' :  cpudt, # DocumentDate
            'BUKRS' : self.params['company_code'] , #  = "BSEG"."BUKRS"
            'CPUDT' : cpudt , # CreationTime
            'CPUTM' : helpers.generate_random_time() , # CreationTime
            'GJAHR' : self.fy ,
            'MANDT' :  values.mandt,
            'TCODE' : tcode,
            'USNAM' :  usnam,
            'WAERS' :  'EUR', # Currency
            'XBLNR' :  '1', # ReferenceDocumentNumber
            'XREVERSAL' : None , # 1 or 2 if reversal document 
        }
        cleardate = self.inv_due_date + timedelta(days=random.randint(-3, 5))
        for i in range(len(self.params['matnrs'])):
            is_cleared = True if random.random() > 0.5 else False
            self.tables['BSEG_json'][str(uuid.uuid4())] = {
                'AUGBL' : self.beleg_number_vendordebit if is_cleared == True else None , #part of clearing ID
                'AUGDT' : cleardate if is_cleared == True else None, # ClearingDate
                'AUGGJ' : self.fy if is_cleared == True else None, # part of clearing ID
                'BELNR' : self.beleg_number_vendordebit , # number to join with BKPF and RBKP
                'BSCHL' : '21' , # creditmemoitem
                'BUKRS' : self.params['company_code'] , # part of VendorMasterCompanyCode
                'BUZEI' : i , # SystemAccountingDocumentItemNumber
                'GJAHR' : self.fy ,
                'KOART' : 'K' ,
                'KUNNR' : None ,
                'LIFNR' : self.params['lifnr'] ,
                'MANDT' : values.mandt ,
                'MANSP' : None ,
                'MANST' : None ,
                'MATNR' : self.params['matnrs'][i] ,
                'SGTXT' : 'D' , #  ItemText TO DO adjust  
                'SHKZG' : 'S' ,
                'SKFBT' : round(self.params['prices'][i]*self.params['quantities'][i], 4)  , # CashDiscountEligibleAmount
                'WRBTR' : round(self.params['prices'][i]*self.params['quantities'][i], 4) , # Amount
                #'WSKTO' : (round(self.params['prices'][i]*self.params['quantities'][i], 2) * 0.05) if self.params['item_has_contract'][i] else (round(self.params['priceifnocontract'][i] * self.params['quantities'][i], 2) * 0.05), # CashDiscountTakenAmount
                'WSKTO' : (round(self.params['prices'][i]*self.params['quantities'][i], 2) * (self.params['cashdiscount'] * 0.01)) if self.params['item_has_contract'][i] else (round(self.params['priceifnocontract'][i] * self.params['quantities'][i], 2) * (self.params['cashdiscount'] * 0.01)), # CashDiscountTakenAmount
                'ZBD1P' : self.params['cashdiscount'] , # CashDiscountPercentage1
                'ZBD2P' : 0,
                'ZBD1T' : self.params['paymentdays'] ,
                'ZBD2T' : 0,
                'ZBD3T' : 0,
                'ZFBDT' : self.inv_due_date, #Baseline date
                'ZLSCH' : 'T' , # PaymentMethod T for Bank transfer, P for custom digital setup, 
                'ZLSPR' : 'R' if random.random() > 0.8 else None , # PaymentBlock
                'ZTERM' : 'Z030',
        }
# A - Payment Block for Accounting Reasons

# Indicates that there is an issue requiring action by the accounting team, such as incorrect account assignment.
# B - Payment Block for Invoice Verification

# Used when the invoice has not been verified against a goods receipt or purchase order.
# C - Payment Block for Payment Authorization

# Payment is held pending approval or authorization.
# D - Payment Block for Dispute

# Applied when there is a vendor dispute or discrepancy in the invoice.
# R - Manual Payment Block

# Set manually by a user to prevent payment until further notice.
# X - Blocked by the System

# Automatically set by the system for various reasons, such as price discrepancies or missing data.