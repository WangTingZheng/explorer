import setuptools


with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="file-explorer",
    version="0.0.0",
    author="WangTingZheng",
    author_email="wangtingzheng@outlook.com",
    description="A simple python cli file browser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WangTingZheng/explorer",
    packages=setuptools.find_packages(),
    install_requires=["pick"],
    entry_points={"console_scripts": ["explorer = explorer.command:main"]},
)
