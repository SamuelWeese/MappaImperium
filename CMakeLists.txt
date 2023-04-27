cmake_minimum_required(VERSION 3.5)

project(MappaImperium LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(SFML 2.5
  COMPONENTS
    system window graphics REQUIRED
    )

set(MAPPA_DEPENDENCIES
    deity.cpp
    gui.cpp
    game_state.cpp
    player.cpp
    place.cpp
    mappamap.cpp
    pausemenu.cpp
    #faction.cpp
    )
add_executable(MappaImperium main.cpp ${MAPPA_DEPENDENCIES})

target_link_libraries(
 ${PROJECT_NAME}
 LINK_PUBLIC
 sfml-graphics
)
