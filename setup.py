import setuptools


setuptools.setup(
    name='apriltag',
    version='1.0.0',
    author='sinback',
    author_email='sinback@picklerobot.com',
    description='Apriltag Python utilities',
    long_description='Forked from https://github.com/swatbotics/apriltag',
    url='https://github.com/Pickle-Robot/apriltag',
    packages=['apriltag'],
    package_dir={'apriltag': 'python/apriltag'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: The Regents of the University of Michigan',
        'Operating System :: Linux',
    ],
    python_requires='>=3.0',
)
