cmake_minimum_required(VERSION 3.18)
project(animus_sim LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

# --- pybind11 -----------------------------------------------------------
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)

execute_process(
  COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmakedir
  OUTPUT_VARIABLE pybind11_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

find_package(pybind11 CONFIG REQUIRED)

# --- sim library (pure C++, no Python knowledge) -------------------------
add_subdirectory(src/sim)

# --- Python bindings module -----------------------------------------------
pybind11_add_module(_animus_core src/bindings/bindings.cpp)
target_link_libraries(_animus_core PRIVATE animus_sim)
target_include_directories(_animus_core PRIVATE src/sim/include)

# Install the compiled extension straight into the python package
install(TARGETS _animus_core LIBRARY DESTINATION animus)