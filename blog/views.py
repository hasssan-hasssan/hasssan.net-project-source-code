from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.core.mail import send_mail
from django.db.models import Count
from django.views.generic import ListView, TemplateView
from blog.models import *
from blog.forms import *
from django.contrib import messages


class Post_list(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, publish__year=year, publish__month=month, publish__day=day)

    # Similar Posts
    post_tags_ids = post.tags.values_list('id')
    similar_posts = Post.published.filter(tags__in=post_tags_ids) \
                        .distinct().exclude(id=post.id) \
                        .annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:6]

    # Post's Codes
    descriptions = Description.objects.filter(post__id=post.id)

    # Post's Comments
    post_id = post.id
    comments = Comment.activated.filter(post__id=post_id)

    # Handle Comment Form
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            nc = form.save(commit=False)
            nc.post = post
            nc.save()
            messages.success(request, 'دیدگاه شما با موفقیت ثبت شد!')
            return redirect(post.get_absolute_url())

    context = {
        'post': post,
        'similar_posts': similar_posts,
        'comments': comments,
        'form': form,
        'descriptions': descriptions
    }
    template_name = 'detail.html'
    return render(request, template_name, context)


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')

    # Handle Email Form
    if request.method == 'POST':
        form = ShareForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Send Mail
            location = post.get_absolute_url()
            post_url = request.build_absolute_uri(location)
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {cd['name']} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'info@mysite.com', [cd['to']])
            messages.success(request, f"پست '{post.title}' با موفقیت به '{cd['to']}' ارسال شد.")
            return redirect(post.get_absolute_url())
    else:
        form = ShareForm()
    context = {
        'post': post,
        'form': form,
    }
    template_name = 'share.html'
    return render(request, template_name, context)


class Pro_list(ListView):
    model = Project
    paginate_by = 3
    context_object_name = 'projects'
    template_name = 'pro_list.html'


def pro_detail(request, project):
    project = get_object_or_404(Project, slug=project)

    # Project's Comments
    pro_id = project.id
    comments = Comment.activated.filter(project__id=pro_id)

    # Handle Comment Form
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            nc = form.save(commit=False)
            nc.project = project
            nc.save()
            messages.success(request, 'دیدگاه شما با موفقیت ثبت شد!')
            return redirect(project.get_absolute_url())
    else:
        form = CommentForm()

    context = {
        'project': project,
        'comments': comments,
        'form': form,
    }
    template_name = 'pro_detail.html'
    return render(request, template_name, context)


def search_engine(request):
    # Handle Form Search Engine
    posts = []
    query = False
    if request.method != 'POST':
        form = SearchForm()
    else:
        form = SearchForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            posts = Post.published.filter(body__contains=data['data'])
            query = True

    context = {
        'form': form,
        'posts': posts,
        'query': query,
    }
    template_name = 'search_engine.html'
    return render(request, template_name, context)


class Teaches_List(ListView):
    model = Teach
    context_object_name = 'teaches'
    template_name = 'teaches_list.html'
    paginate_by = 6


def teach_detail(request, slug):
    teach = get_object_or_404(Teach, slug=slug)
    posts = teach.posts.order_by('publish')
    context = {
        'posts': posts,
        'teach': teach,
    }
    template_name = 'teach_detail.html'
    return render(request, template_name, context)


class About_Me(TemplateView):
    template_name = 'about_me.html'
