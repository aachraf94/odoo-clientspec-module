# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class clientspec(models.Model):
#     _name = 'clientspec.clientspec'

#     name = fields.Char()
class Client(models.Model):
    _name = 'clientspec.client'
    _description = "Client grossiste"

    name = fields.Char(string="Nom_Client", required=True)    
    
    isLocal = fields.Boolean(string="Client local", required=True)
    client_type = fields.Selection([("particulier", "Particulier"), ("public", "Une entreprise publique"), ("private", "Une entreprise privée")], string="Type Client")
    commande_ids = fields.One2many(
        'clientspec.commande', 'client_id', string="Commandes")

class Commande(models.Model):
    _name = 'clientspec.commande'
    _description = "Commandes speciales"

    name = fields.Char(string="IdCommande", required=True)
    date = fields.Date()
    price = fields.Float(digits=(6, 2), help="le prix")    
    client_id = fields.Many2many('clientspec.client',
        ondelete='cascade', string="Client", required=True)

class Assurance(models.Model):
    _name = 'clientspec.assurance'
    _description = "assurance client grossiste"

    label = fields.Char(string="IdAssurance", required=True)
    dateSouscription = fields.Date()
    piece = fields.Binary()    
    client_id = fields.Many2many('clientspec.client',
        ondelete='cascade', string="Client", required=True)



# # one2one relation
# from odoo import models, fields

# class ModelA(models.Model):
#     _name = 'model.a'
#     _description = 'Model A'

#     name = fields.Char(string='Name')
#     model_b_id = fields.Many2one('model.b', string='Model B', ondelete='cascade', unique=True)

# class ModelB(models.Model):
#     _name = 'model.b'
#     _description = 'Model B'

#     name = fields.Char(string='Name')
#     model_a_id = fields.One2many('model.a', 'model_b_id', string='Model A')

