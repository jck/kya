from setuptools import setup

tests_require = ['pytest', 'pytest-qt']

setup(
    name='kya',
    use_scm_version=True,
    author='Keerthan Jaic',
    author_email='jckeerthan@gmail.com',
    url='http://github.com/jck/kya',
    packages=['kya', 'kya.plugins'],
    description='what?',
    zip_safe=False,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'click',
        'pyxdg',
        'quamash',
    ],
    tests_require=tests_require,
    extras_require={
        'testing': tests_require,
    },
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'kya=kya.cli:cli'
        ]
    }
)
