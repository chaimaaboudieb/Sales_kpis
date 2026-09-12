# Sales KPI - Odoo Module

## 1. Présentation

**Sales KPI** est un module Odoo permettant de gérer les commerciaux et de suivre leurs performances mensuelles.

Le module est indépendant des modules **CRM** et **Sales** d'Odoo. Les données sont saisies manuellement.

### Fonctionnalités

* Gestion des commerciaux
* Saisie des performances mensuelles
* Calcul automatique des KPI
* Consultation des KPI dans Odoo
* API REST pour consulter et créer des KPI
* Authentification simple par API Key



## 2. Prérequis

* Odoo 18
* PostgreSQL
* Python
* Un environnement Windows/Linux avec Odoo fonctionnel



## 3. Installation

### Étape 1 : Copier le module

Copier le dossier `sales_kpi` dans le répertoire des addons personnalisés :


custom_addons/
└── sales_kpi/


### Étape 2 : Vérifier la configuration

Vérifier que le répertoire `custom_addons` est présent dans la configuration des addons d'Odoo.

### Étape 3 : Démarrer Odoo

Lancer le serveur Odoo.

### Étape 4 : Installer le module

Dans Odoo :

1. Aller dans **Apps**.
2. Activer le mode développeur si nécessaire.
3. Cliquer sur **Mettre à jour la liste des applications**.
4. Rechercher **Sales KPI**.
5. Cliquer sur **Installer**.



## 4. Utilisation

### Gestion des commerciaux

Le module permet d'enregistrer :

* Nom
* Email
* Téléphone

### Gestion des KPI mensuels

Pour chaque commercial, les informations suivantes peuvent être saisies :

* Commercial
* Mois
* Année
* Prospects contactés
* Rendez-vous obtenus
* Devis envoyés
* Ventes réalisées
* Chiffre d'affaires



## 5. Calcul automatique des KPI

### Taux de transformation


(Ventes réalisées / Prospects contactés) × 100


### Taux de conversion Prospect → Rendez-vous


(Rendez-vous obtenus / Prospects contactés) × 100


### Valeur moyenne d'une vente


Chiffre d'affaires / Ventes réalisées


Les divisions par zéro sont gérées automatiquement.



## 6. API REST

L'API permet de consulter et de créer des KPI via des requêtes HTTP.

### Authentification

L'API utilise une authentification simple par **Bearer API Key**.

La clé utilisée pour le projet est :


sales_kpi


Le header HTTP doit être :


Authorization: Bearer sales_kpi


## 7. GET - Liste des KPI

### Endpoint


GET http://localhost:8069/api/sales_kpi


### Commande


curl.exe -X GET "http://localhost:8069/api/sales_kpi" -H "Authorization: Bearer sales_kpi"


### Réponse

HTTP `200 OK`

L'API retourne la liste des KPI au format JSON.

### Exemple de réponse

```json
[
  {
    "id": 12,
    "commercial_id": 3,
    "month": "9",
    "year": 2026,
    "prospects_contacted": 120,
    "meetings_obtained": 35,
    "quotations_sent": 18,
    "sales_realized": 9,
    "revenue": 108000.0
  }
]


## 8. POST - Création d'un KPI

Cette partie permet de créer un nouvel enregistrement KPI via l'API REST.

### Méthode


POST


### Endpoint


http://localhost:8069/api/sales_kpi


### Headers

`
Authorization: Bearer sales_kpi
Content-Type: application/json


### Exemple de données JSON

json
{
  "commercial_id": 1,
  "month": 10,
  "year": 2026,
  "prospects_contacted": 100,
  "meetings_obtained": 30,
  "quotations_sent": 20,
  "sales_realized": 5,
  "revenue": 60000
}


### Commande PowerShell

Pour éviter les problèmes de formatage du JSON dans PowerShell, créer un fichier `post.json` :

json
{
  "commercial_id": 1,
  "month": 10,
  "year": 2026,
  "prospects_contacted": 100,
  "meetings_obtained": 30,
  "quotations_sent": 20,
  "sales_realized": 5,
  "revenue": 60000
}


Puis exécuter :


curl.exe -X POST "http://localhost:8069/api/sales_kpi" -H "Authorization: Bearer sales_kpi" -H "Content-Type: application/json" --data-binary "@post.json"
```

### Réponse attendue

HTTP `201 Created`

json
{
  "success": true,
  "message": "KPI créé avec succès",
  "data": {
    "id": 14,
    "commercial_id": 1,
    "commercial": "Nom du commercial",
    "month": "10",
    "year": 2026,
    "prospects_contacted": 100,
    "meetings_obtained": 30,
    "quotations_sent": 20,
    "sales_realized": 5,
    "revenue": 60000.0,
    "transformation_rate": 5.0,
    "prospect_to_meeting_rate": 30.0,
    "average_sale_value": 12000.0
  }
}


### Erreur d'authentification

Si la clé API est absente ou incorrecte, l'API retourne :

json
{
  "success": false,
  "error": "Unauthorized"
}


avec le statut HTTP `401 Unauthorized`.



## 9. Captures d'écran

Les captures d'écran du projet présentent :

1. Le menu **Sales KPI**
2. La liste des commerciaux
3. Le formulaire d'un commercial
4. La liste des KPI mensuels
5. Le formulaire d'un KPI avec les indicateurs calculés automatiquement
6. Un exemple de requête **GET**
7. Un exemple de requête **POST**



## 10. Structure du projet


sales_kpi/
│
├── README.md
├── __init__.py
├── __manifest__.py
│
├── controllers/
│   ├── __init__.py
│   └── api.py
│
├── models/
│   ├── __init__.py
│   ├── commercial.py
│   └── sales_kpi.py
│
├── security/
│   └── ir.model.access.csv
│
└── views/
    ├── commercial_views.xml
    ├── sales_kpi_views.xml
    └── menu.xml




## 11. Auteur

Projet réalisé par **Chaimaa Boudieb** dans le cadre de l'exercice technique proposé par **Transformatek**.
