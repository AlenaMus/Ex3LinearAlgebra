# Rectangle Rotation Visualizer

This Python script provides a visual demonstration of a 2D geometric transformation using linear algebra. It displays a rectangle that rotates around its center for 5 seconds.

## Core Concepts Illustrated

- **Vector Representation**: The corners of the rectangle are defined as vectors.
- **Geometric Center**: The center of the rectangle is calculated by finding the mean of the corner vectors.
- **Rotation Matrix**: A 2D rotation matrix is used to apply the rotation transformation.
- **Linear Transformation**: The rotation is applied by translating the rectangle to the origin, multiplying its vectors by the rotation matrix, and translating it back.

## Dependencies

The program is built using the following Python libraries:

- `numpy`: For all numerical and linear algebra operations (vectors, matrices, matrix multiplication).
- `matplotlib`: For creating the plot and animating the visualization.

## How to Run

1.  **Install Dependencies**:
    If you are on a Debian-based system like Ubuntu, you can install the required libraries using `apt`:
    ```bash
    sudo apt install python3-numpy python3-matplotlib
    ```
    Alternatively, if you are using a virtual environment, you can use `pip`:
    ```bash
    pip install numpy matplotlib
    ```

2.  **Execute the Script**:
    ```bash
    python3 rotate_rectangle.py
    ```
    This will open a window displaying the animation.
