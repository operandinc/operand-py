from setuptools import setup

setup(
    name='operand',
    version='0.2',
    license='MIT',
    author="Operand, Inc.",
    author_email='support@operand.ai',
    packages=['operand', 'operand.v1'],
    package_dir={
        'operand': '.',
        'operand.v1': './operand/v1',
    },
    url='https://github.com/operandinc/operand-py',
    keywords='semantic-search search nlp',
    install_requires=[
          'requests',
          'protobuf'
      ],
)