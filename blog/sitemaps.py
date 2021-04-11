from django.contrib.sitemaps import Sitemap
from blog.models import *


class PostSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.update


class ProjectSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.6

    def items(self):
        return Project.objects.all()
