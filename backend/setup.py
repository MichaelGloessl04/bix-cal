from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A brief description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/your_project_name",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "sqlalchemy",
        "uvicorn",
        "httpx",
        "pytest"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Lice nse :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
