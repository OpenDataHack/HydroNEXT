from django.contrib import admin

from .models import Option
from .models import Localizacion
from .models import Coordenadas

admin.site.register(Option)
admin.site.register(Localizacion)
admin.site.register(Coordenadas)
