cmake_minimum_required(VERSION 3.5)

project(MappaImperium LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(MAPPA_DEPENDENCIES
    player.cpp
    place.cpp
    mappamap.cpp
    faction.cpp)
add_executable(MappaImperium main.cpp ${MAPPA_DEPENDENCIES})
