import PySimpleGUI as sg

layout = [
    [sg.Input(key='-INPUT-'),
     sg.DropDown(['километры в мили', 'килограммы в фунты', 'секунды в минуты'], key='-UNITS-')],
    [sg.Button('Конвертировать', key='-CONVERT-')],
    [sg.Text('Результат конвертации', key='-OUTPUT-')]
]

window = sg.Window('Simple Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'километры в мили':
                    output = float(input_value) * 0.621371
                    output_line = f'{input_value} в км равно {output} в милях.'
            window['-OUTPUT-'].update(output_line)

window.close()
