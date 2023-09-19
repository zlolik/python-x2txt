from distutils.core import setup

setup(
  name='x2txt',
  packages=['x2txt'],
  version='0.1',
  description='Utilities to extract text from docx and xlsx files.',
  author='zlolik',
  author_email='lolikandr@gmail.com',
  url='https://github.com/zlolik/python-x2txt',
  download_url='https://github.com/zlolik/python-x2txt/tarball/0.1',
  keywords=['python', 'docx', 'xlsx', 'text', 'images', 'extract'],
  install_requires=['openpyxl']
  scripts=['docx2txt', 'xlsx2txt'],
  classifiers=[],
)
