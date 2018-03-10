# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

ones = ('', 'BİR', 'İKİ', 'Üç', 'DÖRT', 'BEŞ', 'ALTI', 'YEDİ', 'SEKİZ', 'DOKUZ')
tens = ('', 'ON', 'YİRMİ', 'OTUZ', 'KIRK', 'ELLİ', 'ALTMIŞ', 'YETMİŞ', 'SEKSEN', 'DOKSAN')
thousands = ('KATRİLYON', 'TRİLYON', 'MİLYAR', 'MİLYON', 'BİN', '')
groupcount = 6
def amount_to_text_tr(number):
    
		
    stringamount = str(format(number,'.2f'))

    lira = stringamount[:len(stringamount)-3]

    
    kurus = stringamount[-2:]

    text = '--'
    lira = lira.rjust(groupcount * 3, '0')



    for i in range(0, groupcount *3, 3):
        grupdegeri = ''
        if lira[i] != '0':
            grupdegeri += ones[int(lira[i])] + 'YÜZ'
            if grupdegeri == 'BİRYÜZ':
                grupdegeri = 'YÜZ'
        grupdegeri += tens[int(lira[i + 1])]
        grupdegeri += ones[int(lira[i + 2])]
        if grupdegeri != '':
            grupdegeri += thousands[int(i / 3)]
            if grupdegeri == 'BİRBİN':
                grupdegeri = 'BİN'
        text += grupdegeri
    print text
    print grupdegeri
    if text != '':
        text += ' TL '
    textLength = len(text)
    if kurus[0] != '0':
        text+= tens[int(kurus[0])]
    if kurus[1] != '0':
        text+= ones[int(kurus[1])]
    if len(text)> textLength:
        text += ' KURUŞ'
    else:
        text += ' SIFIR KURUŞ'
    return text+'--'


class AccountInvoice(models.Model):
    _inherit = "account.invoice"
   
    @api.one
    @api.depends('amount_total')
    def _amount_in_words(self):
        self.amount_to_text = amount_to_text_tr(self.amount_total)

    amount_to_text = fields.Text(string='YALNIZ',
        store=True, readonly=True, compute='_amount_in_words')

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.one
    @api.depends('amount_total')
    def _amount_in_words(self):
        self.amount_to_text = amount_to_text_tr(self.amount_total)
    
    
    amount_to_text = fields.Text(string='YALNIZ',
        store=True, readonly=True, compute='_amount_in_words')
