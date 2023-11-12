#include "dice.h"
#include <cstdlib>

dice::dice(uint_fast64_t sides, uint_fast64_t dice)
{
    this->numDice = dice;
    this->numSides = sides;
}
uint_fast64_t dice::roll()
{
    return (rand() % this->numSides) +1;
}

uint_fast64_t dice::advantageRoll()
{
    uint_fast64_t a = this->roll();
    uint_fast64_t b = this->roll();
    return a > b ? a : b;
}

uint_fast64_t dice::disadvantageRoll()
{
    uint_fast64_t a = this->roll();
    uint_fast64_t b = this->roll();
    return a < b ? a : b;
}

