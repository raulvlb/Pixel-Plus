from django.shortcuts import render

from .models import portfolio, quemsomos, servicos1, servicos2, trabalhos, depoimentos, FormContato, RedesSociais

# Create your views here.
def index(request):

    itens_portfolio = portfolio.objects.last()
    quem_somos = quemsomos.objects.last()
    servicos_1 = servicos1.objects.last()
    servicos_2 = servicos2.objects.last()
    itens_trabalhos = trabalhos.objects.all()
    itens_depoimentos = depoimentos.objects.all()
    itens_redes_sociais = RedesSociais.objects.last()

    context = {
        'portfolio' : itens_portfolio,
        'quemsomos' : quem_somos,
        'servicos1' : servicos_1,
        'servicos2' : servicos_2,
        'trabalhos' : itens_trabalhos,
        'depoimentos' : itens_depoimentos,
        'redes' : itens_redes_sociais,
    }

    if request.method == 'POST':
        nome_form =request.POST['nome']
        email_form = request.POST['email']
        comentario_form = request.POST['comentario']

        form = FormContato(nome=nome_form, email=email_form, comentario=comentario_form)
        form.save()

    return render(request, 'index.html', context)