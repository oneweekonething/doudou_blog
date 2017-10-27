#!/usr/bin/env python
# encoding: utf-8

from django import template

register = template.Library()


@register.assignment_tag()
def parse_commenttree(commentlist, comment):
    """获得当前评论子评论的列表
    """
    datas = []

    def parse(c):
        chids = commentlist.filter(parent_comment=c)
        for chid in chids:
            datas.append(chid)
            parse(chid)

    parse(comment)
    return datas


@register.inclusion_tag('comments/tags/comment_item.html')
def show_comment_item(comment, ischild):
    """评论"""
    depth = 1 if ischild else 2
    return {
        'comment_item': comment,
        'depth': depth
    }
