from distutils.core import setup

setup(name='smart_defaults',
      version='0.0.1',
      description="",
      author='',
      author_email='',
      packages=['smart_defaults', 'smart_defaults.providers'],
      install_requires=["kao_fn"],
      dependency_links=['git+http://github.com/cloew/KaoFn']
     )