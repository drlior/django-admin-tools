from django.db import models


class Foo(models.Model):
    class Meta:
        app_label="foo"


class Bar(models.Model):
    class Meta:
        app_label="foo"
