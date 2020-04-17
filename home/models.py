from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page


class HomePage(Page):

    st = StreamField(
        [
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
        ],
        verbose_name='Stream',
        null=True,
        blank=True,
    )

    content_panels = [
        MultiFieldPanel([
            FieldPanel('title'),
        ], heading='Title'),

        StreamFieldPanel('st'),
    ]
