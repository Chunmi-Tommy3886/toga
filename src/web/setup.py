#/usr/bin/env python
import io
import re
import sys

from setuptools import setup, find_packages

if sys.version_info[:3] < (3, 4):
    raise SystemExit("Toga requires Python 3.4+.")


with io.open('toga_web/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='toga-web',
    version=version,
    description='A common backend for the Toga widget toolkit on web platforms.',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://pybee.org/toga',
    packages=find_packages(exclude='tests'),
    install_requires=[
        'toga-core>=%s' % version,
    ],
    tests_require=[
        'toga-dummy==%s' % version
    ],
    license='New BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        # 'Operating System :: Microsoft :: Windows :: Windows 8',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Widget Sets',
    ],
    test_suite='tests',
)
