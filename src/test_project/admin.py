from django.contrib import admin
from .models import Classe
from .models import Devoir
from .models import Participe
# Register your models here.
admin.site.register(Classe)
admin.site.register(Devoir)
admin.site.register(Participe)
