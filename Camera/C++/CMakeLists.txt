cmake_minimum_required(VERSION 3.31.6)

project(Camera)

find_package(OpenCV REQUIRED)
find_package(pybind11 REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)
target_include_directories(Camera PRIVATE ${OpenCV_INCLUDE_DIRS})
target_link_libraries(Camera ${OpenCV_LIBS})