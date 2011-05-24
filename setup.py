# Copyright (c) 2011 Simplistix Ltd
# See license.txt for license details.

import os
from setuptools import setup,find_packages

base_dir = os.path.dirname(__file__)

setup(
    name='mortar_workflow',
    author='Chris Withers',
    version='0.3dev',
    author_email='chris@simplistix.co.uk',
    license='MIT',
    description="A framework-agnostic, storage-agnostic state based workflow engine",
    long_description=open(os.path.join(base_dir,'docs','description.txt')).read(),
    url='http://www.simplistix.co.uk/software/python/mortar_workflow',
    classifiers=[
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
    ],    
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires = (
        ),
    extras_require=dict(
        test=[
            'mock',
            'manuel',
            'testfixtures',
            ],
        ),
    )

