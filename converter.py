import PySimpleGUI as sg

layout = [
    [sg.Input(key='-INPUT-'),
     sg.DropDown(['километры в мили', 'килограммы в фунты', 'секунды в минуты'], key='-UNITS-', default_value='километры в мили', readonly=True)],
    [sg.Button('Конвертировать', key='-CONVERT-'), sg.Text('Знаков после запятой:'), sg.Spin([0, 1, 2, 3, 4, 5], key='-LENGTH-')],
    [sg.Text('Вывод:', key='-OUTPUT-')]
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
                    output = round(float(input_value) * 0.621371, values['-LENGTH-'])
                    output_line = f'{input_value} в км равно {output} в милях.'
                case 'килограммы в фунты':
                    output = round(float(input_value) * 2.20462, values['-LENGTH-'])
                    output_line = f'{input_value} в кг равно {output} в фунтах.'
                case 'секунды в минуты':
                    output = round(float(input_value) / 60, values['-LENGTH-'])
                    output_line = f'{input_value} в сек. равно {output} в минутах.'

            window['-OUTPUT-'].update(f'Вывод: {output_line}')

window.close()
