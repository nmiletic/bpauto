from setuptools import setup

setup(name='bpauto',
      version='0.1',
      description='BP test creation automation',
      url='http://github.com/storborg/funniest',
      author='Nemanja Miletic',
      author_email='nemanja@nemanjamiletic.com',
      license='MIT',
      packages=['bpauto'],
      install_requires=[
          'pyyaml',
          'scp',
          'paramiko',
          'pykwalify'
      ],
      scripts=['bin/bpgentcl'],
      zip_safe=False)
