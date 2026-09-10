# Sales KPI - Odoo Module

## 1. Présentation

Sales KPI est un module Odoo permettant de gérer les commerciaux et de suivre leurs performances mensuelles.

Le module est indépendant des modules CRM et Sales d'Odoo. Les données sont saisies manuellement.

### Fonctionnalités

* Gestion des commerciaux
* Saisie des performances mensuelles
* Calcul automatique des KPI
* Consultation des KPI dans Odoo
* API REST pour consulter et créer des KPI

---

## 2. Prérequis

* Odoo
* PostgreSQL
* Python
* Un environnement Windows/Linux avec Odoo fonctionnel

---

## 3. Installation

### Étape 1 : Copier le module

Copier le dossier `sales_kpi` dans le répertoire des addons personnalisés :

```text
custom_addons/
└── sales_kpi/
```

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

---

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

---

## 5. Calcul automatique des KPI

### Taux de transformation

```text
(Ventes réalisées / Prospects contactés) × 100
```

### Taux de conversion Prospect → Rendez-vous

```text
(Rendez-vous obtenus / Prospects contactés) × 100
```

### Valeur moyenne d'une vente

```text
Chiffre d'affaires / Ventes réalisées
```

Les divisions par zéro sont gérées automatiquement.

---

## 6. API REST

### GET - Liste des KPI

**Endpoint :**

```text
http://localhost:8069/api/sales_kpi
```

**Commande :**

```bash
curl http://localhost:8069/api/sales_kpi
```

**Réponse attendue :**

```text
HTTP 200 OK
```

L'API retourne la liste des KPI au format JSON.

### Exemple de réponse

```json
[
  {
    "id": 3,
    "commercial_id": 2,
    "commercial": "Ahmed",
    "month": "5",
    "year": 2026,
    "prospects_contacted": 0,
    "meetings_obtained": 0,
    "quotations_sent": 0,
    "sales_realized": 0,
    "revenue": 0.0
  }
]
```

---

## 7. POST - Création d'un KPI

Cette partie permet de créer un nouvel enregistrement KPI via l'API REST.

**Méthode :**

```text
POST
```

**Endpoint :**

```text
http://localhost:8069/api/sales_kpi
```

> La commande `curl` exacte dépend de la structure définie dans `controllers/api.py`.

---

## 8. Captures d'écran

Les captures d'écran du projet présentent :

1. Le menu **Sales KPI**.
2. La liste des commerciaux.
3. Le formulaire d'un commercial.
4. La liste des KPI mensuels.
5. Le formulaire d'un KPI avec les indicateurs calculés automatiquement.

---

## 9. Structure du projet

```text
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
```

---

## 10. Auteur

Projet réalisé dans le cadre de l'exercice technique proposé par Transformatek.
