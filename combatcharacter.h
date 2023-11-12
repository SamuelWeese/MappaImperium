#ifndef COMBATCHARACTER_H
#define COMBATCHARACTER_H
#include "dice.h"

class combatCharacter
{
    // Abilities
    int strenth;
    int dexterity;
    int constitution;
    int wisdom;
    int intelligence;
    int charisma;

    // Proficencies

    // AC Calc
    int baseAC;
    int dexterityAC;
    int armorAC;
public:
    int getAC();
private:
    // Weapon Calc
    int weaponToHit;
    dice weaponDamage;
    int weaponRange;

public:
    int getToHit();
    int getDamage();
private:

public:
    combatCharacter();

    // Aurora

    // File Reading
};

#endif // COMBATCHARACTER_H
