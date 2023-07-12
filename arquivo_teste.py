import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto_estoque.settings")


application = get_wsgi_application()
from app_produtos.models import Alimentos

# alimentos = Alimentos.objects.all()
# for alimento in alimentos:
#     print(str(alimento.nome))

