from django.contrib import admin

from .models import User
from .models import Team
from .models import Mapt

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Mapt)