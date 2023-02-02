from setuptools import setup

setup(
    name='operand',
    version='0.2.2',
    license='MIT',
    author="Operand, Inc.",
    author_email='support@operand.ai',
    packages=['operand', 'mcp.operand.v1', 'mcp.file.v1', 'mcp.tenant.v1'],
    package_dir={
        'operand': '.',
        'mcp.operand.v1': './mcp/operand/v1',
        'mcp.file.v1': './mcp/file/v1',
        'mcp.tenant.v1': './mcp/tenant/v1',
    },
    url='https://github.com/operandinc/operand-py',
    keywords='semantic-search search nlp',
    install_requires=[
          'requests',
          'protobuf'
      ],
)