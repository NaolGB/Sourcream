from datetime import datetime, timedelta
import uuid
import values, helpers
import random
import pandas as pd
import numpy as np

class Materials:
    def __init__(self, id: uuid.UUID, name: str, availability: float, price: float) -> None:
        self.id = id
        self.name = name
        self.availability = availability
        self.price = price

class SalesOrderItem:
    def __init__(self, vbeln, posnr, kwmeng, matnr, netwr, material) -> None:
        self.mandt = values.mandt
        self.vbeln = vbeln
        self.posnr = posnr
        self.kwmeng = kwmeng
        self.matnr = matnr
        self.netwr = netwr
        self.material = material

class Users:
    def __init__(self, name, user_type) -> None:
        self.name = name
        self.user_type = user_type

class Customer:
    def __init__(self, id, created_at, credit_worthyness) -> None:
        self.id = id
        self.created_at = created_at
        self.credit_worthyness = credit_worthyness

class SalesOrder:
    def __init__(self, users, companies, materials) -> None:
        self.vbak_temp_list = []
        self.vbap_temp_list = []
        self.likp_temp_list = []
        self.lips_temp_list = []
        self.cdhdr_changes_temp_list = []
        self.cdpos_changes_temp_list = []
        self.vbuk_temp_list = []
        self.mkpf_temp_list = []
        self.mseg_temp_list = []
        self.vbrk_temp_list = []
        self.vbrp_temp_list = []

        self.mandt = values.mandt
        self.vbeln = uuid.uuid4()

        cred_worthy = np.array([c.credit_worthyness for c in companies])
        cred_worthy = cred_worthy / np.sum(cred_worthy)
        rand_company_index = np.random.choice(len(cred_worthy), p=cred_worthy)
        self.company = companies[rand_company_index]
        self.erdat = helpers.generate_random_datetime(self.company.created_at, values.times['salesorder_create_end'])
        self.ernam = random.choice(users)
        self.kunnr = self.company.id
        self.netwr = 0
        self.vsbed = random.choice(values.shipping_conditions)
        self.faksk = pd.NA

        self.vbaps = []
        self.vbuk = self.vbuk = [values.mandt, self.vbeln, 'SALESORDERCREATED', pd.NA, self.erdat, 'C']

        self.latest_activity_at = self.erdat
        self.has_billing_block = False
        
        # Create Sales order 
        self.create_vbap_rows(num_items=(random.randint(5, 15)), materials=materials)

        # transition matrix
        self.tmi = {
            'generate_delivery_doc': 0, 
            'release_delivery': 1, 
            'set_billing_block': 2, 
            'ship_goods': 3, 
            'remove_billing_block': 4, 
            'send_invoice': 5, 
            'cancel_order': 6, 
            'receive_delivery_confirmation': 7, 
            'return_goods': 8, 
            'clear_invoice': 9,
            'end': 10,
        }
        self.transition_matrix = np.array([
        #   [gdd., rdel, sbb., shig, rbb., sniv, cano, rdcn, retg, cinv, end.],
            [0.01, 0.80, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00], # generate delivery doc
            [0.00, 0.01, 0.01, 0.80, 0.00, 0.01, 0.00, 0.00, 0.00, 0.00, 0.00], # release delivery
            [0.00, 0.05, 0.00, 0.00, 0.80, 0.00, 0.00, 0.00, 0.01, 0.01, 0.00], # set billing block
            [0.00, 0.00, 0.01, 0.00, 0.00, 0.80, 0.00, 0.00, 0.00, 0.00, 0.00], # ship goods
            [0.00, 0.80, 0.05, 0.01, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00, 0.00], # remove billing block
            [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.80, 0.00, 0.00, 0.00], # send invoice
            [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00], # cancel order
            [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.80, 0.00], # receive delivery confirmation
            [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.20, 0.00, 0.80], # return goods
            [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00], # clear invoice
            [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00]  # end
        ])


    def update_latest_activity_time(self, new_latest_time):
        if self.latest_activity_at < new_latest_time:
            self.latest_activity_at = new_latest_time

    def create_vbap_rows(self, num_items, materials):
        # Activity: Create sales order - item
        total_price = 0
        for j in range(num_items):
            availabilities = np.array([m.availability for m in materials])
            availabilities = availabilities / np.sum(availabilities)
            rand_material_index = np.random.choice(len(availabilities), p=availabilities)
            rand_material = materials[rand_material_index]

            quantity = random.randint(25, 150)

            # add the material to vbap table
            self.vbap_temp_list.append([values.mandt, self.vbeln, j, quantity, rand_material.id, quantity*rand_material.price])
            total_price += (quantity*rand_material.price)

            # add vbap to vbak object
            self.vbaps.append(SalesOrderItem(self.vbeln, j, quantity, rand_material.id, (quantity*rand_material.price), material=rand_material))

        self.netwr = total_price

    def generate_delivery_doc(self):
        """
        Activity: Generate delivery document
        affected by:
            - material availability
            - checking and cofirming price and other order details
        affects:
            - cycle time
        """
        # set random delivery times
        planned_delivery_dt = self.latest_activity_at + helpers.UPTO_WEEK()
        actual_delivery_dt = planned_delivery_dt if random.uniform(0, 1) < 0.5 else planned_delivery_dt + helpers.UPTO_WEEK()

        # update cycle time by material avialability
        avg_mat_availability = sum([SOi.material.availability for SOi in self.vbaps]) / len([SOi.material.availability for SOi in self.vbaps])
        if avg_mat_availability < 0.6:
            delivery_doc_created_at = self.latest_activity_at + helpers.UPTO_MONTH()
        else:
            delivery_doc_created_at = self.latest_activity_at + helpers.UPTO_WEEK()

        # update billing block probability
        if self.company.credit_worthyness <= 0.4:
            self.transition_matrix[self.tmi['generate_delivery_doc'], self.tmi['set_billing_block']] = 0.6

        # assign user
        if random.uniform(0, 1) < 0.24: # 24% automation rate
            user = 'BATCH_JOB'
        else:
            user = random.choice(list(values.users))
        
        # impact of user type
        if user == 'BATCH_JOB':
            delivery_doc_created_at =  self.latest_activity_at + helpers.UPTO_HOUR()
        else:
            delivery_doc_created_at =  self.latest_activity_at + helpers.UPTO_DAY()
        
        self.update_latest_activity_time(new_latest_time=delivery_doc_created_at)


        # cycle time
        cycle_time = (self.latest_activity_at - self.erdat).days
        if cycle_time >= 15:
            self.transition_matrix[self.tmi['generate_delivery_doc'], self.tmi['return_goods']] = 0.60
            self.transition_matrix[self.tmi['generate_delivery_doc'], self.tmi['release_delivery']] = 0.10
            self.transition_matrix[self.tmi['generate_delivery_doc'], self.tmi['cancel_order']] = 0.30

        rand_likp_id = uuid.uuid4()
        self.likp_temp_list.append([values.mandt, rand_likp_id, planned_delivery_dt, actual_delivery_dt, delivery_doc_created_at, user])
        
        self.generate_delivery_doc_item(likp_id=rand_likp_id)
    
    def generate_delivery_doc_item(self, likp_id: uuid.UUID):
        # Activity: Generate delivery document - item
        for vbap_elem in self.vbaps:
            self.lips_temp_list.append([values.mandt, likp_id, self.vbeln, vbap_elem.posnr])

    def release_delivery(self):
        # Activity: Release delivery
        rand_changenr = uuid.uuid4()
        rand_usr = random.choice(list(values.users))

        # apply the effect of material availability and user tyoe
        avg_mat_availability = sum([SOi.material.availability for SOi in self.vbaps]) / len([SOi.material.availability for SOi in self.vbaps])
        if avg_mat_availability < 0.4:
            delivery_released_at = self.latest_activity_at + helpers.UPTO_MONTH()
        else:
            delivery_released_at = self.latest_activity_at + helpers.UPTO_WEEK()

        self.update_latest_activity_time(new_latest_time=delivery_released_at)

        # cycle time
        cycle_time = (self.latest_activity_at - self.erdat).days
        if cycle_time >= 15:
            self.transition_matrix[self.tmi['release_delivery'], self.tmi['return_goods']] = 0.60
            self.transition_matrix[self.tmi['release_delivery'], self.tmi['ship_goods']] = 0.10
            self.transition_matrix[self.tmi['release_delivery'], self.tmi['cancel_order']] = 0.30
        
        # record change
        self.cdhdr_changes_temp_list.append([values.mandt, 'DELIVERY', self.vbeln, rand_changenr, rand_usr, delivery_released_at])
        self.cdpos_changes_temp_list.append([values.mandt, rand_changenr, 'VBUK', 'LFSTK', pd.NA, 'DELIVERYRELEASED'])
        
        self.vbuk = [values.mandt, self.vbeln, 'DELIVERYRELEASED', pd.NA, delivery_released_at, 'C']

    def ship_goods(self):
        # Activity: Ship goods
        rand_mblnr = uuid.uuid4()
        goods_shipped_at = self.latest_activity_at + helpers.UPTO_WEEK()
        self.update_latest_activity_time(new_latest_time=goods_shipped_at)

        # assign user
        if random.uniform(0, 1) < 0.3: # 30% automation rate
            user = 'BATCH_JOB'
        else:
            user = random.choice(list(values.users))

        self.mkpf_temp_list.append([values.mandt, rand_mblnr, 'GOODSISSUE', goods_shipped_at, user])

        # cycle time
        cycle_time = (self.latest_activity_at - self.erdat).days
        if cycle_time >= 15:
            self.transition_matrix[self.tmi['ship_goods'], self.tmi['return_goods']] = 0.60
            self.transition_matrix[self.tmi['ship_goods'], self.tmi['send_invoice']] = 0.10
            self.transition_matrix[self.tmi['ship_goods'], self.tmi['cancel_order']] = 0.30
        
        for vbap_elem in self.vbaps:
            self.mseg_temp_list.append([values.mandt, rand_mblnr, self.vbeln, vbap_elem.posnr])

    def send_invoice(self):
        # assign user
        if random.uniform(0, 1) < 0.3: # 30% automation rate
            user = 'BATCH_JOB'
        else:
            user = random.choice(list(values.users))

        # impact of user type
        if user == 'BATCH_JOB':
            invoice_sent_at =  self.latest_activity_at + helpers.UPTO_HOUR()
        else:
            invoice_sent_at =  self.latest_activity_at + helpers.UPTO_DAY()
        self.update_latest_activity_time(new_latest_time=invoice_sent_at)

        # cycle time
        cycle_time = (self.latest_activity_at - self.erdat).days
        if cycle_time >= 15:
            self.transition_matrix[self.tmi['send_invoice'], self.tmi['return_goods']] = 0.60
            self.transition_matrix[self.tmi['send_invoice'], self.tmi['clear_invoice']] = 0.10
            self.transition_matrix[self.tmi['send_invoice'], self.tmi['cancel_order']] = 0.30

        rand_vbrk_id = uuid.uuid4()
        self.vbrk_temp_list.append([values.mandt, rand_vbrk_id, 'INVOICE', user, invoice_sent_at])
        
        self.send_invoice_items(vbrk_id=rand_vbrk_id)

    def send_invoice_items(self, vbrk_id: uuid.UUID):
        for vbap_elem in self.vbaps:
            self.vbrp_temp_list.append([values.mandt, vbrk_id, self.vbeln, vbap_elem.posnr])
    
    def receive_delivery_confirmation(self):
        # Activity: Recieve delivery confirmation
        rand_changenr = uuid.uuid4()
        rand_usr = random.choice(list(values.users))

        delivery_confirmed_at = self.latest_activity_at + helpers.UPTO_WEEK()
        self.update_latest_activity_time(new_latest_time=delivery_confirmed_at)

        self.vbuk = [values.mandt, self.vbeln, 'DELIVERYCONFIRMED', pd.NA, delivery_confirmed_at, 'C']

        # record change
        self.cdhdr_changes_temp_list.append([values.mandt, 'DELIVERY', self.vbeln, rand_changenr, rand_usr, delivery_confirmed_at])
        self.cdpos_changes_temp_list.append([values.mandt, rand_changenr, 'VBUK', 'LFSTK', 'DELIVERYRELEASED', 'DELIVERYCONFIRMED'])

        # throughput time
        throughput_time = (self.latest_activity_at - self.erdat).days
        if throughput_time >= 20:
            self.transition_matrix[self.tmi['receive_delivery_confirmation'], self.tmi['return_goods']] = 0.60
            self.transition_matrix[self.tmi['receive_delivery_confirmation'], self.tmi['clear_invoice']] = 0.10
            self.transition_matrix[self.tmi['receive_delivery_confirmation'], self.tmi['cancel_order']] = 0.30

    def clear_invoice(self):
        # Activity: Clear invoice
        rand_changenr = uuid.uuid4()
        rand_usr = random.choice(list(values.users))

        # DSO based on credit worthyness of the company
        invoice_cleared_at = self.latest_activity_at + timedelta(days=int(10/self.company.credit_worthyness))
        self.update_latest_activity_time(new_latest_time=invoice_cleared_at)

        self.vbuk = [values.mandt, self.vbeln, 'DELIVERYCONFIRMED', 'INVOICECLEARED', invoice_cleared_at, 'C']

        # record change
        self.cdhdr_changes_temp_list.append([values.mandt, 'BILLING', self.vbeln, rand_changenr, rand_usr, invoice_cleared_at])
        self.cdpos_changes_temp_list.append([values.mandt, rand_changenr, 'VBUK', 'FKSTK', pd.NA, 'INVOICECLEARED'])

