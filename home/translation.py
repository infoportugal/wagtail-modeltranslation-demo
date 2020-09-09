from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import HomePage, SubSubModel


@register(HomePage)
class HomePageTR(TranslationOptions):
    pass

@register(SubSubModel)
class SubSubModelTR(TranslationOptions):
    fields = ('body',)
