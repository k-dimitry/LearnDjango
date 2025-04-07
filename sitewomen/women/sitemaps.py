from django.contrib.sitemaps import Sitemap

from women.models import Woman, Category


class PostSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Woman.published.all()

    def lastmod(self, obj):
        return obj.time_updated


class CategorySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Category.objects.all()
