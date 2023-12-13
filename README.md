# Point Rotation Project

## Overview

This Python project implements a point rotation functionality 
using the tkinter GUI library for user input and visualization. 
The rotation calculations are performed based on the entered parameters, 
and the results are displayed as a plot and a DataFrame, which can be saved for further 
use.

Project was designed to simplify research activities at SOLARIS National Radiation Center. Especially on the PIRX beamline.
Where a rotatable sample holder might be used for X-ray Absorption Spectroscopy measurements. Calculation of the 2D point rotation
facilitates the process of measurement planning. 

## Features

- **Point Rotation:** Calculate and visualize the rotation of a point in 2D space.
- **User Interface:** Utilize tkinter for a simple and interactive user interface.
- **DataFrame Display:** Display the rotation data in a pandas DataFrame within the GUI.
- **File Saving:** Save the rotation data as a text or CSV file.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Required Python libraries: matplotlib, pandas, tkinter

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/szpytmus/2D_Angle_Transformer.git
   
2. Download the executable file from the Download folder on this repository. ‼️(Will be added in the future)

## Usage

1. If the .exe file is not used run the `main.py` file in the project directory:

   ```bash
   python main.py
   
2. The tkinter GUI will prompt you to enter the rotation parameters and angle range.
3. Click the "Submit" button to perform the rotation calculation.
4. The results will be displayed in a plot, and you can view the rotation data in a DataFrame within the GUI.
5. Optionally, you can save the rotation data as a text or CSV file using the "Save as File" button.
6. Repeat the new calculation.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub flow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

## Code Style

Project's code style follows PEP 8 conventions.