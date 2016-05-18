# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.template.base import Node

from aldryn_apphooks_config.utils import get_app_instance

register = template.Library()


@register.simple_tag(takes_context=True)
def aldryn_apphoks_config(context, *args, **kwargs):
    """
    Example:

        {% load aldryn_apphoks_config_utils %}

        {% block content %}
            {% aldryn_apphoks_config %}
            Namespace: "{{ namespace }}", Config: "{{ config }}"
        {% endblock %}
    """

    namespace, config = get_app_instance(context.request)
    context['namespace'] = namespace
    context['config'] = config
    return ''


class AldrynApphooksConfigNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        namespace, config = get_app_instance(context.request)
        values = {
            'namespace': namespace,
            'config': config,
        }
        with context.push(**values):
            return self.nodelist.render(context)


@register.tag('with_aldryn_apphoks_config')
def with_aldryn_apphoks_config(parser, token):
    """
    Example:

        {% load aldryn_apphoks_config_utils %}

        {% block content %}
            {% with_aldryn_apphoks_config %}
               Namespace: "{{ namespace }}", Config: "{{ config }}"
            {% endwith_aldryn_apphoks_config %}
        {% endblock %}
    """

    nodelist = parser.parse(('endwith_aldryn_apphoks_config',))
    parser.delete_first_token()
    return AldrynApphooksConfigNode(nodelist)
