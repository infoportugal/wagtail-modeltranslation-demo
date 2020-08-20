from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import HomePage


@register(HomePage)
class HomePageTR(TranslationOptions):
    pass
