# TODO: Remplacer par des vrais modèles Django
# Fichier temporaire pour le POC - Données de démonstration

# ============================================================================
# CLIENTS (30 clients pour tester la pagination)
# ============================================================================

ALL_CLIENTS = [
    {'id': 1, 'code': '000000', 'nom': 'PROSPECT', 'ville': '-', 'commercial': '-', 'famille': '-', 'actif': True},
    {'id': 2, 'code': '000006', 'nom': 'GRAINOCEAN INTERNATIONAL', 'ville': 'LA ROCHELLE CDX', 'commercial': '-',
     'famille': 'Industrie', 'actif': True},
    {'id': 3, 'code': '000015', 'nom': 'BAUDELET SAS', 'ville': 'BLARINGHEM', 'commercial': '-', 'famille': 'PME',
     'actif': True},
    {'id': 4, 'code': '000024', 'nom': 'TPF UTILITIES FRANCE', 'ville': 'FRETIN', 'commercial': '-',
     'famille': 'Grand Compte', 'actif': True},
    {'id': 5, 'code': '000025', 'nom': 'CONSTELLIUM MONTREUIL JUIGNE', 'ville': 'MONTREUIL JUIGNE', 'commercial': '-',
     'famille': 'Industrie', 'actif': False},
    {'id': 6, 'code': '000031', 'nom': 'SOFISE', 'ville': 'VENISSIEUX', 'commercial': '-', 'famille': '-',
     'actif': True},
    {'id': 7, 'code': '000036', 'nom': 'WDL S.A.S', 'ville': 'LILLE CEDEX', 'commercial': '-', 'famille': 'PME',
     'actif': True},
    {'id': 8, 'code': '000042', 'nom': 'NWL FRANCE SERVICES SAS', 'ville': 'SAINT HERBLAIN', 'commercial': '-',
     'famille': '-', 'actif': True},
    {'id': 9, 'code': '000044', 'nom': 'COS ARTISAN', 'ville': 'ST GERMAIN S/MORIN', 'commercial': '-',
     'famille': 'Artisan', 'actif': True},
    {'id': 10, 'code': '000049', 'nom': 'CARPENTIER PREUX', 'ville': 'CAUDRY', 'commercial': 'Aurélien VANPARYS',
     'famille': '-', 'actif': True},
    {'id': 11, 'code': '000051', 'nom': 'DUO EMBALLAGES', 'ville': 'WILLEMS', 'commercial': 'Aurélien VANPARYS',
     'famille': 'PME', 'actif': True},
    {'id': 12, 'code': '000052', 'nom': 'CAUDRESIENNE ETS', 'ville': 'CAUDRY', 'commercial': 'Olivier GUILLAUME',
     'famille': 'Artisan', 'actif': False},
    {'id': 13, 'code': '000058', 'nom': 'TECH SOLUTIONS PARIS', 'ville': 'PARIS', 'commercial': 'Aurélien VANPARYS',
     'famille': 'Grand Compte', 'actif': True},
    {'id': 14, 'code': '000062', 'nom': 'INNOVATECH', 'ville': 'LYON', 'commercial': 'Olivier GUILLAUME',
     'famille': 'PME', 'actif': True},
    {'id': 15, 'code': '000067', 'nom': 'MARITIME SERVICES', 'ville': 'MARSEILLE', 'commercial': '-',
     'famille': 'Industrie', 'actif': True},
    {'id': 16, 'code': '000071', 'nom': 'ATELIER BOIS MASSIF', 'ville': 'ANNECY', 'commercial': 'Aurélien VANPARYS',
     'famille': 'Artisan', 'actif': True},
    {'id': 17, 'code': '000075', 'nom': 'CONSEIL ET STRATEGIE', 'ville': 'TOULOUSE', 'commercial': 'Olivier GUILLAUME',
     'famille': 'PME', 'actif': True},
    {'id': 18, 'code': '000080', 'nom': 'AGRO INDUSTRIES SUD', 'ville': 'MONTPELLIER', 'commercial': '-',
     'famille': 'Industrie', 'actif': False},
    {'id': 19, 'code': '000084', 'nom': 'DIGITAL AGENCY', 'ville': 'NANTES', 'commercial': 'Aurélien VANPARYS',
     'famille': 'PME', 'actif': True},
    {'id': 20, 'code': '000089', 'nom': 'CONSTRUCTION MODERNE', 'ville': 'BORDEAUX', 'commercial': '-',
     'famille': 'Grand Compte', 'actif': True},
    {'id': 21, 'code': '000093', 'nom': 'DISTRIBUTION OUEST', 'ville': 'RENNES', 'commercial': 'Olivier GUILLAUME',
     'famille': 'PME', 'actif': True},
    {'id': 22, 'code': '000098', 'nom': 'MENUISERIE TRADITIONNELLE', 'ville': 'STRASBOURG', 'commercial': '-',
     'famille': 'Artisan', 'actif': True},
    {'id': 23, 'code': '000102', 'nom': 'ENERGIES RENOUVELABLES', 'ville': 'GRENOBLE',
     'commercial': 'Aurélien VANPARYS', 'famille': 'Industrie', 'actif': True},
    {'id': 24, 'code': '000107', 'nom': 'LOGISTIQUE EXPRESS', 'ville': 'DIJON', 'commercial': 'Olivier GUILLAUME',
     'famille': 'PME', 'actif': True},
    {'id': 25, 'code': '000111', 'nom': 'PHARMA SOLUTIONS', 'ville': 'NICE', 'commercial': '-',
     'famille': 'Grand Compte', 'actif': False},
    {'id': 26, 'code': '000116', 'nom': 'CONSULTING GROUP', 'ville': 'ROUEN', 'commercial': 'Aurélien VANPARYS',
     'famille': 'PME', 'actif': True},
    {'id': 27, 'code': '000120', 'nom': 'TEXTILE INNOVATION', 'ville': 'REIMS', 'commercial': '-',
     'famille': 'Industrie', 'actif': True},
    {'id': 28, 'code': '000125', 'nom': 'FORGE ARTISANALE', 'ville': 'CLERMONT FERRAND',
     'commercial': 'Olivier GUILLAUME', 'famille': 'Artisan', 'actif': True},
    {'id': 29, 'code': '000129', 'nom': 'TELECOM SERVICES', 'ville': 'TOURS', 'commercial': 'Aurélien VANPARYS',
     'famille': 'Grand Compte', 'actif': True},
    {'id': 30, 'code': '000134', 'nom': 'ECO EMBALLAGES', 'ville': 'LIMOGES', 'commercial': '-', 'famille': 'PME',
     'actif': True},
]


