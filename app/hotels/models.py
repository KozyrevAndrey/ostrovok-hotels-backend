from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Hotel(models.Model):
    name = models.CharField(_('Name'), max_length=3000, help_text=_('Hotel Name'))
    address = models.CharField(
        _('Address'), max_length=3000, help_text=_('Hotel Address')
    )
    phone_number = PhoneNumberField(
        _('Phone Number'), help_text=_('Hotel Phone Number')
    )
    city = models.ForeignKey(
        'dictionaries.City', on_delete=models.PROTECT, help_text=_('Hotel City')
    )

    class Meta:
        verbose_name = _('Hotels')
        verbose_name_plural = _('Hotels')

    def __str__(self):
        return self.name
