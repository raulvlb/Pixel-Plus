from django.contrib import admin

from .models import portfolio, quemsomos, servicos1, servicos2, trabalhos, depoimentos, FormContato, RedesSociais
# Register your models here.

admin.site.register(portfolio)
admin.site.register(quemsomos)
admin.site.register(servicos1)
admin.site.register(servicos2)
admin.site.register(trabalhos)
admin.site.register(depoimentos)
admin.site.register(FormContato)
admin.site.register(RedesSociais)
