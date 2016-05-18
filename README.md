## aldryn-apphooks-config-utils
Utils for aldryn-apphooks-config

### Example usage

```html
{% load aldryn_apphoks_config_utils %}

{% block content %}
    {% aldryn_apphoks_config %}
    Namespace: "{{ namespace }}", Config: "{{ config }}"
{% endblock %}
```

```html
{% load aldryn_apphoks_config_utils %}

{% block content %}
    {% with_aldryn_apphoks_config %}
       Namespace: "{{ namespace }}", Config: "{{ config }}"
    {% endwith_aldryn_apphoks_config %}
{% endblock %}
```