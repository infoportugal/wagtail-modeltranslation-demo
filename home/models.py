from django.db import models
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel("sub_models"),
    ]


# class TopModel(ClusterableModel):
#     panels = [
#         InlinePanel("sub_models"),
#     ]


class SubModel(ClusterableModel):
    top_model = ParentalKey(HomePage, related_name="sub_models", on_delete=models.CASCADE)

    panels = [
        InlinePanel("sub_sub_models"),
    ]


class SubSubModel(models.Model):
    sub_model = ParentalKey(SubModel, on_delete=models.CASCADE, related_name="sub_sub_models")
    body = RichTextField(blank=True)
