# Blender Automated Render Project

This project provides an automated setup for generating, modifying, and rendering 3D scenes in Blender. Using Python scripts, it automates tasks including 3D model manipulation, setting up scenes, and rendering animations. It also allows for organized test management and caching of simulation data.

## Project Structure

- **`main.py`**: Main entry script that initiates the Blender scene setup, executes tests, and optionally renders animations.
- **`modules/`**: Contains all reusable modules such as object creation, transformation, selection management, physics setup, and rendering tools.
- **`tests/`**: Includes test files (`test0.py`, `test1.py`, etc.) to generate various configurations within Blender for testing purposes.
- **`homework files`**: A custom scene configuration used as the primary setup in this project.
- **`scene/`**: Stores generated `.blend` files and render outputs.

## Requirements

- **Blender**: Ensure Blender is installed on your system and added to your system path for command-line access.
- **Python**: Blender’s internal Python interpreter is used to execute scripts.

## Usage

### Running the Project
To run `main.py` in Blender’s background mode and execute the setup:

```bash
blender --background --python main.py
