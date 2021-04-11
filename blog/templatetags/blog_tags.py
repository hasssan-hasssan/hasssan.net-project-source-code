import markdown
from django import template
from blog.models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('latest.html')
def show_latest_posts(count):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=3):
    return Post.published.annotate(total_comments=Count('p_comments')) \
               .order_by('-total_comments')[:count]


@register.filter
def mark_safe_markdown_filter(text):
    return mark_safe(markdown.markdown(text))


@register.filter
def mark_safe_filter(text):
    return mark_safe(text)


@register.simple_tag
def get_commented_post(post_id):
    post = Post.published.get(id=post_id)
    return post.p_comments.count()
