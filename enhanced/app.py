# Written by: Gregoria Ramirez
# Course: CS-499 Computer Science Capstone
# Description: Main file that launches the Dash app.

# Enhancements (Software Design and Engineering):
# - Moved layout and callbacks into separate files to follow MVC structure and keep things modular.
# - Replaced outdated app.run_server() with app.run() for better compatibility.
# - Simplified the launch code to make the app easier to read, maintain, and expand.

# Original version created in Feb 2025 and enhanced by me for the final capstone.

from dash import Dash
from model.view import layout
from controller import register_callbacks

# Enhancement (Software Design and Engineering): Loads layout from separate view file to support modular design
app = Dash(__name__)
app.layout = layout

# Enhancement (Software Design and Engineering): Connects modular callback functions from controller file
register_callbacks(app)

# Enhancement (Software Design and Engineering): Uses updated app.run() instead of deprecated app.run_server()
app.run(debug=True, port=8550)

