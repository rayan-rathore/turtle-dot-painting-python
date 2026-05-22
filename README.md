Hirst-Inspired Spot Painting Generator 🎨
---------
A beginner-friendly Python project that uses the turtle graphics library to automatically generate beautiful, randomized dot paintings inspired by the famous artist Damien Hirst.

This project helps to understand how to use loops, coordinate positioning, and randomized RGB color palettes to create digital art. As a bonus, it automatically saves your generated masterpiece as an .eps file!

---------
Features
Automated Art Generation: Automatically draws a uniform grid of 405 colored dots (15 rows by 27 columns).

Randomized Palette: Uses the random module to pick from a list of 27 RGB colors.

Auto-Save Functionality: Captures the final turtle screen and saves it to your computer as an .eps (Encapsulated PostScript) file, complete with a unique timestamp.

Clean Exit: The program keeps the drawing window open until you click on it to close.

------------

Prerequisites
To run this project, you will need Python installed on your computer. The turtle and datetime modules are built into standard Python, so you don't need to install them separately.

If you plan to extract your own colors from images (using the commented-out code in the script), you will need to install the colorgram.py library. (pip install colorgram.py)

---------
## How the Code Works

Here is a quick breakdown of the logic for beginners learning Python:

* **Color Extraction (Commented Out):** The script includes a block of code using colorgram. This is how the custom colors list was originally created! It extracts the 30 most prominent colors from a source image (image.jpg) and formats them into RGB tuples. 
* **Turtle Setup:** We create a turtle named aqua, hide its icon, and lift its pen (aqua.penup()) so it doesn't draw lines between the dots.
* **The Grid System:** We set a starting x and y coordinate (Top-Left of the screen). 
  * The **Outer Loop** for y in range(15): controls the rows. After every row is complete, it resets the X position and moves the Y position down by 50 pixels.
  * The **Inner Loop** for _ in range(27): controls the columns. It stamps a 20-pixel dot in a random color, then moves forward by 50 pixels.
* **Saving the Canvas:** We access the underlying Tkinter canvas from the Turtle screen and use the .postscript() method to export it. We use the datetime module to ensure every saved painting has a unique name so they don't overwrite each other.

---

💡 Tip: Converting .eps to .png
Because .eps is a vector file format (mostly used for printing), it might not easily open on your phone or regular photo viewer.

You can quickly convert your saved artwork into a standard .png image for free online:

Go to CloudConvert's EPS to PNG tool. https://cloudconvert.com/eps-to-png

Upload your generated painting_YYYYMMDD_HHMMSS.eps file.

Click Convert and download your high-quality .png image!
