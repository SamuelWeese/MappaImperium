#ifndef PLACE_H
#define PLACE_H

#include <string>
#include <SFML/Graphics/Sprite.hpp>
#include "player.h"


struct Vector2 {
    long double x;
    long double y;
};

class place
{
public:
    place();
    Vector2 location;
    std::string name;
    player *owner;
    sf::Sprite sprite;
    void tint(sf::Color);
};

#endif // PLACE_H
