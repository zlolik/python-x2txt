import glob
from distutils.core import setup

# get all of the scripts
scripts = glob.glob('bin/*')

setup(
  description='A pure python-based utility to extract text and images '
              'from docx files.',
  author='Ankush Shah',
  author_email='ankush.shah.nitk@gmail.com',
  url='https://github.com/ankushshah89/python-docx2txt',
  download_url='https://github.com/ankushshah89/python-docx2txt/tarball/0.8',
  keywords=['python', 'docx', 'text', 'images', 'extract'],
  scripts=scripts,
  name='x2txt',
  packages=['x2txt'],
  version='0.1',
  classifiers=[],
)
