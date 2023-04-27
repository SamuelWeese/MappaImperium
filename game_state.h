#ifndef GAME_STATE_H
#define GAME_STATE_H

#include <vector>
#include "mappamap.h"


class game_state
{
    //MappaMap map;
    std::vector<player> players;
public:
    game_state();
    void eventHandler();


};

#endif // GAME_STATE_H
