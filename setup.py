import setuptools

setuptools.setup(
    name='aodotpy',
    version='0.2.1',
    packages=['ao',],
    license='MIT',
    description = 'Python wrappers for ao',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'xiaojay',
    author_email = 'xiaojay@gmail.com',
    install_requires=['requests', 'python-jose', 'arweave-python-client', 'arseeding'],
    url = 'https://github.com/permadao/ao.py',
    download_url = 'https://github.com/xiaojay/permadao/archive/refs/tags/v0.2.1.tar.gz',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
