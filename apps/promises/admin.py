from django.contrib import admin
from promises.models import Promise, Source, Status

admin.site.register(Promise)
admin.site.register(Source)
admin.site.register(Status)
