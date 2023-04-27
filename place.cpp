#include "place.h"

int roll(int dxd)
{
    int total = 0;
    for (int i = 0; i < dxd; i++)
    {
        total += rand() % 6 + 1;
    }
    return total;
}
/*
place::place()
{

}
*/

place::place(Vector2 coords, std::string name, player* owner, sf::Sprite sprite)
{
    this->location = coords;
    this->name = name;
    this->owner = owner;
    this->sprite = sprite;
}

void place::draw(sf::RenderWindow *target)
{
    target->draw(this->sprite);
}

void place::tint(sf::Color aColor)
{
    this->sprite.setColor(aColor);
}
