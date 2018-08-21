from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Orderable, Page
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                                MultiFieldPanel)
from wagtail.core.fields import RichTextField


class HompageInline(Orderable):
    page = ParentalKey('home.HomePage', related_name='inlines')
    title = models.CharField(verbose_name='Title', max_length=50)
    body = RichTextField(verbose_name=u'Body')

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
        ], heading='Title'),
        MultiFieldPanel([
            FieldPanel('body'),
        ], heading='Body'),
    ]


class HomePage(Page):

    content_panels = [
        MultiFieldPanel([
            FieldPanel('title'),
        ], heading='Title'),
        InlinePanel('inlines', label=u'Inlines')
    ]
