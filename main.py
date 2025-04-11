import json
import PySimpleGUI as sg
from utils import load_adr_rules, detect_adr

# Load ADR rules from JSON file
adr_rules = load_adr_rules()

# Define the GUI layout
sg.theme('LightBlue3')  # Setting an attractive theme

layout = [
    [sg.Text('SmartCare ADR Detector', font=('Any 18'))],
    [sg.Text('Enter patient symptoms (comma separated):', font=('Any 12'))],
    [sg.InputText(key='-SYMPTOMS-', size=(50, 1))],
    [sg.Text('Enter current medications (comma separated):', font=('Any 12'))],
    [sg.InputText(key='-MEDICATIONS-', size=(50, 1))],
    [sg.Button('Check ADR', font=('Any 12')), sg.Button('Exit', font=('Any 12'))],
    [sg.HorizontalSeparator()],
    [sg.Multiline(key='-OUTPUT-', size=(70, 15), font=('Courier', 11), disabled=True)]
]

# Create the Window
window = sg.Window('SmartCare ADR Detector [Hackathon Edition]', layout, resizable=True)

def process_inputs(values):
    # Get user inputs and standardize: strip and lower-case
    symptoms = [s.strip().lower() for s in values['-SYMPTOMS-'].split(',') if s.strip()]
    medications = [m.strip().lower() for m in values['-MEDICATIONS-'].split(',') if m.strip()]
    alerts = detect_adr(symptoms, medications, adr_rules)
    return alerts

# Event Loop
while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
        
    if event == 'Check ADR':
        alerts = process_inputs(values)
        output = "🔍 ADR Detection Results:\n" + "-" * 40 + "\n"
        if alerts:
            for alert in alerts:
                output += f"{alert['severity']} Possible ADR Detected: '{alert['symptom']}' + '{alert['medication']}'\n"
        else:
            output += "✅ No ADRs detected. Patient is safe for now.\n"
        output += "\n🛡️ Tip: Always re-check symptoms after starting new medications."
        window['-OUTPUT-'].update(output)

window.close()
