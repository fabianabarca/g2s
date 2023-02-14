from setuptools import find_packages, setup

setup(
    name='gtfs2series',
    packages=find_packages(include=['gtfs2series']),
    version='0.0.0',
    description='Transform GTFS Realtime data into multivariate time series.',
    author='Fabián Abarca',
    license='MIT',
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'requests',
    ],
)
