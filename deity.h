#ifndef DEITY_H
#define DEITY_H

#include <string>
#include "place.h"
#include "player.h"

// 2.2
const std::string Domains[6]{"a geography",
                          "something in nature",
                          "an art or craft",
                          "an endeavor",
                          "something from around the home",
                          "something grim"
};
// 2.3
const std::string Symbols[6]{"a weapon",
                          "a tool",
                          "an animal",
                          "a plant",
                          "something natural",
                          "a body part"
};
// 2.4
const std::string Names[36]{
    "mith",
    "tri",
    "dar",
    "gor",
    "an",
    "va",
    "col",
    "sige",
    "dir",
    "era",
    "altas",
    "remea",
    "fir",
    "alga",
    "lorra",
    "shiro",
    "velen",
    "amron",
    "for",
    "ened",
    "ziri",
    "red",
    "saur",
    "baal",
    "li",
    "serat",
    "cho",
    "maht",
    "alidren",
    "esh",
    "sae",
    "rah",
    "on",
    "tin",
    "ti",
    "ah"
};
// 2.5
const std::string Sacred_Sites[11]
{
    "bottomless pit",
    "lone mountain",
    "hot spring",
    "rock tower",
    "small lake",
    "ancient tree",
    "cave",
    "volcano",
    "grove",
    "henge",
    "geyser"
};


class deity
{
    player* owner;
    std::string name;
    std::string generateName();
    std::string symbol;
    std::string generateSymbol();
    std::string domain;
    std::string generateDomain();
    std::vector<place *> sacred_sites;
public:
    deity();
    deity(player *aPlayer, std::string name, std::string symbol, std::string domain);

};

#endif // DEITY_H
