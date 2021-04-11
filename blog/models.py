from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Teach(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    thumbnail = models.ImageField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'teaches'


class PublishedManager(models.Manager):
    """ Personal Manager for Published Posts """

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    """ Posts' Model """

    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish', allow_unicode=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    teach = models.ForeignKey(Teach, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    objects = models.Manager()  # Django Manager
    published = PublishedManager()  # Post Manager
    tags = TaggableManager()  # Tag Manager

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug,
        ])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']


class Project(models.Model):
    """ Projects' Model """

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    link = models.URLField()
    create = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    thumbnail_screen_lg = models.ImageField()
    thumbnail_screen_sm = models.ImageField()

    def get_absolute_url(self):
        return reverse('blog:pro_detail', args=[
            self.slug,
        ])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create']


class ActiveManager(models.Manager):
    """ Personal Manager for Active Comments """

    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(active_status=True)


class Comment(models.Model):
    """ Comments' model """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='p_comments', null=True, )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='w_comments', null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    active_status = models.BooleanField(default=True)
    objects = models.Manager()  # Django Manager
    activated = ActiveManager()  # Personal Manager

    def __str__(self):
        return f"Comment by {self.name} in {self.create}"

    class Meta:
        ordering = ['-create']


class Description(models.Model):
    """ Description's Model """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='description')
    header_description = models.TextField()
    body_description = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['create']


class Reply(models.Model):
    """ Replies' Model """

    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()

    def __str__(self):
        return f"Reply by {str(self.author)} on comment :({str(self.comment.body)})"

    class Meta:
        verbose_name_plural = 'replies'


