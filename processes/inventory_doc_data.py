import uuid
import random
from datetime import datetime, timedelta
from masterdata import values
from extras import helpers

class Inventory:
    def __init__(self, vbeln, params, start_date:datetime, index) -> None:
        self.index = index
        self.purchase_req_number = f'{str(uuid.uuid4())[-5:]}{self.index}' # HACK to avoid overflow - short ids are used, to maintain uniqueness - index is used
        self.purchase_order_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.mat_doc_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.unit = values.om_units[random.choice(list(values.om_units.keys()))]['MSEHI']
        self.pr_req_date = start_date
        self.fy = int(start_date.year)
        self.beleg_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.incoming_material_document_item_number = f'{str(uuid.uuid4())[-5:]}{self.index}'
        self.params = params
        self.vbeln = vbeln
        self.objnr = f'{str(uuid.uuid4())[-17:]}' # HACK to avoid overflow when multiple ids being cancatenated
        self.likp_vbeln = f'{str(uuid.uuid4())[-11:]}' 
        self.vbrk_vbeln = f'{str(uuid.uuid4())[-11:]}'
        self.bkpf_belnr = f'{str(uuid.uuid4())[-11:]}'
        self.mblnr = f'{str(uuid.uuid4())[-11:]}'
        self.start_date = start_date
        self.mjahr = int(start_date.year)
        self.prod_order_number = f'{str(uuid.uuid4())[-5:]}{self.index}'

        self.tables = {
            'EBAN_json': {}, 
            'CDHDR_json': {},
            'CDPOS_json': {},
            'EKKO_json': {},
            'EKPO_json': {},
            'NAST_json': {},
            'MSEG_json': {},
            'EKBE_json': {},
            'RBKP_json': {},
            'RSEG_json': {},
            'EKET_json': {},
            'AFKO_json': {},
            'AFPO_json': {},
            'VBAK_json': {},
            'VBAP_json': {},
            'AUFK_json': {},
            'VBFA_json': {},
            'LIKP_json': {},
            'LIPS_json': {},
            'VBKD_json': {},
            'VBUK_json': {},
            'VBEP_json': {},
            'MBEWH_json': {}
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

    def record_flow(self, erdat, prev_vbeln, next_vbeln, prev_type, next_type):
        for i in range(len(self.params['matnrs'])):
            self.tables['VBFA_json'][str(uuid.uuid4())] = {
                "MANDT": values.mandt,
                "VBELV": prev_vbeln,
                "POSNV": i,
                "VBTYP_V": prev_type,
                "VBELN": next_vbeln,
                "POSNN": i,
                "VBTYP_N": next_type,
                "ERDAT": erdat,
                "ERZET": helpers.generate_random_time(),
                "MATNR": self.params['matnrs'][i]
            }
    
    
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
            'LOEKZ': 'D',
            'MANDT': values.mandt,
            'RESWK': None, # HACK
            'STATU': 'B',
            'WAERS': 'EUR',
            'ZBD1P': 0,
            'ZBD1T': 0,
            'ZBD2P': 0,
            'ZBD2T': 0,
            'ZBD3T': 0,
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
            self.tables['EKPO_json'][str(uuid.uuid4())] = {
                'AEDAT': aedat,
                'AFNAM': self.params['requested_by'],
                "BANFN": self.purchase_req_number,
                "BNFPO": i,
                'BPRME': 1,
                'BSTYP': 'F',
                'BUKRS': self.params['company_code'],
                'DPDAT': datetime.fromtimestamp(0).date(), # HACK 01/01/1970
                'EBELN': self.purchase_order_number,
                'EBELP': i,
                'KONNR': self.params['konnr'] if self.params['item_has_contract'][i] else None,
                'KTMNG': self.params['quantities'][i],
                'KTPNR': i if self.params['item_has_contract'][i] else None, # HACK -1 not None so as to make pd not consider this a float and add .0 to all
                'LOEKZ': 'D', # HACK
                'MANDT': values.mandt,
                "MATNR": None if self.params['is_free_text'] and randnom > 0.3 else self.params['matnrs'][i],
                'MEINS': self.unit,
                'MENGE': self.params['quantities'][i],
                'NETPR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
                'NETWR': round(self.params['prices'][i]*self.params['quantities'][i], 4),
                'PEINH': 1,
                'REPOS': None, # Invoice not recieved
                "TXZ01": self.params['free_text_materials'][i] if self.params['is_free_text'] and randnom > 0.3 else self.params['matnrs'][i],
                'UEBTO': 0,
                'WEBRE': None,
                'WEPOS': None, # Goods receipt indicator
                'WERKS': self.params['plant'],
                'ZWERT': round(self.params['prices'][i]*self.params['quantities'][i], 4),
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
            "BWTAR": None,
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
            'WAERS': 'EUR',
            'WERKS': self.params['plant'],
            'ZEILE': item_position,
        }
        self.tables['EKBE_json'][str(uuid.uuid4())] = { # TODO check how this affects OutgoingMaterialDocument (in OM/sales_doc_data)
            'BELNR': self.mat_doc_number,
            'BUZEI': item_position,
            'GJAHR': self.fy,
            'MANDT': values.mandt,
            'MENGE': delivered_quanity,
            'VGABE': '1',
            'WAERS': 'EUR',
            'WRBTR': round(self.params['prices'][item_position]*delivered_quanity, 4),
        }

        self.tables['MBEWH_json'][str(uuid.uuid4())] = {
            "BWKEY": 'VA01',
            "BWTAR": None,
            "LBKUM": (random.randint(500, 10000)),
            "LFGJA": self.fy,
            "LFMON": cpudt.strftime('%m'),
            "MANDT": values.mandt,
            "MATNR": self.params['matnrs'][item_position],
            "PEINH": 1,
            "SALK3": 99, #TO DO add custom value
            "STPRS": self.params['prices'][item_position],
            "VERPR": self.params['prices'][item_position],
            "VPRSV": 'V', # TODO add custom value
        }

    def create_purchase_order_schedule_line(self, eindt, creation_date, creation_time, ernam, ebelp, scheduled_quanity, delivered_quanity, item_position):
        self.tables['EKET_json'][str(uuid.uuid4())] = {
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

    def create_sales_order(
        self,
        shipping_condition,
        erdat,
        reqested_delivery_date,
        ernam,
        atime,
        
        all_units=values.om_units,
        all_categories=values.om_sales_doc_item_categories,
        all_routes=values.om_routes,
    ):
        self.tables['VBAK_json'][str(uuid.uuid4())] = {
            "AUART": self.params['sales_doc_type'],
            "BSTDK": erdat,
            "BSTNK": self.vbeln,
            "BUKRS_VF": self.params['company_code'],
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": atime,
            "KKBER": 'D', # TODO add custom value
            "KUNNR": self.params['kunnr'],
            "MANDT": values.mandt,
            "NETWR": round(sum([self.params['prices'][i]*self.params['quantities'][i] for i in range(len(self.params['matnrs']))]), 4),
            "OBJNR": self.objnr,
            "VBELN": self.vbeln,
            "VBTYP": 'C',
            "VDATU": reqested_delivery_date,
            "VKBUR": self.params['sales_office'],
            "VKORG": self.params['sales_org'],
            "VSBED": shipping_condition,
            "VTWEG": self.params['distribution_channel'],
            "WAERK": 'EUR',
            "LIFSK": None,
            'FAKSK': None
        }
        self.tables['VBKD_json'][str(uuid.uuid4())] = {
            "INCO1": 'D', # TODO add custom value
            "INCO2": 'D', # TODO add custom value
            "MANDT": values.mandt,
            "POSNR": '000000',
            "VBELN": self.vbeln,
            "ZTERM": self.params['payment_term'],
        }
        self.tables['VBUK_json'][str(uuid.uuid4())] = {
            "BESTK": 'A',
            "GBSTK": 'A',
            "MANDT": values.mandt,
            "VBELN": self.vbeln,
            "KOSTK": 'A', # Not yet processed
            "CMGST": None, # Credit Block
        }

        for i in range(len(self.params['matnrs'])):
            temp_vbeln = f'{str(uuid.uuid4())[-11:]}'
            self.tables['VBAP_json'][temp_vbeln] = {
                "ABGRU": None, # 'D' HACK
                "BRGEW": 99, # TODO add custom value
                "ERDAT": erdat,
                "ERNAM": ernam,
                "ERZET": str(helpers.add_random_hours(1, atime)),
                "FKREL": 'A',
                "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "KDMAT": self.params['matnrs'][i],
                "KPEIN": 1,
                "KWMENG": self.params['quantities'][i],
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "NETPR": self.params['prices'][i],
                "NETWR": round(self.params['prices'][i]*self.params['quantities'][i], 4),
                "NTGEW": 99, # TODO add custom value
                "OBJNR": self.objnr,
                "POSNR": i,
                "PSTYV": all_categories[random.choice(list(all_categories.keys()))]['PSTYV'],
                "ROUTE": all_routes[random.choice(list(all_routes.keys()))]['ROUTE'],
                "VBELN": self.vbeln,
                "VGBEL": self.vbeln, # same value as VBUK.VBELN
                "VGPOS": i, # same value as VBUP.VGPOS where VBUP.VBELN is vbeln
                "VGTYP": 'C',
                "VRKME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "WAERK": 'EUR',
                "WERKS": self.params['plant'],
                'FAKSP': None
            }
            self.tables['VBEP_json'][temp_vbeln] = {
                "BMENG": self.params['quantities'][i], # HACK all qauntities are the same as their confirmed queantities
                "EDATU": erdat,
                "ETENR": i,
                "MANDT": values.mandt,
                "MBDAT": None, # TODO MaterialAvailabilityDate edit later on shipping
                "MEINS": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "POSNR": i,
                "VBELN": self.vbeln,
                "WADAT": None, # TODO MaterialAvailabilityDate edit later on shipping,
            }


        self.record_flow( # HACK no quotation before
            erdat=erdat, 
            prev_vbeln=None, 
            prev_type=None, 
            next_vbeln=self.vbeln, 
            next_type='C'
        )
    
    def post_goods_issue(self, cpudt, usnam, atime, all_units=values.om_units):
        for i in range(len(self.params['matnrs'])): 
            self.tables['MSEG_json'][str(uuid.uuid4())] = {
                "BWART": '601',
                "BWTAR": None,
                "CPUDT_MKPF": cpudt,
                "CPUTM_MKPF": atime,
                "ERFME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "KDAUF": self.vbeln,
                "KDPOS": i,
                "LBKUM": round(self.params['prices'][i]*self.params['quantities'][i], 4),
                "LGORT": 'D', # TODO add custom value
                "LIFNR": None, # HACK only cosidering OM not Procurement
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "MBLNR": self.mblnr,
                "MEINS": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "MENGE": self.params['quantities'][i],
                "MJAHR": self.mjahr,
                "SHKZG": 'H', # Credit
                "SJAHR": self.mjahr,
                "SMBLN": self.mblnr,
                "SMBLP": i,
                "USNAM_MKPF": usnam,
                "VBELN_IM": self.likp_vbeln,
                "VBELP_IM": i,
                'WAERS': 'EUR',
                "WERKS": self.params['plant'],
                "ZEILE": i,
            }
            self.tables['EKBE_json'][str(uuid.uuid4())] = { # HACK every SO has 1:1 mapping form PO
                "BELNR": self.mblnr,
                "BUZEI": i,
                "GJAHR": self.mjahr,
                "MANDT": values.mandt,
                "MENGE": self.params['quantities'][i],
                "VGABE": 1, # Good Receipt
                "WAERS": 'EUR',
                "WRBTR": round(self.params['prices'][i]*self.params['quantities'][i], 4),
            }

            self.tables['MBEWH_json'][str(uuid.uuid4())] = {
                "BWKEY": 'VA01',
                "BWTAR": None,
                "LBKUM": (random.randint(500, 10000)),
                "LFGJA": self.fy,
                "LFMON": cpudt.strftime('%m'),
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "PEINH": 1,
                "SALK3": 99, #TO DO add custom value
                "STPRS": self.params['prices'][i],
                "VERPR": self.params['prices'][i],
                "VPRSV": 'V', # TODO add custom value
            }
     
        self.record_flow( 
            erdat=cpudt, 
            prev_vbeln=self.likp_vbeln, 
            prev_type='J', 
            next_vbeln=self.mblnr, 
            next_type='R'
        )
    
    def create_production_order_header(self, cpudt, ernam, atime, all_units=values.om_units):
        self.tables['AFKO_json'][str(uuid.uuid4())] = {
                "MANDT":values.mandt,
                "AUFNR":self.prod_order_number,
                "GSTRS": cpudt, #ScheduledStartTime
                "GSUZS": atime,
                "GLTRS": cpudt, #ScheduledFinishTime
                "GLUZS": atime,
                "GSTRI": cpudt, #StartTime
                "GSUZI": atime,
                "GLTRI": cpudt + timedelta(days=random.randint(5,15)), #FinishTime
                "GEUZI": atime,
            }
        self.tables['AUFK_json'][str(uuid.uuid4())] = {
                "MANDT": values.mandt,
                "AUFNR": self.prod_order_number,
                "ERNAM": ernam,
                "AUTYP": '10',
                "ERDAT": cpudt,
                "ERFZEIT": atime
            }

        for i in range(len(self.params['matnrs'])): 
            self.tables['AFPO_json'][str(uuid.uuid4())] = {
                "MANDT": values.mandt,
                "AUFNR": self.prod_order_number,
                "POSNR": i,
                "ETRMP": atime,
                "PSMNG": self.params['quantities'][i],
                "MEINS": self.unit,
                "WEMNG": self.params['quantities'][i],
                "DWERK": self.params['plant'],
                "MATNR": self.params['matnrs'][i],
                "XLOEK": None,
                "ELIKZ": None,
            }

            self.tables['MBEWH_json'][str(uuid.uuid4())] = {
                "BWKEY": 'VA01',
                "BWTAR": None,
                "LBKUM": (random.randint(500, 10000)),
                "LFGJA": self.fy,
                "LFMON": cpudt.strftime('%m'),
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "PEINH": 1,
                "SALK3": 99, #TO DO add custom value
                "STPRS": self.params['prices'][i],
                "VERPR": self.params['prices'][i],
                "VPRSV": 'V', # TODO add custom value
            }

            self.tables['MSEG_json'][str(uuid.uuid4())] = {
                "BWART": '101',
                "BWTAR": None,
                "CPUDT_MKPF": cpudt,
                "CPUTM_MKPF": atime,
                "ERFME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "KDAUF": self.vbeln,
                "KDPOS": i,
                "LBKUM": round(self.params['prices'][i]*self.params['quantities'][i], 4),
                "LGORT": 'D', # TODO add custom value
                "LIFNR": None, # HACK only cosidering OM not Procurement
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "MBLNR": self.mblnr,
                "MEINS": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "MENGE": self.params['quantities'][i],
                "MJAHR": self.mjahr,
                "SHKZG": 'S', # Credit
                "SJAHR": self.mjahr,
                "SMBLN": self.mblnr,
                "SMBLP": i,
                "USNAM_MKPF": ernam,
                "VBELN_IM": self.likp_vbeln,
                "VBELP_IM": i,
                'WAERS': 'EUR',
                "WERKS": self.params['plant'],
                "ZEILE": i,
            }

    def generate_delivery_document(
            self, 
            ernam, 
            erdat,
            planned_delivery_date,
            picking_date,
            delivery_date,
            confirmation_date,
            atime,
            all_units=values.om_units,
        ):
        self.tables['LIKP_json'][str(uuid.uuid4())] = {
            "BTGEW": 99, # TODO add custom value
            "ERDAT": erdat,
            "ERNAM": ernam,
            "ERZET": atime,
            "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
            "KODAT": picking_date,  #PickingDate
            "KOUHR": atime,         #PickingDate
            "KUNNR": self.params['kunnr'],
            "LFART": 'D', # TODO add custom value
            "LFDAT": delivery_date,
            "MANDT": values.mandt,
            "NTGEW": len(self.params['matnrs'])*99, # TODO add custom weight and assign accordingly to VBAP
            "PODAT": confirmation_date,
            "POTIM": atime,
            "VBELN": self.likp_vbeln,
            "VBTYP": 'J',
            "VOLEH": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
            "VOLUM": 99, # TODO add custom value
            "WADAT": planned_delivery_date,
        }



        for i in range(len(self.params['matnrs'])):
            self.tables['LIPS_json'][str(uuid.uuid4())] = {
                "ERDAT": erdat,
                "ERNAM": ernam,
                "ERZET": str(helpers.add_random_hours(1, atime)),
                "GEWEI": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "LFIMG": self.params['quantities'][i],
                "LGORT": 'D',#TODO add custom value
                "MANDT": values.mandt,
                "MATNR": self.params['matnrs'][i],
                "NTGEW": 99, # TODO add custom value
                "POSNR": i,
                "VBELN": self.likp_vbeln,
                "VGBEL": self.vbeln,
                "VGPOS": i,
                "VGTYP": 'C',
                "VOLEH": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "VOLUM": 99, # TODO add custom value
                "VRKME": all_units[random.choice(list(all_units.keys()))]['MSEHI'],
                "WERKS": self.params['plant']
            }
        self.record_flow( 
            erdat=erdat, 
            prev_vbeln=self.vbeln, 
            prev_type='C', 
            next_vbeln=self.likp_vbeln, 
            next_type='J'
        )
    
    # def begin_production_order(self, cpudt, usnam, atime):
    #     for i in range(len(self.params['matnrs'])):

    # def adjust_stock_plus(self, cpudt):
    #     for i in range(len(self.params['matnrs'])):
    #         self.tables['MBEWH_json'][str(uuid.uuid4())] = {
    #             "BWKEY": 'VA01'
    #             "BWTAR": None
    #             "LBKUM": random.randint(500, 1000)
    #             "LFGJA": self.fy
    #             "LFMON": cpudt.month
    #             "MANDT": values.mandt
    #             "MATNR": self.params['matnrs'][i]
    #             "PEINH": 1
    #             "SALK3": 99 #TO DO add custom value
    #             "STPRS": self.params['prices'][i],
    #             "VERPR": self.params['prices'][i],
    #             "VPRSV": 'V', # TODO add custom value
    #         }