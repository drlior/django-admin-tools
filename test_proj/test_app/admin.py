from django.contrib import admin
from test_proj.test_app.models import Foo, Bar

admin.site.register(Foo)
admin.site.register(Bar)
