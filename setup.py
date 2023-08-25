from setuptools import setup, find_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Remove your trash in any folder',
      author='OKravchenko',
      author_email='alya.v.kravchenko@gmail.com',
      packages=find_packages(),
      entry_points={"console_scripts":["clean-folder = clean_folder.clean:main"]},
      install_requires=["numpy", "Pillow",],
      )