from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.db.models import Q


def home_page(request):
    hot_posts = Post.objects.all().order_by('-created_at')[:4]
    posts = Post.objects.all().order_by('-created_at')[:5]
    context = {
        'hot_posts': hot_posts,
        'posts': posts,
    }
    return render(request, 'index.html', context)

def all_news_page(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'all-news.html', context)

def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'by-category.html', context)

def search_page(request):
    return render(request, 'search.html')

def search_results(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        all_posts = Post.objects.all()
        query_lower = query.lower()

        results = [
            post for post in all_posts
            if query_lower in post.title.lower() or
               query_lower in post.description.lower()
        ]

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search-results.html', context)

def read_news(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # related posts: same category, exclude current post, latest first, limit 4
    related_posts = Post.objects.filter(category=post.category).exclude(pk=post.pk).order_by('-created_at')[:4]
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'read-news.html', context)
