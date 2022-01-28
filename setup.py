from setuptools import setup

setup(name='db_connector',
      version='0.1',
      description='A plugin to easily handle mysql connections',
      author='Benoît de Witte',
      author_email='bw@oncodna.com',
      license='MIT',
      packages=['db_connector'],
      install_requires = [
            'mysql-connector-python',
            'schematics',
            'configparser'
      ],
      zip_safe=False)