class BillingDeviation:
    def __init__(self, vbak: SalesOrder) -> None:
        self.vbak = vbak
        
    def set_billing_block(self):
        # Activity: Set billing block
        self.vbak.faksk = 'BILLINGBLOCK'

        rand_changenr = uuid.uuid4()

        # assign user
        if random.uniform(0, 1) < 0.6: 
            user = 'BATCH_JOB'
        else:
            user = random.choice(list(values.users))

        # impact of user type
        if user == 'BATCH_JOB':
            billing_block_set_at =  self.vbak.latest_activity_at + helpers.UPTO_HOUR()
        else:
            billing_block_set_at =  self.vbak.latest_activity_at + helpers.UPTO_DAY()

        # increase cycle time
        self.vbak.update_latest_activity_time(new_latest_time=billing_block_set_at + helpers.UPTO_MONTH())

        self.vbak.cdhdr_changes_temp_list.append([values.mandt, 'BILLING', self.vbak.vbeln, rand_changenr, user, billing_block_set_at])
        self.vbak.cdpos_changes_temp_list.append([values.mandt, rand_changenr, 'VBAK', 'FAKSK', pd.NA, 'BILLINGBLOCK'])
        
        self.vbak.has_billing_block = True

    def remove_billing_block(self):
        # Activity: Remove billing block
        self.vbak.faksk = pd.NA

        rand_changenr = uuid.uuid4()
        rand_usr = random.choice(list(values.users))

        billing_block_removed_at = self.vbak.latest_activity_at + helpers.UPTO_WEEK()
        self.vbak.update_latest_activity_time(new_latest_time=billing_block_removed_at)

        self.vbak.cdhdr_changes_temp_list.append([values.mandt, 'BILLING', self.vbak.vbeln, rand_changenr, rand_usr, billing_block_removed_at])
        self.vbak.cdpos_changes_temp_list.append([values.mandt, rand_changenr, 'VBAK', 'FAKSK', 'BILLINGBLOCK', pd.NA])

