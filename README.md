# Mappa Imperium

[Mappa Imperium](https://nookrium.itch.io/mappa-imperium) is a great little world building table top game designed by Nookrium. You should check it and [his other work out](https://nookrium.itch.io/)!


## This Project

This project (also poorly named Mappa Imperium) is a python based (originally cpp until classes + work took too much time) implementation of Mappa Imperium.

### Get Started

This project has no build options (as of yet). To run the project:


Install requirements:

```python3 -m install -r requirements.txt```

Run the app:

```python3 ./main.py```

## Currently Supported

### Rolling in chat window
- Use /r or /roll {x}d{y}!

![alt text](/readme.img/0.0.0.commands_example.png)

### Drawing on screen (WIP)
- Color selection is implemented, but I'm unhappy with it
- Width selection is supported, but the pen gets jagged when scaled up in width (WIP)

![alt text](/readme.img/0.0.3.drawing_example.png)

### Adding places with custom images (WIP)
- Currently images are supported to the exent they were in the [Jaran Project](https://github.com/kharanpv/AI_DnD). I plan on adding additional options for data storage once I rework drawing and image overlays.

![alt text](/readme.img/0.0.0.location_example.png)

## Future Work
This is the short list of things I intend to make headway on in the next month.
- Saving (most likely via pickle!)
- "Multiplayer"
- Build Options and Official Release

I'm currently active and trying to work on this project daily. If you have any suggestions, feel free to open an issue. This project will no longer be [ZeroVer](https://0ver.org/) compliant upon other people thinking it feels nice to use, and all the rules from Mappa Imperium are implemented robustly. What that means, I have yet to find out.
