from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.utils import six
try:
    from django.utils.text import truncate_words
except ImportError:
    # django >=1.5
    from django.utils.text import Truncator
    from django.utils.functional import allow_lazy
    def truncate_words(s, num, end_text='...'):
        truncate = end_text and ' %s' % end_text or ''
        return Truncator(s).words(num, truncate=truncate)
    truncate_words = allow_lazy(truncate_words, six.text_type)

class Announcement(models.Model):
    content = models.TextField(verbose_name=_('Announcement'))
    enabled = models.BooleanField(default=False, verbose_name=_('Enabled'), db_index=True)
    ordering = models.IntegerField(default=1, verbose_name=_('Order'), db_index=True)
    important = models.BooleanField(default=False, verbose_name=_('Important'), db_index=True)

    class Meta:
        ordering = ['ordering']

    def __unicode__(self):
        return truncate_words(self.content, 10)
