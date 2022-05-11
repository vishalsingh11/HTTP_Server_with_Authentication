cmake_minimum_required(VERSION 3.4)

project(MySimpleHttpServer)
find_package(CURL REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(MySimpleHttpServer curl)