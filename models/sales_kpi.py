from odoo import api, fields, models


class SalesKPI(models.Model):
    _name = 'sales.kpi'
    _description = 'KPI Mensuel Commercial'
    _order = 'year desc, month desc, commercial_id'

    commercial_id = fields.Many2one(
        'sales.commercial',
        string='Commercial',
        required=True,
        ondelete='cascade',
    )

    month = fields.Selection(
        [
            ('1', 'Janvier'),
            ('2', 'Février'),
            ('3', 'Mars'),
            ('4', 'Avril'),
            ('5', 'Mai'),
            ('6', 'Juin'),
            ('7', 'Juillet'),
            ('8', 'Août'),
            ('9', 'Septembre'),
            ('10', 'Octobre'),
            ('11', 'Novembre'),
            ('12', 'Décembre'),
        ],
        string='Mois',
        required=True,
    )

    year = fields.Integer(
        string='Année',
        required=True,
        default=lambda self: fields.Date.today().year,
    )

    prospects_contacted = fields.Integer(
        string='Prospects contactés',
        default=0,
    )

    meetings_obtained = fields.Integer(
        string='Rendez-vous obtenus',
        default=0,
    )

    quotations_sent = fields.Integer(
        string='Devis envoyés',
        default=0,
    )

    sales_realized = fields.Integer(
        string='Ventes réalisées',
        default=0,
    )

    revenue = fields.Float(
        string="Chiffre d'affaires",
        default=0.0,
    )

    transformation_rate = fields.Float(
        string='Taux de transformation (%)',
        compute='_compute_kpis',
        store=True,
    )

    prospect_to_meeting_rate = fields.Float(
        string='Conversion Prospect → RDV (%)',
        compute='_compute_kpis',
        store=True,
    )

    average_sale_value = fields.Float(
        string="Valeur moyenne d'une vente",
        compute='_compute_kpis',
        store=True,
    )

    @api.depends(
        'prospects_contacted',
        'meetings_obtained',
        'sales_realized',
        'revenue',
    )
    def _compute_kpis(self):
        for record in self:

            # Taux de transformation Prospect → Vente
            record.transformation_rate = (
                record.sales_realized
                / record.prospects_contacted
                * 100
                if record.prospects_contacted
                else 0.0
            )

            # Taux de conversion Prospect → Rendez-vous
            record.prospect_to_meeting_rate = (
                record.meetings_obtained
                / record.prospects_contacted
                * 100
                if record.prospects_contacted
                else 0.0
            )

            # Valeur moyenne d'une vente
            record.average_sale_value = (
                record.revenue
                / record.sales_realized
                if record.sales_realized
                else 0.0
            )

    _sql_constraints = [
        (
            'unique_commercial_period',
            'unique(commercial_id, month, year)',
            'Un seul KPI peut être enregistré pour un commercial, un mois et une année.',
        ),
    ]