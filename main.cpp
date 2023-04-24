#include <iostream>
#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>

/*

void myFunction(int a, int b = 1, int c = 2) {
    std::cout << a << " " << b << " " << c << std::endl;
}



int main()
{
    // Create a new render-window
    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML window");
    // Create a new render-texture
    sf::RenderTexture texture;
    if (!texture.create(500, 500))
        return -1;
    // The main loop
    sf::Shader aShader;

    while (window.isOpen())
    {
       // Event processing
       // ...
       // Clear the whole texture with red color
       texture.clear(sf::Color::Red);
       // Draw stuff to the texture
       //texture.draw(sprite);  // sprite is a sf::Sprite
       //texture.draw(shape);   // shape is a sf::Shape
       //texture.draw(text);    // text is a sf::Text
       // We're done drawing to the texture
       texture.display();
       // Now we start rendering to the window, clear it first
       window.clear();
       // Draw the texture
       sf::Sprite sprite(texture.getTexture());
       window.draw(sprite);
       // End the current frame and display its contents on screen
       window.display();
    }


}
*/
/*

#include <SFML/Graphics.hpp>
#include <vector>

int main()
{
    // create the window
    sf::RenderWindow window(sf::VideoMode(800, 600), "My window");
   std::vector <sf::Vertex> lines;
   sf::Texture texture;
   sf::Sprite sprite;
   texture.create(800,600);

   int mousedown = 0;
    // run the program as long as the window is open
   window.setFramerateLimit(30);

    while (window.isOpen())
    {
        // check all the window's events that were triggered since the last iteration of the loop
        sf::Event event;
        while (window.pollEvent(event))
        {
            // "close requested" event: we close the window
            if (event.type == sf::Event::Closed)
                window.close();
         else if ((event.type == sf::Event::MouseMoved) && (mousedown == 1))
         {
            lines.push_back(sf::Vertex(sf::Vector2f::Vector2(sf::Mouse::getPosition(window))));
         }
         else if (event.type == sf::Event::MouseButtonPressed)
         {
            mousedown = 1;
         }
         else if (event.type == sf::Event::MouseButtonReleased)
         {
            mousedown = 0;
            texture.update(window);
            lines.clear();
         }
      }

        window.clear(sf::Color::Black);

         window.draw(sprite);

      window.draw(&lines[0], lines.size(), sf::LinesStrip);

      sprite.setTexture(texture);
        window.display();

    }

    return 0;
}
*/
#include "mappamap.h"
#include <SFML/Graphics.hpp>
#include <vector>

int main(int argc, char **argv) {
    sf::RenderWindow window(sf::VideoMode(800, 600), L"SFML Drawing – C to clear, PageUp/PageDown to pick colors", sf::Style::Default);
    // Set a specific frame rate, since we don't want to
    // worry about vsync or the time between drawing iterations
    window.setVerticalSyncEnabled(false);
    window.setFramerateLimit(60);
/*
    // First we'll use a canvas to basically store our image
    sf::RenderTexture canvas;
    canvas.create(800, 600);
    canvas.clear(sf::Color::White);

    // Next we'll need a sprite as a helper to draw our canvas
    sf::Sprite sprite;
    sprite.setTexture(canvas.getTexture(), true);

    // Define some colors to use
    // These are all with very low alpha so we
    // can (over-)draw based on how fast we move the cursor
    const std::vector<sf::Color> colors = {
        sf::Color(255, 0, 0),
        sf::Color(255, 255, 0, 8),
        sf::Color(0, 255, 0, 8),
        sf::Color(0, 255, 255, 8),
        sf::Color(0, 0, 255, 8),
        sf::Color(255, 0, 255, 8)
    };

    // We'll need something to actually draw
    // For simplicity, I'm just drawing a circle shape
    // but you could also draw a line, rectangle, or something more complex
    const float brush_size = 25;
    sf::CircleShape brush(brush_size, 24);
    brush.setOrigin(brush_size, brush_size); // Center on the circle's center

    sf::Vector2f lastPos;
    bool isDrawing = false;
    unsigned int color = 0;

    // Apply some default color
    brush.setFillColor(colors[color]);

*/

//MappaMap
    MappaMap map(&window);


    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event)) {
            map.eventHandler(event);
            switch (event.type) {
            case sf::Event::Closed:
                window.close();
                break;
                }
        }

        // Clear the window
        window.clear(sf::Color(64, 64, 64));

        // Draw our canvas
        map.draw();

        // Show the window
        window.display();
    }
    return 0;
}
