from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page


class HomePage(Page):
    intro_title = models.CharField(max_length=16, verbose_name="Título")
    intro_body = models.CharField(max_length=64, verbose_name="Corpo")
    intro_background = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Imagem de fundo"
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro_title', classname="full"),
        FieldPanel('intro_body', classname="full"),
        ImageChooserPanel('intro_background', classname="full"),
    ]
