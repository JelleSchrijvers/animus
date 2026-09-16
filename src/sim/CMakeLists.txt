add_library(animus_sim STATIC
    body.cpp
)

target_include_directories(animus_sim PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
