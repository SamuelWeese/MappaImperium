#ifndef MAPPAMAP_H
#define MAPPAMAP_H

#include <SFML/Graphics.hpp>
#include <SFML/Graphics/Shader.hpp>
#include <cstdlib>
#include <vector>
#include <string>
#include "player.h">
#include "place.h"
int roll(int);

#define COLOR_WRAPPER(ARG) Vector4(ARG)

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

struct deity {
    std::string name;
    std::string symbol;
    std::string domain;
    std::vector<place *> sacred_sites;

};

class MappaMap
{
    sf::RenderWindow *window;

    sf::RenderTexture mapTexture;
    sf::Sprite mapBackGround;
    sf::Vector2f lastPos;
    const float brush_size = 25;

    unsigned int colorIndex;
    bool isDrawing;
    sf::CircleShape brush;

    std::vector<player> player_list;
    // 2.1
    deity generate_Deity();

public:
    MappaMap();
    MappaMap(sf::RenderWindow *);
    void draw(sf::RenderWindow*);
    void draw();
    void eventHandler(sf::Event);
};

#endif // MAPPAMAP_H
