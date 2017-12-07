from setuptools import setup

setup(name='aocframework',
      version='0.2',
      description='Framework for solving tasks at adventofcode.com',
      url='https://github.com/roboxv/aocframework',
      author='robox',
      author_email='root@roboxv.pro',
      license='WTFPL',
      packages=['aocframework'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
