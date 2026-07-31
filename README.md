# gravity-paint
Your mouse cursor is a planet. Particles orbit it. You paint with gravity.

An interactive particle simulation where floating particles are attracted to your cursor using real inverse-square gravity physics. As particles orbit, they leave glowing trails that form unique, beautiful art — every session creates a different masterpiece.

📸 Preview
text

                    ● ← Mouse Cursor (Gravity Source)
                   /|\
                  / | \
                 ↙  ↓  ↘
               ●    ●    ●   ← Particles pulled toward cursor
              ╱    ╱    ╲
             ●    ●      ●   ← Orbital paths
              ╲  ╱      ╱
               ●●      ●     ← Glowing trails left behind
                ╲      ╱
                 ● ─ ─ ●

        Move cursor slowly = tight spirals
        Move cursor fast   = wild flings
        Click              = spawn burst of new particles
✨ Features
Real Physics — Inverse-square gravity law (same as actual planets)
Particle Trails — Particles leave fading glowing tails as they orbit
Interactive — Attract, repel, spawn, and reset particles
Zero Dependencies — Uses only Python's built-in tkinter
60 FPS Animation — Smooth real-time simulation
Unique Art Every Time — No two sessions produce the same result
🚀 Setup
Prerequisites
Python 3.6+ installed on your system
tkinter (comes pre-installed with Python on most systems)
Verify tkinter is Installed
Bash

python -c "import tkinter; print('tkinter OK')"
If tkinter is missing:

Ubuntu/Debian:

Bash

sudo apt-get install python3-tk
Fedora:

Bash

sudo dnf install python3-tkinter
macOS:

Bash

# tkinter comes with Python from python.org
# If using Homebrew Python:
brew install python-tk
Windows:

Bash

# tkinter is included with the standard Python installer
# Reinstall Python from python.org if missing
Installation
Bash

# 1. Clone or download the project
git clone <repository-url>
cd gravity-paint

# 2. No dependencies to install! Run directly.
python gravity_paint.py
🎮 Controls
Control	Action
Move Mouse	Attract particles toward cursor (gravity)
Left Click	Spawn a burst of 8 new particles at cursor
Right Click	Toggle between Attract ↔ Repel mode
Space	Reset — clear all particles and start fresh
Escape	Quit the application
📖 Usage Guide
Basic Usage
Bash

python gravity_paint.py
A window will open with 80 colorful particles floating randomly. Move your mouse to attract them.

Creating Art
🌀 Tight Spirals
Move your mouse slowly in small circles
Particles will form tight, beautiful orbital rings
💥 Explosions
Right-click to switch to repel mode
Move cursor near particles — they scatter outward
Right-click again to switch back — watch them return
🎆 Bursts
Click rapidly in different spots
Creates overlapping trails from multiple gravity wells
🌊 Waves
Move mouse in a sine wave pattern across the screen
Particles create wave-like trail patterns
🎨 Galaxy Art
Start with default particles
Move mouse slowly in a large circle (center of screen)
Click a few times to add more particles
Wait 30 seconds
You'll see a spiral galaxy form!
Tips for Best Results
Tip	Why
Start with slow movements	Lets particles settle into orbits
Use both attract and repel	Creates interesting collision patterns
Click in clusters, not randomly	Creates denser, more visible trails
Let it run for a minute	Trails accumulate into complex art
Press Space to reset anytime	Start fresh with a new canvas
🔧 Configuration
Edit these values at the top of 
gravity_paint.py
 to customize:

Python

# Window size
WIDTH, HEIGHT = 900, 700

# Starting number of particles
NUM_PARTICLES = 80

# Gravity strength (higher = stronger pull)
GRAVITY = 3000

# Friction (1.0 = no friction, lower = more friction)
DAMPING = 0.995

# How many frames the trail lasts
TRAIL_LENGTH = 40

# Background color (hex)
BG = "#0a0a1a"

# Particle colors (add/remove hex codes)
COLORS = [
    "#ff6b6b", "#feca57", "#48dbfb", "#ff9ff3",
    "#54a0ff", "#5f27cd", "#01a3a4", "#f368e0",
]
Suggested Tweaks
Want to...	Change...	To...
Stronger gravity	GRAVITY	5000
More particles	NUM_PARTICLES	150
Longer trails	TRAIL_LENGTH	80
Slower particles	DAMPING	0.990
Darker background	BG	#050510
📁 Project Structure
text

gravity-paint/
├── gravity_paint.py    # Main application (single file)
└── README.md           # This file
That's it. One file. No dependencies. No setup.

🧠 How It Works
Physics Engine
Each frame (60 times per second), for every particle:

text

1. Calculate distance to cursor
2. Calculate gravity force:  F = G / (distance² + 100)
3. Apply force to velocity:  vx += (dx/dist) × force
4. Apply friction:           vx *= 0.995
5. Move particle:            x += vx
6. Store position for trail
7. Draw trail + particle
Trail Rendering
Trails fade from bright to dark using color multiplication:

text

For each trail point:
    alpha = point_index / total_points    # 0.0 (old) → 1.0 (new)
    color = original_color × alpha × 0.6  # Dimmer = older
    draw line segment with that color
Performance Management
Oldest particles are removed when count exceeds 300
Old canvas drawings are deleted each frame (prevents memory leak)
Trail length is capped at 40 points per particle
🐛 Troubleshooting
Problem	Solution
No module named tkinter	Install tkinter (see Setup section)
Window doesn't appear	Check if Python is running: python --version
Laggy/slow animation	Reduce NUM_PARTICLES to 40
Particles disappear	Increase TRAIL_LENGTH to 60
Nothing happens on click	Make sure window is focused (click on it first)
📜 License
MIT License — free to use, modify, and distribute.

🙏 Acknowledgments
Built with Python and tkinter
Inspired by orbital mechanics and generative art
Physics based on Newton's Law of Universal Gravitation
<div align="center">
Made with ❤️ and physics

Every session creates a unique masterpiece.

</div>
