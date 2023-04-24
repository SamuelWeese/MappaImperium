#ifndef MAPPAMAP_H
#define MAPPAMAP_H

#include <SFML/Graphics.hpp>
#include <cstdlib>
#include <string>
#include "player.h">
int roll(int dxd = 1)
{
    int total = 0;
    for (int i = 0; i < dxd; i++)
    {
        total += rand() % 5 + 1;
    }
    return total;
}

#define DIRT_COLOR sf::Color(244,164,96)
#define WATER_COLOR sf::Color(202, 240, 246)
//TODO SAM
#define BEACH_COLOR
#define GRASS_COLOR

// TABLE 1.2
#define SAVANNA_COLOR
#define WETLANDS_COLOR
#define HILLS_COLOR
#define LAKE_COLOR
#define RIVER_COLOR
#define FOREST_COLOR
#define MOUNTAINS_COLOR
#define DESERT_COLOR
#define JUNGLE_COLOR
#define CANYON_COLOR
#define VOLCANO_COLOR

// TABLE 1.3
#define LAKE_COLOR
#define GLACIER_COLOR
#define

struct Deity {
    std::string name;
    std::string symbol;
    std::string domain;
    std::vector<place *> sacred_sites;

};

class MappaMap
{
    const sf::Shader dirtColor = "void main() " \
    "{"\
        // transform the vertex position
        "gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;" \

        // transform the texture coordinates
        "gl_TexCoord[0] = gl_TextureMatrix[0] * gl_MultiTexCoord0;" \

        // forward the vertex color
        "gl_FrontColor = gl_Color;" \
    "}";

    std::vector<player> player_list;
    // 2.1
    Deity generate_Deity();

public:
    MappaMap();
};

#endif // MAPPAMAP_H
