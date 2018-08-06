from setuptools import setup, find_packages

setup(
    name='tweepyutils',
    version='0.1',
    description='Utility extension for Tweepy.',
    author='Exceen',
    author_email='github@exceen.at',
    url='https://github.com/exceen/tweepyutils/',
    license='MIT license',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'tweepy==1.12',
    ],
    packages=find_packages(),
)
