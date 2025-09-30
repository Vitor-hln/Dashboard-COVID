from django.shortcuts import render

def dashboard(request):
    """
    View principal que renderiza o template do dashboard
    As APIs são chamadas diretamente pelo JavaScript do frontend
    """
    return render(request, 'dashboard/index.html')

# Remova estas funções - não são mais necessárias
# def get_global_stats(request):
# def get_country_timeline(request, country_code):
# def get_heatmap_data(request):