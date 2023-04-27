#ifndef PLACE_H
#define PLACE_H

#include <string>
#include <SFML/Graphics.hpp>
#include "player.h"

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

int roll(int dxd = 1);

struct Vector2 {
    long double x;
    long double y;
};

class place
{
public:
    Vector2 location;
    std::string name;
    player *owner;
    sf::Sprite sprite;

    //place();
    place(Vector2, std::string name, player *owner, sf::Sprite sprite);

    void draw(sf::RenderWindow *);

    void tint(sf::Color);
};

#endif // PLACE_H
