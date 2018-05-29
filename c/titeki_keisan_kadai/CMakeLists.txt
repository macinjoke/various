cmake_minimum_required(VERSION 3.10)
project(titeki_keisan_kadai)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_CXX_COMPILER /usr/local/bin/g++-6)
set(CMAKE_C_COMPILER /usr/local/bin/gcc-6)
# enable openmp using -fopenmp
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -fopenmp")


add_executable(titeki_keisan_kadai main.cpp)

