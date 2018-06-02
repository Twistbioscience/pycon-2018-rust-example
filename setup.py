from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name='is_blank',
    version='0.1.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Rust',
        'Operating System :: POSIX',
    ],
    packages=['is_blank'],
    rust_extensions=[RustExtension('is_blank._fast_is_blank', 'Cargo.toml')],
    install_requires=[],
    setup_requires=['setuptools-rust>=0.9.2'],
    include_package_data=True,
    zip_safe=False,
)
