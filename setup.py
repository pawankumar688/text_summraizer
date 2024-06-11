import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description =f.read()

__version__ = "0.0.0"

REPO_NAME = "text_summraizer"
AUTHOR_USER_NAME = "pawankumar688"
SRC_REPO ="textSummarier"
AUTHOR_EMAIL = "pawanjumarfromhuc.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL ,
    description="A small python package of NLP applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pawankumar688/text_summraizer",
    project_urls={
        'Source': 'https://github.com/pawankumar688/text_summarizer',
        'Tracker': 'https://github.com/pawankumar688/text_summarizer/issues',
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    
    )
