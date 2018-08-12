from setuptools import setup, find_packages

setup(
    name='tweepyutils',
    version='1.1',
    description='Utility extension for Tweepy.',
    author='Exceen',
    author_email='github@exceen.at',
    url='https://github.com/exceen/tweepyutils/',
    license='MIT License',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'tweepy>=1.12'
    ],
    packages=find_packages(),
    scripts=[
        'bin/tweepyutils',
        'bin/followings',
        'bin/tweet'
    ]
)
