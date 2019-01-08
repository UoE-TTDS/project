from setuptools import setup, find_packages
import sys

with open("tests/requirements-tests.txt", 'r') as f:
    test_requirements = f.read().split('\n')

with open("requirements.txt", 'r') as f:
    requirements = f.read().split('\n')

if '--dev' in sys.argv:
    with open("requirements-dev.txt", 'r') as f:
        requirements += f.read().split('\n')

    index = sys.argv.index('--dev')
    sys.argv.pop(index)  # Removes the '--dev'

setup(
    name='ttds_project',
    version='1.0',
    packages=find_packages(),
    url='',
    license='MIT',
    author='',
    author_email='',
    description='',
    setup_requires=requirements,
    tests_require=test_requirements,
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov'
        ]
    },
    use_2to3_exclude_fixers=[],
)