# ============================================================================
# KPI DASHBOARD
# ============================================================================

def get_dashboard_kpi():
    """Retourne les KPI pour le dashboard"""
    return [
        {
            'title': 'Projets actifs',
            'value': '24',
            'subtitle': 'vs mois dernier',
            'trend': 'up',
            'trend_value': '+12%',
            'color': 'primary',
            'icon': '''<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>'''
        },
        {
            'title': 'Tâches en cours',
            'value': '156',
            'subtitle': 'à compléter',
            'trend': 'down',
            'trend_value': '-3%',
            'color': 'warning',
            'icon': '''<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
            </svg>'''
        },
        {
            'title': 'Clients actifs',
            'value': '89',
            'subtitle': '+5 nouveaux ce mois',
            'trend': 'up',
            'trend_value': '+5.6%',
            'color': 'success',
            'icon': '''<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>'''
        },
        {
            'title': 'CA du mois',
            'value': '45 352€',
            'subtitle': 'Objectif: 50 000€',
            'trend': 'up',
            'trend_value': '+18%',
            'color': 'info',
            'icon': '''<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>'''
        },
    ]

# ============================================================================
# PROJETS (par client_id)
# ============================================================================

def get_projets_for_client(client_id):
    """Retourne les projets d'un client spécifique"""
    projets_map = {
        2: [
            {
                'reference': 'PRJ-2023-001',
                'nom': 'Refonte site web',
                'date_debut': '15/03/2023',
                'date_fin': '15/06/2023',
                'montant': '45 000€',
                'statut': 'Terminé',
                'badge_color': 'success'
            },
            {
                'reference': 'PRJ-2024-012',
                'nom': 'Application mobile',
                'date_debut': '01/01/2024',
                'date_fin': '30/06/2024',
                'montant': '120 000€',
                'statut': 'En cours',
                'badge_color': 'primary'
            },
            {
                'reference': 'PRJ-2024-045',
                'nom': 'ERP personnalisé',
                'date_debut': '15/08/2024',
                'date_fin': '15/12/2024',
                'montant': '80 000€',
                'statut': 'En cours',
                'badge_color': 'primary'
            },
        ],
        4: [
            {
                'reference': 'PRJ-2024-033',
                'nom': 'Infrastructure Cloud',
                'date_debut': '10/05/2024',
                'date_fin': '10/11/2024',
                'montant': '250 000€',
                'statut': 'En cours',
                'badge_color': 'primary'
            },
        ],
        11: [
            {
                'reference': 'PRJ-2024-021',
                'nom': 'Site e-commerce',
                'date_debut': '01/02/2024',
                'date_fin': '01/05/2024',
                'montant': '35 000€',
                'statut': 'Terminé',
                'badge_color': 'success'
            },
            {
                'reference': 'PRJ-2024-067',
                'nom': 'Module CRM',
                'date_debut': '01/09/2024',
                'date_fin': '31/12/2024',
                'montant': '52 000€',
                'statut': 'En attente',
                'badge_color': 'warning'
            },
        ],
    }
    return projets_map.get(client_id, [])


# ============================================================================
# STATISTIQUES (par client_id)
# ============================================================================

