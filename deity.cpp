#include "deity.h"

deity::deity()
{
    this->owner = nullptr;
    this->name = generateName();
    this->symbol = generateSymbol();
    this->domain = generateDomain();

}

deity::deity(player *owner, std::string name, std::string symbol, std::string domain)
{
    this->owner = owner;
    this->name = name;
    this->symbol = symbol;
    this->domain = domain;
}

std::string deity::generateName()
{
    std::string deity_name = "";
    short syllabols = (roll()%2) + (roll()%2);
    for (int i = 0; i < syllabols; i++)
    {
        deity_name += Names[rand()%36];
    }
    return deity_name;
}

std::string deity::generateSymbol()
{
    return Symbols[roll()-1];
}

std::string deity::generateDomain()
{
    return Domains[roll()-1];
}
