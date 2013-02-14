import os
from setuptools import setup, find_packages

import simplecareers


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name ="django-simple-careers",
    version=simplecareers.__version__,
    classifiers = (
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ),
    packages=find_packages(),
    install_requires = (
    	"django-uni-form",
    	"django-classy-tags",
    	"surlex",
    	"south",
    ),
    author='Zenobius Jiricek',
    author_email='airtonix@gmail.com',
    description='a simple careers application for django. post jobs, toggle them as vacancies and collect applications with resume uploads',
    long_description = read('README.md'),
    license='MIT',
    keywords='django, careers, jobs, vacancies, human resource',
    url='http://github.com/airtonix/django-simple-careers/',
    include_package_data=True,
)