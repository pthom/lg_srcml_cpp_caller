#include <pybind11/pybind11.h>


#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)


namespace py = pybind11;


void py_init_module_lg_srcml_cpp_caller(py::module& m);


// This builds the native python module `_lg_srcml_cpp_caller`
// it will be wrapped in a standard python module `lg_srcml_cpp_caller`
PYBIND11_MODULE(_lg_srcml_cpp_caller, m)
{
    #ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
    #else
    m.attr("__version__") = "dev";
    #endif

    py_init_module_lg_srcml_cpp_caller(m);
}
