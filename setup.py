from setuptools import setup, find_packages

setup(
		name ="simplecareers",
        version  ="0.1",
        packages = find_packages(),
        install_requires = [
        	"django-uni-form",
        	"django-classy-tags",
        	"surlex",
        	"south",
        ],
)