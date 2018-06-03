# Example of creating a Rust module to be used from Python

This is based on this [example](https://github.com/PyO3/pyo3/tree/master/examples/word-count) from the PyO3 repo 

Requires Python 3.6+ and Rust nightly

Best way to install Rust and use the nightly toolchain is with [rustup](https://rustup.rs/)

    $ rustup install nightly
    $ rustup default nightly

Then install the Python dependencies (recommended in virtualenv) 

    $ pip install -r requirements.txt

Then build the package and install it (first time will take a while as Cargo download the dependencies and compiles them)

    $ python setup.py install

## Running the tests

If you want to run the tests, first create the fixture files (only need to run this once)

    $ python tests/create_fixtures.py

The, simply run the tests with pytest

    $ py.test
