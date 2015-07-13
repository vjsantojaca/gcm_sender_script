from setuptools import setup

setup(
    name='gcm_sender_python',
    version='1.0',
    packages=['gcm'],
    author='Victor Santoja',
    author_email='victorsantoja@gmail.com',
    description='Send message using GCM service',
    keywords='android gcm push notification google cloud messaging',
    install_requires=['requests', 'mysql-python'],
)