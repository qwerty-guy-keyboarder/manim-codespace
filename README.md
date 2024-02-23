# Manim Workshop Codespace

Forking this repository to your personal GitHub
account will allow you to use GitHub Codespaces
to get started with manim community edition using
just your web browser.

# Getting Started

## Set up GitHub Codespaces

1. Fork the repository (by clicking the fork button on the top right of your screen)
2. Click the green code button, then under codespaces click "Create codespace on main."

## Rendering 

The command to render a scene is `manim render -ql main.py TanLine`. Use the Terminal to run this command. If a Terminal is not visible in your Codespace, use the keyboard shortcut ``[Ctrl/Cmd]+[Shift]+[`]`` to make it appear.

You can now view the video by looking under the folder `media/videos/main` and then clicking on the video which will have the name of your scene. You may need to click the refresh icon `⟳` if your video file does not appear at first.

We can also define the quality (default is 1920x1080 60FPS). We can add `-ql` for 854x480 15FPS, `-qm` for 1280x720 30FPS, `-qh` for 1920x1080 60FPS, `-qp` for 2560x1440 and `-qk` for 3840x2160 60FPS. \
For example, `manim render -ql main.py Riemann` will render the scene at 854x480 15FPS. Note, lower quality videos render faster, so it is adviced to render low quality videos while coding, and higher quality videos when you need to export them. 

To get more options and help with rendering, type `manim render --help`.

## Learning Resources 

[Manim CE Tutorial Page](https://docs.manim.community/en/stable/tutorials/index.html) (the quickstart page should give you a quick idea of the basics) \
[Manim CE Example Page](https://docs.manim.community/en/stable/examples.html) (looking at the examples to get ideas and understand how they did it) \
[Manim Beginner Video](https://www.youtube.com/watch?v=KHGoFDB-raE) (a really good explanation of manim concepts)

Take your time and experiment with the concepts as you are learning them, have fun :)
