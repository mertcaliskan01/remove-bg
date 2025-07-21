from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="remove-bg",
    version="1.0.0",
    author="Mert Çalışkan",
    author_email="mcaliskanmert@gmail.com",
    description="Resimlerin arka planını kaldıran ve 40 farklı arka plan seçeneği sunan Python uygulaması",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mertcaliskan01/remove-bg",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "remove-bg=bg_remover:main",
        ],
    },
    keywords="background removal, image processing, AI, rembg, pillow",
    project_urls={
        "Bug Reports": "https://github.com/mertcaliskan01/remove-bg/issues",
        "Source": "https://github.com/mertcaliskan01/remove-bg",
        "Documentation": "https://github.com/mertcaliskan01/remove-bg#readme",
    },
) 