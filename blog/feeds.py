from django.urls import reverse_lazy
from blog.models import Post
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description_template = 'New posts of my blog'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 10)