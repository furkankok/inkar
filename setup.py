from setuptools import setup, find_packages

setup(
    name='django-validate-decorators',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='Useful decorators for Django views',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Furkan Koksal',
    author_email='furkankoksaldi28@gmail.com',
    url='https://github.com/furkankok/inkar',
    install_requires=[
        'Django>=4.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
