Color Detection App

This project is a Color Detection App built with Streamlit, OpenCV, and Pandas. It allows users to upload an image and click on any part of the image to detect the color at that pixel. The application displays the color name and its RGB values.

Project Structure

├── H1.py               # Main application file
├── colors.csv          # Dataset containing color names and RGB values
├── README.md           # Documentation (You are here!)

Requirements

To run this project, ensure you have the following dependencies installed:

pip install opencv-python-headless
pip install pandas
pip install streamlit

Dataset

The colors.csv file contains the following columns:

Color: The basic color group

ColorName: The name of the color

Hex: The hexadecimal code of the color

R: Red value

G: Green value

B: Blue value

The app uses these values to match the closest color to the clicked pixel.

Usage

To run the application, use the following command:

streamlit run H1.py

After running the command, a local Streamlit server will start. You can upload an image and click on the image to detect colors.

How It Works

The user uploads an image.

The image is displayed using Streamlit.

When the user clicks the 'Detect Color' button:

OpenCV registers click events on the image window.

The RGB values are captured from the clicked pixel.

The app finds the closest matching color from the dataset.

The color name and its RGB values are displayed.

Future Improvements

Add a color history panel to keep track of clicked colors.

Improve UI/UX for a smoother experience.

Support for real-time video color detection.

Author

Created by Your Name.

Feel free to contribute and make improvements! If you encounter any issues, feel free to open an issue or submit a pull request.

