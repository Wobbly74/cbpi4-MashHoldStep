from setuptools import setup

setup(name='cbpi4-MashHoldStep',
      version='0.0.2',
      description='CraftBeerPi Plugin based on the standard mash steps to add ability to hold kettle temperature when AutoMode set to Off',
      author='Wobbly',
      author_email='neil@milne.com',
      url='https://github.com/Wobbly74/cbpi4-MashHoldStep',
      license='GPLv3',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-MashHoldStep': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-MashHoldStep'],
)