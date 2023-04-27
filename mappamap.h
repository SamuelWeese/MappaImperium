#ifndef MAPPAMAP_H
#define MAPPAMAP_H

#include <SFML/Graphics.hpp>
#include <SFML/Graphics/Shader.hpp>
#include <cstdlib>
#include <vector>
#include <string>
#include "player.h"
#include "place.h"

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

public:
    //MappaMap();
    MappaMap(sf::RenderWindow *);
    void draw(sf::RenderWindow*);
    void draw();
    void eventHandler(sf::Event);
    sf::Color getColor(Vector2 coords);
};

#endif // MAPPAMAP_H