class CancelOrReturn:
    def __init__(self, vbak) -> None:
        self.vbak = vbak
    
    def cancel_order(self):
        # Activity: Cancel order
        rand_changenr = uuid.uuid4()
        rand_usr = random.choice(list(values.users))

        sd_cancelled_at = self.vbak.latest_activity_at + helpers.UPTO_DAY()
        self.vbak.update_latest_activity_time(new_latest_time=sd_cancelled_at)

        self.vbak.cdhdr_changes_temp_list.append([values.mandt, 'SALESORDER', self.vbak.vbeln, rand_changenr, rand_usr, sd_cancelled_at])
        self.vbak.cdpos_changes_temp_list.append([values.mandt, rand_changenr, 'VBUK', 'VBTYP', self.vbak.vbuk[-1], 'h'])
        self.vbak.vbuk[-1] = 'h'

    def return_goods(self):
        # Activity: Return goods
        rand_changenr = uuid.uuid4()
        rand_usr = random.choice(list(values.users))

        sd_returned_at = self.vbak.latest_activity_at + helpers.UPTO_MONTH()
        self.vbak.update_latest_activity_time(new_latest_time=sd_returned_at)

        self.vbak.cdhdr_changes_temp_list.append([values.mandt, 'SALESORDER', self.vbak.vbeln, rand_changenr, rand_usr, sd_returned_at])
        self.vbak.cdpos_changes_temp_list.append([values.mandt, rand_changenr, 'VBUK', 'VBTYP', self.vbak.vbuk[-1], 'H'])
        self.vbak.vbuk[-1] = 'H'