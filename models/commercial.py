from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class Commercial(models.Model):
    _name = 'sales.commercial'
    _description = 'Commercial'

    name = fields.Char(string='Nom', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Téléphone')

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email:
                if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', record.email):
                    raise ValidationError(
                        "Veuillez saisir une adresse email valide."
                    )

    @api.constrains('phone')
    def _check_phone(self):
        for record in self:
            if record.phone:
                if not record.phone.isdigit():
                    raise ValidationError(
                        "Le numéro de téléphone doit contenir uniquement des chiffres."
                    )