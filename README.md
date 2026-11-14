🚤 Boat on River with Waves using PyOpenGL
An interactive computer graphics project developed using Python and PyOpenGL, demonstrating fundamental graphics algorithms, geometric transformations, and mathematical animation techniques through a realistic river scene.

📌 Project Overview
This project simulates a boat floating on a dynamic river with animated waves. The scene includes a moving boat, rotating sun rays, drifting clouds, flying birds, layered water effects, and user-controlled interactions.

The project integrates concepts from multiple Computer Graphics laboratory assignments, including primitive drawing, Bresenham circle generation, geometric transformations, and sine-wave based animation.

🎥 Project Demonstration
📺 YouTube Demo Video

https://youtu.be/xFVNyMfc9UY

Watch the complete project demonstration, animation behavior, and user interactions.

✨ Features
Realistic animated river waves using sine functions
Boat movement synchronized with wave motion
Automatic boat tilting based on wave slope
Flying birds with flapping wings
Moving clouds
Rotating sun rays
Animated flag movement
Multi-layer transparent water effects
Interactive keyboard controls
Smooth real-time animation
🖥️ Technologies Used
Python 3
PyOpenGL
OpenGL
GLUT
GLU
Mathematics (Sin, Cos, Trigonometry)
🎓 Computer Graphics Concepts Implemented
Lab 1: Graphics Primitives
The project uses basic OpenGL primitives such as:

Polygon
Rectangle
Lines
Filled Shapes
Used for:

Boat body
Hills
River bank
Sails
Water surfaces
Lab 2: Bresenham Circle Algorithm
The Midpoint/Bresenham Circle Algorithm is implemented to draw circles efficiently.

Applications:

Sun
Clouds
Boat portholes
Lab 3: Geometric Transformations
Several transformation techniques are used:

Translation
Used to move:

Boat
Clouds
Birds
Rotation
Used for:

Boat tilting along wave slope
Rotating sun rays
Scaling
Used for:

Boat direction flipping
Cloud size variation
Lab 4: Mathematical Animation
Wave motion is generated using trigonometric functions.

Techniques:

Sine Wave Animation
Cosine-Based Slope Calculation
Time-Based Dynamic Motion
Used for:

River waves
Bird wing movement
Flag waving effect
🎮 Controls
Key	Action
← Left Arrow	Decrease boat speed
→ Right Arrow	Increase boat speed
+	Increase wave height
-	Decrease wave height
Space	Pause / Resume animation
R	Reset project
ESC	Exit application
📂 Project Structure
Boat-on-River-with-Waves/
│
├── boat_on_river.py
├── README.md
└── assets/
🌊 Animation Workflow
Generate dynamic water waves using sine functions.
Calculate wave height at each position.
Determine wave slope using cosine functions.
Move the boat along the wave surface.
Rotate the boat according to slope angle.
Animate clouds, birds, and flag continuously.
Render all scene components in real-time.
🚀 How to Run
Clone Repository
git clone https://github.com/MAHEEOSD/Boat-on-River-with-Waves-.git
Install Dependencies
pip install PyOpenGL PyOpenGL_accelerate
Run Project
python boat_on_river.py
📸 Project Output
The application generates an animated river environment featuring:

Dynamic water waves
Floating boat
Natural landscape
Interactive controls
Real-time graphical effects
👨‍💻 Author
Mubtasim CSE Student, BAUST

⭐ Academic Objective
This project was developed to demonstrate the practical implementation of fundamental Computer Graphics concepts, including:

Graphics Primitives
Bresenham Circle Algorithm
Geometric Transformations
Mathematical Animation
Real-Time Rendering
📜 License
This project is developed for educational and academic purposes.
