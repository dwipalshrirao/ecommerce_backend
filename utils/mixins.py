from django.db import models



class BaseModelMixin(models.Model):
    modification_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False, )

    class Meta:
        abstract = True