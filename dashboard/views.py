from django.shortcuts import render
from django.core.paginator import Paginator

def dashboard(request):
    # Données KPI (en vrai ça viendrait de ta base de données)
    kpi_data = [
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
    
    # Fil d'Ariane
    breadcrumb_items = [
        {'label': 'Dashboard', 'url': None}
    ]
    
    context = {
        'kpi_data': kpi_data,
        'breadcrumb_items': breadcrumb_items,
    }
    
    return render(request, 'dashboard/pages/dashboard.html', context)

def list_view(request):
    # Données de démo complètes (12 clients)
    all_clients = [
        {'id': 1, 'code': '000000', 'nom': 'PROSPECT', 'ville': '-', 'commercial': '-', 'famille': '-', 'actif': True},
        {'id': 2, 'code': '000006', 'nom': 'GRAINOCEAN INTERNATIONAL', 'ville': 'LA ROCHELLE CDX', 'commercial': '-', 'famille': 'Industrie', 'actif': True},
        {'id': 3, 'code': '000015', 'nom': 'BAUDELET SAS', 'ville': 'BLARINGHEM', 'commercial': '-', 'famille': 'PME', 'actif': True},
        {'id': 4, 'code': '000024', 'nom': 'TPF UTILITIES FRANCE', 'ville': 'FRETIN', 'commercial': '-', 'famille': 'Grand Compte', 'actif': True},
        {'id': 5, 'code': '000025', 'nom': 'CONSTELLIUM MONTREUIL JUIGNE', 'ville': 'MONTREUIL JUIGNE', 'commercial': '-', 'famille': 'Industrie', 'actif': False},
        {'id': 6, 'code': '000031', 'nom': 'SOFISE', 'ville': 'VENISSIEUX', 'commercial': '-', 'famille': '-', 'actif': True},
        {'id': 7, 'code': '000036', 'nom': 'WDL S.A.S', 'ville': 'LILLE CEDEX', 'commercial': '-', 'famille': 'PME', 'actif': True},
        {'id': 8, 'code': '000042', 'nom': 'NWL FRANCE SERVICES SAS', 'ville': 'SAINT HERBLAIN', 'commercial': '-', 'famille': '-', 'actif': True},
        {'id': 9, 'code': '000044', 'nom': 'COS ARTISAN', 'ville': 'ST GERMAIN S/MORIN', 'commercial': '-', 'famille': 'Artisan', 'actif': True},
        {'id': 10, 'code': '000049', 'nom': 'CARPENTIER PREUX', 'ville': 'CAUDRY', 'commercial': 'Aurélien VANPARYS', 'famille': '-', 'actif': True},
        {'id': 11, 'code': '000051', 'nom': 'DUO EMBALLAGES', 'ville': 'WILLEMS', 'commercial': 'Aurélien VANPARYS', 'famille': 'PME', 'actif': True},
        {'id': 12, 'code': '000052', 'nom': 'CAUDRESIENNE ETS', 'ville': 'CAUDRY', 'commercial': 'Olivier GUILLAUME', 'famille': 'Artisan', 'actif': False},
    ]
    
    # Récupérer les filtres
    search = request.GET.get('search', '')
    actif_filter = request.GET.get('actif', '')
    commercial_filter = request.GET.get('commercial', '')
    famille_filter = request.GET.get('famille', '')
    
    # Appliquer les filtres
    filtered_clients = all_clients
    
    if search:
        filtered_clients = [c for c in filtered_clients if 
                          search.lower() in c['nom'].lower() or 
                          search.lower() in c['code'].lower() or
                          search.lower() in c['ville'].lower()]
    
    if actif_filter:
        actif_bool = actif_filter == 'true'
        filtered_clients = [c for c in filtered_clients if c['actif'] == actif_bool]
    
    if commercial_filter and commercial_filter != '-':
        filtered_clients = [c for c in filtered_clients if c['commercial'] == commercial_filter]
    
    if famille_filter and famille_filter != '-':
        filtered_clients = [c for c in filtered_clients if c['famille'] == famille_filter]
    
    # Pagination (5 par page)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(filtered_clients, 5)
    page_obj = paginator.get_page(page_number)
    
    # Listes pour les filtres
    commerciaux = sorted(list(set([c['commercial'] for c in all_clients if c['commercial'] != '-'])))
    familles = sorted(list(set([c['famille'] for c in all_clients if c['famille'] != '-'])))
    
    breadcrumb_items = [
        {'label': 'Clients', 'url': None}
    ]
    
    # Si requête HTMX, renvoyer juste la table
    if request.headers.get('HX-Request'):
        return render(request, 'dashboard/components/clients_table.html', {
            'page_obj': page_obj,
        })
    
    # Sinon, page complète
    context = {
        'page_obj': page_obj,
        'breadcrumb_items': breadcrumb_items,
        'total_clients': len(all_clients),
        'filtered_count': len(filtered_clients),
        'commerciaux': commerciaux,
        'familles': familles,
        'current_search': search,
        'current_actif': actif_filter,
        'current_commercial': commercial_filter,
        'current_famille': famille_filter,
    }
    
    return render(request, 'dashboard/pages/list.html', context)

def create_view(request):
    return render(request, 'dashboard/pages/create.html')

def edit_view(request, pk):
    return render(request, 'dashboard/pages/edit.html', {'pk': pk})

def detail_view(request, pk):
    return render(request, 'dashboard/pages/detail.html', {'pk': pk})