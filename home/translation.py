from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import HomePage, BlogPage


@register(HomePage)
class HomePageTR(TranslationOptions):
    pass

@register(BlogPage)
class BlogPageTR(TranslationOptions):
    pass
