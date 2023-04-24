cmake_minimum_required(VERSION 3.5)

project(MappaImperium LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(SFML 2.5
  COMPONENTS
    system window graphics network audio REQUIRED
    )

set(MAPPA_DEPENDENCIES
    gui.cpp
    player.cpp
    place.cpp
    mappamap.cpp
    faction.cpp)
add_executable(MappaImperium main.cpp ${MAPPA_DEPENDENCIES})
