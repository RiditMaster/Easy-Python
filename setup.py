from setuptools import setup, find_packages

setup(
    name='Easy Python',
    version='0.1',
    license='MIT',
    author="Ridit Jangra",
    author_email='riyanjangra9@gmail.com',
    packages=find_packages('easyput.py,screen.py,p.py,speak.py'),
    package_dir={'': ''},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)