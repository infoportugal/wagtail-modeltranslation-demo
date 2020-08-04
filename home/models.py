from django.http import HttpResponseRedirect
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class BlogPage(Page):
    content_panels = [
        MultiFieldPanel([
            FieldPanel('title'),
        ], heading='Title'),
    ]


class HomePage(RoutablePageMixin, Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    @route(r"^(?P<blog_slug>[-\w]*)/$", name="blog_post")
    def blog_post(self, request, blog_slug, *args, **kwargs):
        print("HERER")
        print(blog_slug)
        try:
            # Get the blog page
            blog_page = BlogPage.objects.live().get(slug=blog_slug)
            print("GET")
        except BlogPage.DoesNotExist:
            # 404 or post is not live yet
            return HttpResponseRedirect("/")
        except Exception:
            # Handle your other exceptions here; here's a simple redirect back to home
            return HttpResponseRedirect("/")

        # Additional logic if you need to perform something before serving the blog post

        # Let the blog post page handle the serve
        return blog_page.specific.serve(request, *args, **kwargs)
