from setuptools import setup

setup(
   name='exemplo',
   version='1.0.0',
   description='Exemplo Python3',
   author='Guilherme de Lemos',
   author_email='guilherme.eti@gmail.com',
   packages=['exemplo'],  #same as name
   install_requires=['numpy', 'scipy'], #external packages as dependencies
)