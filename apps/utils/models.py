from django.db import models
from apps.authapp.models import User


# Create your models here.
class AbstractTableMeta(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User(), on_delete=models.DO_NOTHING, related_name='+')
    updated_by = models.ForeignKey(User(), on_delete=models.DO_NOTHING, related_name='+')

    class Meta:
        abstract = True
