import os
from urllib import request

from django.core.wsgi import get_wsgi_application



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto_estoque.settings")


application = get_wsgi_application()
from app_produtos.models import Alimentos

dicionario_de_cores = {'preto': '#000', 'branco': '#fff'}
