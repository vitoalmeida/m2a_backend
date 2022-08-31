from setuptools import setup, find_packages

setup(
    name='Gabriel API',
    packages=find_packages(),
    install_requires=[
        'Django==3.2.7',
        'django-cors-headers==3.8.0',
        'djangorestframework==3.12.4',
        'drf-yasg==1.20.0',
        'djangorestframework-simplejwt==5.2.0',
        'django-filter==21.1'
    ],
    author='Luiz Fernando Rodrigues Lemos',
    author_email='luizfernandorole@gmail.com'
)
