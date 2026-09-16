#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "animus/body.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_animus_core, m) {
    m.doc() = "Animus C++ physics core (pybind11 bindings)";

    py::class_<animus::Body>(m, "Body")
        .def(py::init<>())
        .def("reset", &animus::Body::reset,
             "Reset the simulation and return the initial observation")
        .def("step", &animus::Body::step,
             py::arg("action"), py::arg("dt") = 0.01,
             "Advance the simulation by dt seconds given an action vector")
        .def("get_observation", &animus::Body::get_observation,
             "Return the current observation vector");
}
