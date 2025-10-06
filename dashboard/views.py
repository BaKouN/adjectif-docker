from django.shortcuts import render
from django.core.paginator import Paginator
from . import mock_data


def dashboard(request):
    """Page d'accueil du dashboard avec KPI"""
    context = {
        'kpi_data': mock_data.get_dashboard_kpi(),
        'breadcrumb_items': [{'label': 'Dashboard', 'url': None}]
    }
    return render(request, 'dashboard/pages/dashboard.html', context)


def list_view(request):
    """Liste des clients avec filtres et pagination"""
    all_clients = mock_data.ALL_CLIENTS

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

    # Pagination (10 par page)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(filtered_clients, 10)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'breadcrumb_items': [{'label': 'Clients', 'url': None}],
        'total_clients': len(all_clients),
        'filtered_count': len(filtered_clients),
        'commerciaux': mock_data.get_commerciaux(),
        'familles': mock_data.get_familles(),
        'current_search': search,
        'current_actif': actif_filter,
        'current_commercial': commercial_filter,
        'current_famille': famille_filter,
    }

    # Si requête HTMX, renvoyer juste la table
    if request.headers.get('HX-Request'):
        return render(request, 'dashboard/list/clients_table.html', {'page_obj': page_obj})

    return render(request, 'dashboard/pages/list.html', context)


def create_view(request):
    """Page de création d'un client"""
    return render(request, 'dashboard/pages/create.html')


def edit_view(request, pk):
    """Page d'édition d'un client"""
    return render(request, 'dashboard/pages/edit.html', {'pk': pk})


def detail_view(request, pk):
    """Page de détail d'un client avec onglets HTMX"""
    client = mock_data.get_client_by_id(pk)
    if not client:
        client = mock_data.ALL_CLIENTS[0]

    tab = request.GET.get('tab', 'info')

    context = {
        'client': client,
        'breadcrumb_items': [
            {'label': 'Clients', 'url': '/list/'},
            {'label': client['nom'], 'url': None}
        ],
        'current_tab': tab,
    }

    # Si requête HTMX, renvoyer juste le contenu du tab
    if request.headers.get('HX-Request'):
        if tab == 'projets':
            context['projets'] = mock_data.get_projets_for_client(pk)
        elif tab == 'stats':
            context['stats'] = mock_data.get_stats_for_client(pk)
        elif tab == 'timeline':
            context['timeline'] = mock_data.get_timeline_for_client(pk)

        return render(request, f'dashboard/detail/tab_{tab}.html', context)

    return render(request, 'dashboard/pages/detail.html', context)