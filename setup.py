from setuptools import setup

setup(name='Bot',
      version='0.0.1',
      author='Konrad Jopek',
      author_email='kjopek@gmail.com',
      url='http://www.agh.edu.pl',
      license='BSD',
      package_dir={'':'lib'},
      packages=['bot'],
      package_data={'bot': ['sql/*.sql']},
      data_files=[('conf', 'config/config.yaml')],
      setup_requires=['ssjp>=0.0.1', 'PyYAML>=3.0.0'],
      install_requires=['ssjp>=0.0.1', 'PyYAML>=3.0.0']
      )