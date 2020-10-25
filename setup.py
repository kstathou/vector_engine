from setuptools import setup
from setuptools import find_namespace_packages

common_kwargs = dict(
    version="0.1.0",
    license="MIT",
    # install_requires=required,
    long_description=open("README.md").read(),
    url="https://github.com/kstathou/vector_engine",
    author="Kostas Stathoulopoulos",
    author_email="k.stathou@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">3.6",
    include_package_data=False,
)

setup(
    name="vector_engine",
    packages=find_namespace_packages(where="vector_engine.*"),
    **common_kwargs
)
