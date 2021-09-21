from setuptools import setup

setup(
    name='polarstereo-lonlat-convert-py',
    version='1.0.0',
    description=(
        'Python functions for converting polar stereographic coordinates.'
    ),
    url='https://github.com/nsidc/polarstereo-lonlat-convert-py',
    author='NSIDC Development Team',
    packages=['polar_convert'],
    license='MIT',
    install_requires=[
        'numpy >=1.21.2,<1.22',
    ],
    python_requires='>=3.6, <4.0',
)
