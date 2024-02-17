from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(max_length=1000, db_index=True, help_text=_('City Name'))

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self) -> str:
        return self.name
