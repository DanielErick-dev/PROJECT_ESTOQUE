import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto_estoque.settings")


application = get_wsgi_application()
from app_produtos.models import Alimentos

alimento = Alimentos.objects.get(nome='barra chocolate')
alimento.quantidade = 100
alimento.save()