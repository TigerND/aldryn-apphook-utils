## aldryn-apphooks-config-utils
[![Build Status](https://travis-ci.org/TigerND/aldryn-apphooks-config-utils.svg?branch=master)](https://travis-ci.org/TigerND/aldryn-apphooks-config-utils)

Utils for aldryn-apphooks-config

### Example usage

```html
{% load aldryn_apphooks_config_utils %}

{% block content %}
    {% aldryn_apphooks_config %}
    Namespace: "{{ namespace }}", Config: "{{ config }}"
{% endblock %}
```

```html
{% load aldryn_apphooks_config_utils %}

{% block content %}
    {% with_aldryn_apphooks_config %}
       Namespace: "{{ namespace }}", Config: "{{ config }}"
    {% endwith_aldryn_apphooks_config %}
{% endblock %}
```