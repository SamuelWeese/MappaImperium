#ifndef DICE_H
#define DICE_H

#include <stdint.h>

class dice
{

public:
    uint_fast64_t numSides;
    uint_fast64_t numDice;
    dice(uint_fast64_t numSides = 20, uint_fast64_t numDice = 1);
    uint_fast64_t advantageRoll();
    uint_fast64_t disadvantageRoll();
    uint_fast64_t roll();
    uint_fast64_t catchRoll();

};

#endif // DICE_H
