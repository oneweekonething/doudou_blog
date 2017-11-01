#!/usr/bin/env python
# encoding: utf-8

from django import template
from blog.models import Category
from django.template.defaultfilters import stringfilter
from django.conf import settings
from django.utils.safestring import mark_safe
from blog.models import Article
from comments.models import Comment

register = template.Library()


@register.inclusion_tag('share_layout/nav.html')
def load_nav_info():
    category_list = Category.objects.all()
    return {
        'nav_category_list': category_list
    }


@register.assignment_tag
def query(qs, **kwargs):
    """ template tag which allows queryset filtering. Usage:
        {% query books author=author as mybooks %}
        {% for book in mybooks %}
          ...
        {% endfor %}
    """
    return qs.filter(**kwargs)


@register.inclusion_tag('blog/tags/article_info.html')
def load_article_detail(article, isindex, user):
    """
    加载文章详情
    :param article:
    :param isindex:
    :param user:
    :return:
    """
    return {
        'article': article,
        'isindex': isindex,
        'user': user
    }


@register.inclusion_tag('blog/tags/article_meta_info.html')
def load_article_metas(article, user):
    """
    获得文章的meta信息
    :param article:
    :param user:
    :return:
    """
    return {
        'article': article,
        'user': user
    }


@register.filter(is_safe=True)
@stringfilter
def truncatechars_content(content):
    from django.template.defaultfilters import truncatechars_html
    return truncatechars_html(content, settings.ARTICLE_SUB_LENGTH)


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(content):
    from doudou_blog.utils import CommonMarkdown
    return mark_safe(CommonMarkdown.get_markdown(content))


@register.simple_tag
def datetimeformat(data):
    try:
        return data.strftime(settings.DATE_TIME_FORMAT)
    except:
        return ""


@register.inclusion_tag('blog/tags/sidebar.html')
def load_sidebar(user):
    """
    加载侧边栏
    :param user:
    :return:
    """
    recent_articles = Article.objects.filter(status='p')[:settings.SIDEBAR_ARTICLE_COUNT]
    sidebar_categorys = Category.objects.all()
    most_read_articles = Article.objects.filter(status='p').order_by('-views')[:settings.SIDEBAR_ARTICLE_COUNT]
    commment_list = Comment.objects.order_by('-id')[:settings.SIDEBAR_COMMENT_COUNT]
    return {
        'user': user,
        'recent_articles': recent_articles,
        'sidebar_categorys': sidebar_categorys,
        'most_read_articles': most_read_articles,
        'sidebar_comments': commment_list
    }
