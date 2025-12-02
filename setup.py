from setuptools import setup

setup(name='eupy',
        version='1.2.1',
        description='An API to interact with the chatrooms at euphoria.leet.nu',
        author='Justin Chadwell',
        author_email='jedevc@gmail.com',
        url='https://github.com/jedevc/euphoria-python',
        license='MIT',
        packages=['euphoria'],
        install_requires=['websocket-client']
)
