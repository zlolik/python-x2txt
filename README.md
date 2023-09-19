## python-x2txt

Utilities to extract text from docx and xlsx files. 

The code is taken and adapted from [python-docx2txt](https://github.com/ankushshah89/python-docx2txt).


## Text from docx

a. From command line:
```bash
# extract text
docx2txt file.docx
# extract text and images
docx2txt -i /tmp/img_dir file.docx
```
b. From python:
```python
from x2txt import text_from_docx
# extract text
text = text_from_docx("file.docx")
# extract text and write images in /tmp/img_dir
text = text_from_docx("file.docx", "/tmp/img_dir") 
```

## Text from xlsx

a. From command line:
```bash
# extract text
xlsx2txt file.xlsx
```
b. From python:
```python
from x2txt import text_from_xlsx
# extract text
text = text_from_xlsx("file.xlsx")
```
