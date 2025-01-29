from setuptools import setup, find_packages

setup(
    name="mlops3_1",
    version="0.1",
    description="Credit default analysis package",
    author="Michael Ivanov",
    packages=find_packages(),
    install_requires=[
        # не забыть указать зависимости
    ],
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)

