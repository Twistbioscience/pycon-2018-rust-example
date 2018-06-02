#![feature(proc_macro, specialization)]
extern crate pyo3;

use std::fs::File;
use std::io::prelude::*;

use pyo3::prelude::*;
use pyo3::py::modinit as pymodinit;

#[pymodinit(_fast_is_blank)]
fn init_mod(py: Python, m: &PyModule) -> PyResult<()> {
    #[pyfn(m, "is_blank")]
    fn is_blank(filepath: String) -> PyResult<bool> {
        let mut file = File::open(filepath)?;
        let mut content = String::new();
        file.read_to_string(&mut content)?;
        Ok(content.chars().all(|c| c.is_whitespace()))
    }

    Ok(())
}
