import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='flaskr',
    version='1.0.0',
    url='http://flask.pocoo.org/docs/tutorial/',
    license='BSD',
    maintainer='yang he teng shan',
    maintainer_email='tengshan2008@hotmail.com',
    description='The basic blog app built in the Flask tutorial.',
    long_decription=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['flask'],
    extras_require={
        'test': ['pytest', 'coverage']
    }
)