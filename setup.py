
import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('kya/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='kya',
    author='Keerthan Jaic',
    author_email='jckeerthan@gmail.com',
    version=version,
    url='http://github.com/jck/kya',
    packages=['kya'],
    description='what?',
    zip_safe=False,
    install_requires=[
        'pyxdg'
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'kya=kya.kya:cli'
        ]
    }
)
