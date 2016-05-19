# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from aldryn_apphooks_config.utils import get_app_instance


def apphooks_config(request):
    namespace, config = get_app_instance(request)
    return {
        'namespace': namespace,
        'config': config,
    }
