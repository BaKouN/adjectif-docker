from django.shortcuts import render

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
    return render(request, 'dashboard/pages/list.html')

def create_view(request):
    return render(request, 'dashboard/pages/create.html')

def edit_view(request, pk):
    return render(request, 'dashboard/pages/edit.html', {'pk': pk})

def detail_view(request, pk):
    return render(request, 'dashboard/pages/detail.html', {'pk': pk})