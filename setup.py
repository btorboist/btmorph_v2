from setuptools import setup, find_packages
setup(
    name = 'btmorph2',
    packages = find_packages(),
    version = '2.0.0',
    description = 'Object-oriented library to analyze neuronal structure',
    long_description=open('README.rst', 'r').read(),
    author = 'Benjamin Torben-Neilsen',
    author_email = 'b.torbennielsen@oist.jp',
    url = 'https://github.com/btorboist/btmorph_v2',
    license = '',
    download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
    keywords = ['dendrites', 'neuroscience'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Languge :: Python :: 2',
        'Programming Languge :: Python :: 2.7',
    ],
    install_requires = ['h5py', 'numpy', 'scipy', 'matplotlib', 'ipython',
                        'pycrypto'],
    include_package_data = True,
    extras_require = {
        'test': ['nosetests']
    }
)
