with open("REAADME.md",'r',encoding = 'utf-8')as f:
    long_description = f.read()
import setuptools

__version__ = "0.0.0"

REPO_NAME ="Kidney-Disease-Classification-Deep-Learning-End-to-End-Project"
AUTHOR_USER_NAME ="chitaki10"
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL ="chitakin876@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version =__version__,
    author = AUTHOR_USER_NAME,
    author_email =AUTHOR_EMAIL,
    description = "a small python package for cnn app",
    long_description = long_description,
    LOng_description_content = 'text/markdown',
)