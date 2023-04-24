#include "mappamap.h"

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
// 3.1
const std::string Races[11]
{
    "Demonkind",
    "Seafolk",
    "Smallfolk",
    "Reptilian",
    "Dwarves",
    "Humans",
    "Elves",
    "Greenskins",
    "Animalfolk",
    "Giantkind",
    "Player's Choice"
};
// 3.2
const std::string SymbolsF[36]{
    "Flame",
    "Horse",
    "Boar",
    "Lion",
    "Dragon",
    "Hydra",
    "Lightning Bolt",
    "Bird",
    "Mountain",
    "Sun",
    "Moon",
    "Leaf",
    "Tree",
    "Claw",
    "Spider",
    "Grain",
    "Bow",
    "Horeshoe",
    "Harp",
    "Fish",
    "Anvil",
    "Wolf",
    "Wings",
    "Skull",
    "Axe",
    "Diamond",
    "Flower",
    "Apple",
    "Cup",
    "Spade",
    "Sword",
    "Beholder",
    "Scorpion",
    "Crab",
    "Unicorn",
    "Star"
};

const std::vector<sf::Color> colors = {
    sf::Color(255, 0, 0),
    sf::Color(255, 255, 0, 8),
    sf::Color(0, 255, 0, 8),
    sf::Color(0, 255, 255, 8),
    sf::Color(0, 0, 255, 8),
    sf::Color(255, 0, 255, 8)
};

MappaMap::MappaMap()
{

    mapTexture.create(800, 600);
    mapTexture.clear(sf::Color(207, 183, 120));
    mapBackGround.setTexture(mapTexture.getTexture(), true);
    this->isDrawing = false;
    colorIndex = 0;
    brush = sf::CircleShape(brush_size, 24);
    brush.setFillColor(colors[colorIndex]);

}

deity MappaMap::generate_Deity()
{
    deity aDeity;
    bool roll_for_name = true;
    for (auto aPlayer : this->player_list)
    {
        aDeity.domain = Domains[roll()-1];
        aDeity.symbol = Symbols[roll()-1];
        std::string deity_name = "";
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

void MappaMap::draw(sf::RenderWindow *renderTarget)
{
    renderTarget->draw(this->mapBackGround);
}

void MappaMap::eventHandler(sf::Event event)
{
    switch (event.type) {
    case sf::Event::KeyPressed:
        switch (event.key.code) {
            case sf::Keyboard::C:
                // Clear our mapTexture
                mapTexture.clear(sf::Color::White);
                mapTexture.display();
                break;
            case sf::Keyboard::PageUp:
                // Get next color
                this->colorIndex = (this->colorIndex + 1) % colors.size();
                // Apply it
                brush.setFillColor(colors[colorIndex]);
                break;
            case sf::Keyboard::PageDown:
                // Get previous color
                colorIndex = (colorIndex - 1) % colors.size();
                // Apply it
                brush.setFillColor(colors[colorIndex]);
                break;
        }
        break;
    case sf::Event::Resized:
        {
            // Window got resized, update the view to the new size
            sf::View view(window->getView());
            const sf::Vector2f size(window->getSize().x, window->getSize().y);
            view.setSize(size); // Set the size
            view.setCenter(size / 2.f); // Set the center, moving our drawing to the top left
            window->setView(view); // Apply the view
            break;
        }
    case sf::Event::MouseButtonPressed:
        // Only care for the left button
        if (event.mouseButton.button == sf::Mouse::Left) {
            isDrawing = true;
            // Store the cursor position relative to the mapTexture
            lastPos = window->mapPixelToCoords({event.mouseButton.x, event.mouseButton.y});

            // Now let's draw our brush once, so we can
            // draw dots without actually draging the mouse
            brush.setPosition(lastPos);

            // Draw our "brush"
            mapTexture.draw(brush);

            // Finalize the texture
            mapTexture.display();
        }
        break;
    case sf::Event::MouseButtonReleased:
        // Only care for the left button
        if (event.mouseButton.button == sf::Mouse::Left)
            isDrawing = false;
        break;
    case sf::Event::MouseMoved:
        if (isDrawing)
        {
            // Calculate the cursor position relative to the mapTexture
            const sf::Vector2f newPos(window->mapPixelToCoords(sf::Vector2i(event.mouseMove.x, event.mouseMove.y)));

            // I'm only using the new position here
            // but you could also use `lastPos` to draw a
            // line or rectangle instead
            brush.setPosition(newPos);

            // Draw our "brush"
            mapTexture.draw(brush);

            // Finalize the texture
            mapTexture.display();
            break;
        }
    }
}
