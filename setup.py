#!/usr/bin/env python

from setuptools import setup

setup(
    name='aldryn-apphooks-config-utils',
    version='0.1.0',
    description='aldryn-apphooks-config-utils',
    author='Aleksandr Zykov',
    author_email='tiger@vilijavis.lt',
    url='https://github.com/TigerND/aldryn-apphooks-config-utils',
    packages=[
        'aldryn_apphooks_config_utils',
        'aldryn_apphooks_config_utils.templatetags',
    ],
    data_files=[
    ],
    install_requires = [
        'aldryn-apphooks-config>=0.2.7',
    ],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)
