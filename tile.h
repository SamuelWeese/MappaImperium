#ifndef TILE_H
#define TILE_H
#include <SFML/Graphics.hpp>

class tile
{
    // some kind of display method
    // sprite
    // texture? or reference to texture?
    // we probably need a texture handler
    sf::Sprite drawValue;
    sf::Window *drawTarget;


public:
    tile();
     void draw();
};

#endif // TILE_H
