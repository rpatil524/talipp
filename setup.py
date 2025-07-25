import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()
requirements = [line.strip() for line in requirements]

with open("VERSION", "r") as fh:
    version = fh.read()

setuptools.setup(
    name="talipp",
    version=version,
    author="nardew",
    author_email="talipp.pyth@gmail.com",
    description="talipp - Incremental Technical Analysis Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nardew/talipp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    install_requires=requirements,
    python_requires='>=3.8.0',
)
