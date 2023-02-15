import PySimpleGUI as sg

# Define the layout of the GUI
layout = [
    [sg.Text('Enter your name:'), sg.InputText()],
    [sg.Button('Submit'), sg.Button('Cancel')]
]

# Create the GUI window
window = sg.Window('GitHub Action', layout)

# Run the event loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        # Exit the event loop if the user closes the window or clicks the Cancel button
        break
    elif event == 'Submit':
        # Perform some action based on the user's input
        name = values[0]
        print(f'Hello, {name}!')

# Close the window
window.close()
