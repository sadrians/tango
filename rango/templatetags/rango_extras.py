'''
Created on Jan 23, 2016

@author: ad
'''
from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
    print 'cat is', cat
    return {'cats': Category.objects.all(), 'act_cat': cat}