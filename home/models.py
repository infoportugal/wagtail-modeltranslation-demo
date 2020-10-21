from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class SkiResortPage(Page):
    top_destination_first_block = models.ForeignKey(
        "home.HomePage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="ski_resort_pages_top_destination_first_block",
    )

class DestinationPage(Page):
    heading_h1 = models.CharField(max_length=100, blank=True)
    heading_h2 = models.CharField(max_length=100, blank=True)
