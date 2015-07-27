from setuptools import setup

reqs=[
    'quamash',
    'click',
    'pyxdg',
    'fuzzywuzzy'
],
test_reqs = ['pytest', 'pytest-qt']
requires = {
    'setup_requires': ['setuptools_scm'],
    'install_requires': reqs,
    'tests_require': test_reqs,
    'extras_require': {
        'testing': test_reqs,
    }
}

setup(
    name='kya',
    use_scm_version=True,
    author='Keerthan Jaic',
    author_email='jckeerthan@gmail.com',
    url='http://github.com/jck/kya',
    packages=['kya', 'kya.plugins'],
    description='what?',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 1 - Planning'
    ],
    entry_points={
        'console_scripts': [
            'kya=kya.cli:cli'
        ]
    },
    **requires
)
