# coding: utf-8
import os
import sys

from setuptools import setup


__author__ = 'Yeongbin Jo <iam.yeongbin.jo@gmail.com>'


with open('README.md') as readme_file:
    long_description = readme_file.read()


# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()
elif sys.argv[-1] == 'clean':
    import shutil
    if os.path.isdir('build'):
        shutil.rmtree('build')
    if os.path.isdir('dist'):
        shutil.rmtree('dist')
    if os.path.isdir('edgedriver_autoinstaller.egg-info'):
        shutil.rmtree('edgedriver_autoinstaller.egg-info')


setup(
    name="edgedriver-autoinstaller",
    version="0.2.1",
    author="Federico Capece",
    author_email="capece.1744999@studenti.uniroma1.it",
    description="Automatically install edgedriver that supports the currently installed version of edge.",
    license="MIT",
    keywords="edgedriver edge selenium splinter",
    url="https://github.com/fc-dev/python-edgedriver-autoinstaller",
    packages=['edgedriver_autoinstaller'],
    entry_points={
        'console_scripts': ['edgedriver-path=edgedriver_autoinstaller.utils:print_edgedriver_path'],
    },
    long_description_content_type='text/markdown',
    long_description=long_description,
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Installation/Setup',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=["requests"],
)
