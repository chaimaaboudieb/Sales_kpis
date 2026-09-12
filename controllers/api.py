
import json

from odoo import http
from odoo.http import request


# ============================================================
# API KEY
# ============================================================

API_KEY = 'sales_kpi'


class SalesKpiAPI(http.Controller):

    # ========================================================
    # AUTHENTIFICATION
    # ========================================================

    def _check_api_key(self):
        """
        Vérifie si la clé API envoyée dans le header
        Authorization correspond à la clé définie.
        """

        auth_header = request.httprequest.headers.get('Authorization')

        return auth_header == f'Bearer {API_KEY}'

    # ========================================================
    # GET - CONSULTER LES KPI
    # ========================================================

    @http.route(
        '/api/sales_kpi',
        type='http',
        auth='none',
        methods=['GET'],
        csrf=False
    )
    def get_kpis(self, **kwargs):

        # Vérification de l'API Key
        if not self._check_api_key():
            return request.make_response(
                json.dumps({
                    'success': False,
                    'error': 'Unauthorized'
                }),
                headers=[
                    ('Content-Type', 'application/json')
                ],
                status=401
            )

        # Récupération des KPI depuis Odoo
        kpis = request.env['sales.kpi'].sudo().search([])

        result = []

        for kpi in kpis:

            result.append({
                'id': kpi.id,

                'commercial_id': (
                    kpi.commercial_id.id
                    if kpi.commercial_id
                    else None
                ),

                'commercial': (
                    kpi.commercial_id.name
                    if kpi.commercial_id
                    else None
                ),

                'month': kpi.month,
                'year': kpi.year,

                'prospects_contacted': kpi.prospects_contacted,
                'meetings_obtained': kpi.meetings_obtained,
                'quotations_sent': kpi.quotations_sent,
                'sales_realized': kpi.sales_realized,
                'revenue': kpi.revenue,

                # KPI calculés automatiquement
                'transformation_rate': kpi.transformation_rate,
                'prospect_to_meeting_rate': kpi.prospect_to_meeting_rate,
                'average_sale_value': kpi.average_sale_value,
            })

        # Retour JSON
        return request.make_response(
            json.dumps(result),
            headers=[
                ('Content-Type', 'application/json')
            ],
            status=200
        )

    # ========================================================
    # POST - CREER UN KPI
    # ========================================================

    @http.route(
        '/api/sales_kpi',
        type='http',
        auth='none',
        methods=['POST'],
        csrf=False
    )
    def create_kpi(self, **kwargs):

        # Vérification de l'API Key
        if not self._check_api_key():
            return request.make_response(
                json.dumps({
                    'success': False,
                    'error': 'Unauthorized'
                }),
                headers=[
                    ('Content-Type', 'application/json')
                ],
                status=401
            )

        try:

            # Lire le JSON envoyé par le client
            data = json.loads(
                request.httprequest.data.decode('utf-8')
            )

            # Champs obligatoires
            required_fields = [
                'commercial_id',
                'month',
                'year',
            ]

            for field in required_fields:

                if field not in data:

                    return request.make_response(
                        json.dumps({
                            'success': False,
                            'error': (
                                f'Champ obligatoire manquant : {field}'
                            )
                        }),
                        headers=[
                            ('Content-Type', 'application/json')
                        ],
                        status=400
                    )

            # Création du KPI dans Odoo
            kpi = request.env['sales.kpi'].sudo().create({

                'commercial_id': data['commercial_id'],

                'month': str(data['month']),

                'year': data['year'],

                'prospects_contacted': data.get(
                    'prospects_contacted',
                    0
                ),

                'meetings_obtained': data.get(
                    'meetings_obtained',
                    0
                ),

                'quotations_sent': data.get(
                    'quotations_sent',
                    0
                ),

                'sales_realized': data.get(
                    'sales_realized',
                    0
                ),

                'revenue': data.get(
                    'revenue',
                    0.0
                ),
            })

            # Réponse après création
            response = {

                'success': True,

                'message': 'KPI créé avec succès',

                'data': {

                    'id': kpi.id,

                    'commercial_id': (
                        kpi.commercial_id.id
                        if kpi.commercial_id
                        else None
                    ),

                    'commercial': (
                        kpi.commercial_id.name
                        if kpi.commercial_id
                        else None
                    ),

                    'month': kpi.month,
                    'year': kpi.year,

                    'prospects_contacted':
                        kpi.prospects_contacted,

                    'meetings_obtained':
                        kpi.meetings_obtained,

                    'quotations_sent':
                        kpi.quotations_sent,

                    'sales_realized':
                        kpi.sales_realized,

                    'revenue':
                        kpi.revenue,

                    # KPI calculés automatiquement
                    'transformation_rate':
                        kpi.transformation_rate,

                    'prospect_to_meeting_rate':
                        kpi.prospect_to_meeting_rate,

                    'average_sale_value':
                        kpi.average_sale_value,
                }
            }

            return request.make_response(
                json.dumps(response),
                headers=[
                    ('Content-Type', 'application/json')
                ],
                status=201
            )

        # JSON invalide
        except json.JSONDecodeError:

            return request.make_response(
                json.dumps({
                    'success': False,
                    'error': 'JSON invalide'
                }),
                headers=[
                    ('Content-Type', 'application/json')
                ],
                status=400
            )

        # Autre erreur
        except Exception as e:

            return request.make_response(
                json.dumps({
                    'success': False,
                    'error': str(e)
                }),
                headers=[
                    ('Content-Type', 'application/json')
                ],
                status=500
            )
