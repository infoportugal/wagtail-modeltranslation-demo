from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import DestinationPage, HomePage, SkiResortPage


@register(HomePage)
class HomePageTR(TranslationOptions):
    pass


@register(SkiResortPage)
class SkiResortPageTR(TranslationOptions):
    pass


@register(DestinationPage)
class DestinationPageTR(TranslationOptions):
    fields = (
        "heading_h1",
        "heading_h2",
    )
