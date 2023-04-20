#ifndef PLACE_H
#define PLACE_H

struct Vector2 {
    long double x;
    long double y;
};

class place
{
public:
    place();
    Vector2 location;
};

#endif // PLACE_H
