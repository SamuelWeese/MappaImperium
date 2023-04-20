#include "mappamap.h"

using namespace std;
MappaMap::MappaMap()
{


}

const std::string Domains[6]{"a geography",
                          "something in nature",
                          "an art or craft",
                          "an endeavor",
                          "something from around the home",
                          "something grim"
};

const std::string Symbols[6]{"a weapon",
                          "a tool",
                          "an animal",
                          "a plant",
                          "something natural",
                          "a body part"
};

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


Deity MappaMap::generate_Deity()
{
    Deity aDeity;
    bool roll_for_name = true;
    for (auto aPlayer : this->player_list)
    {
        aDeity.domain = Domains[roll()-1];
        aDeity.symbol = Symbols[roll()-1];
        string deity_name = "";
        if (roll_for_name)
        {
            short syllabols = (roll()%2) + (roll()%2);
            for (int i = 0; i < syllabols; i++)
            {
                deity_name += Names[rand()%36];
            }
        } else { deity_name = "You pick one!";}
    }
    return aDeity;
}
