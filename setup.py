#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Stello - 中文静态网站生成器的安装脚本
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取 README 作为长描述
here = Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

# 读取依赖
requirements = (here / "requirements.txt").read_text(encoding="utf-8").strip().split("\n")
requirements = [r.strip() for r in requirements if r.strip()]

setup(
    name="stello",
    version="1.0.0",
    description="中文静态网站生成器 - A Static Site Generator for Chinese Users",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Stello Contributors",
    author_email="admin@wangru.net",
    url="https://github.com/wangru2025/stello",
    project_urls={
        "Bug Tracker": "https://github.com/wangru2025/stello/issues",
        "Documentation": "https://github.com/wangru2025/stello#readme",
        "API Documentation": "https://github.com/wangru2025/stello/blob/main/API.md",
        "Source Code": "https://github.com/wangru2025/stello",
        "Changelog": "https://github.com/wangru2025/stello/blob/main/CHANGELOG.md",
    },
    license="MIT",
    packages=find_packages(exclude=["examples", "tests", "docs"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "stello=stello.main:main",
        ],
    },
    keywords=[
        "static-site-generator",
        "ssg",
        "markdown",
        "chinese",
        "dsl",
        "website",
        "blog",
        "documentation",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Office/Business",
        "Topic :: Text Processing :: Markup :: Markdown",
    ],
    zip_safe=False,
)
