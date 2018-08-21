from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import HomePage, HompageInline


@register(HompageInline)
class InlineSectionsUsefulInfoTR(TranslationOptions):
    fields = ('title', 'body',)


@register(HomePage)
class UsefulInfoPageTR(TranslationOptions):
    pass
