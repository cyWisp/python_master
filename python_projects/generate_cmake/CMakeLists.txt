cmake_minimum_required(VERSION 3.10.2)
project(hello_world)
include_directories(${PROJECT_SOURCE_DIR})
add_executable(hello_world hello.c main.c )