def get_stats_for_client(client_id):
    """Retourne les statistiques d'un client"""
    stats_map = {
        2: {
            'ca_total': '245 000€',
            'projets_actifs': 2,
            'projets_total': 8,
            'factures_impayees': 1,
            'montant_impaye': '8 500€',
            'jours_derniere_commande': '12j',
            'date_derniere_commande': '22/09/2024'
        },
        4: {
            'ca_total': '650 000€',
            'projets_actifs': 1,
            'projets_total': 5,
            'factures_impayees': 0,
            'montant_impaye': '0€',
            'jours_derniere_commande': '5j',
            'date_derniere_commande': '29/09/2024'
        },
        11: {
            'ca_total': '87 000€',
            'projets_actifs': 1,
            'projets_total': 4,
            'factures_impayees': 2,
            'montant_impaye': '15 200€',
            'jours_derniere_commande': '45j',
            'date_derniere_commande': '19/08/2024'
        },
    }
    # Valeurs par défaut si client pas dans le map
    return stats_map.get(client_id, {
        'ca_total': '0€',
        'projets_actifs': 0,
        'projets_total': 0,
        'factures_impayees': 0,
        'montant_impaye': '0€',
        'jours_derniere_commande': '-',
        'date_derniere_commande': '-'
    })


# ============================================================================
# TIMELINE / ACTIVITÉS (par client_id)
# ============================================================================

def get_timeline_for_client(client_id):
    """Retourne l'historique d'activité d'un client"""
    timeline_map = {
        2: [
            {
                'date': '15/03/2023',
                'titre': 'Client créé',
                'description': 'Création de la fiche client dans le système',
                'utilisateur': 'Admin',
                'color': 'success'
            },
            {
                'date': '22/03/2023',
                'titre': 'Premier contact',
                'description': 'Appel téléphonique de qualification',
                'utilisateur': 'Commercial',
                'color': 'primary'
            },
            {
                'date': '05/04/2023',
                'titre': 'Devis envoyé',
                'description': 'Devis DEV-2023-001 • Montant: 45 000€',
                'utilisateur': 'Commercial',
                'color': 'info'
            },
            {
                'date': '12/04/2023',
                'titre': 'Devis accepté',
                'description': 'Signature du devis et création du projet',
                'utilisateur': 'Commercial',
                'color': 'success'
            },
            {
                'date': '22/09/2024',
                'titre': 'Facture émise',
                'description': 'Facture FAC-2024-089 • Montant: 8 500€',
                'utilisateur': 'Service comptabilité',
                'color': 'warning'
            },
        ],
        4: [
            {
                'date': '10/01/2023',
                'titre': 'Client créé',
                'description': 'Création de la fiche client grand compte',
                'utilisateur': 'Admin',
                'color': 'success'
            },
            {
                'date': '15/01/2023',
                'titre': 'Réunion de cadrage',
                'description': 'Présentation des besoins infrastructure',
                'utilisateur': 'Aurélien VANPARYS',
                'color': 'primary'
            },
            {
                'date': '10/05/2024',
                'titre': 'Contrat signé',
                'description': 'Démarrage projet Infrastructure Cloud - 250k€',
                'utilisateur': 'Direction',
                'color': 'success'
            },
        ],
        11: [
            {
                'date': '20/01/2024',
                'titre': 'Client créé',
                'description': 'Ajout du client suite à prospection',
                'utilisateur': 'Aurélien VANPARYS',
                'color': 'success'
            },
            {
                'date': '01/02/2024',
                'titre': 'Projet e-commerce démarré',
                'description': 'Site e-commerce - 35 000€',
                'utilisateur': 'Aurélien VANPARYS',
                'color': 'primary'
            },
            {
                'date': '01/05/2024',
                'titre': 'Projet livré',
                'description': 'Livraison et mise en production du site',
                'utilisateur': 'Équipe dev',
                'color': 'success'
            },
            {
                'date': '15/08/2024',
                'titre': 'Relance factures',
                'description': 'Relance pour 2 factures impayées',
                'utilisateur': 'Service comptabilité',
                'color': 'error'
            },
        ],
    }

    # Valeur par défaut si client pas dans le map
    return timeline_map.get(client_id, [
        {
            'date': '01/01/2024',
            'titre': 'Client créé',
            'description': 'Création de la fiche client',
            'utilisateur': 'Admin',
            'color': 'success'
        },
    ])


# ============================================================================
# HELPERS
# ============================================================================

def get_client_by_id(client_id):
    """Récupère un client par son ID"""
    return next((c for c in ALL_CLIENTS if c['id'] == client_id), None)


def get_commerciaux():
    """Retourne la liste unique des commerciaux"""
    return sorted(list(set([c['commercial'] for c in ALL_CLIENTS if c['commercial'] != '-'])))


def get_familles():
    """Retourne la liste unique des familles"""
    return sorted(list(set([c['famille'] for c in ALL_CLIENTS if c['famille'] != '-'])))