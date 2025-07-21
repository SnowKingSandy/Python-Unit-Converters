import sys
import tkinter as tk
from tkinter import ttk  # Import ttk for Combobox

class UnitConverter(tk.Frame):

    def __init__(self, root):

        self.color1 = '#0e2d41'
        self.color2 = '#e776a2'
        self.color3 = '#dfdfd3'

        self.conversions_available = ['km --> mi',
                                     'mi --> km',
                                     'kg --> lbs',
                                     'lbs --> kg',
                                     '°F --> °C',
                                     '°C --> °F',
                                     'm² --> ft²',
                                     'ft² --> m²',
                                     'hectare --> acre',
                                     'acre --> hectare']
        super().__init__(root, bg=self.color1)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(2, weight=1)
        self.create_widgets()

    def create_widgets(self):

        self.title = tk.Label(
            self.main_frame,
            bg=self.color1,
            fg=self.color2,
            font=('Arial', 22, 'bold'),
            text='Unit Converter'
        )

        self.title.grid(column=0, row=0, sticky=tk.EW, pady=(10, 20))

        def callback_trace_conversion(*args):
            self.convert_value()

        self.conversion = tk.StringVar()
        self.conversion.set(self.conversions_available[0])
        self.conversion.trace('w', callback_trace_conversion)

        self.select_conversion = ttk.Combobox(
            self.main_frame,
            values=self.conversions_available,
            textvariable=self.conversion,
            justify=tk.CENTER,
            state='readonly'
        )

        self.select_conversion.grid(column=0, row=1, sticky='nsew', padx=50)

        self.container_values = tk.Frame(self.main_frame, bg=self.color1)
        self.container_values.columnconfigure(1, weight=1)
        self.container_values.grid(column=0, row=2, sticky=tk.NSEW, padx=50, pady=40)

        def value_validation(value):
            if not value or value == '-':
                return True

            try:
                value = float(value)
            except ValueError:
                return False

            return True

        value_validation_command = self.register(value_validation)

        self.value_to_convert = tk.Entry(
            self.container_values,
            bg=self.color3,
            fg=self.color1,
            selectbackground=self.color1,
            selectforeground=self.color2,
            font=('Arial', 14),
            highlightthickness=0,
            border=0,
            justify=tk.CENTER,
            width=11,
            validate='key',
            validatecommand=(value_validation_command, '%P')
        )

        self.value_to_convert.grid(column=0, row=0, sticky=tk.N, ipady=3)
        self.value_to_convert.bind('<KeyPress>', self.call_convert_value_delay)

        right_arrow_label = tk.Label(
            self.container_values,
            bg=self.color1,
            fg=self.color3,
            text='\u2192',
            font=('Arial', 20),
            justify=tk.CENTER
        )

        right_arrow_label.grid(column=1, row=0, sticky=tk.N)

        self.converted_value = tk.StringVar()
        self.entry_converted_value = tk.Entry(
            self.container_values,
            bg=self.color3,
            fg=self.color1,
            disabledbackground=self.color3,
            disabledforeground=self.color1,
            font=('Arial', 14),
            highlightthickness=0,
            border=0,
            justify=tk.CENTER,
            width=11,
            state=tk.DISABLED,
            cursor='arrow',
            textvariable=self.converted_value
        )

        self.entry_converted_value.grid(column=2, row=0, sticky=tk.N, ipady=3)

    def call_convert_value_delay(self, event):
        self.main_frame.after(100, self.convert_value)

    def convert_value(self):
        self.converted_value.set("")  # Clear previous conversion result
        conversion = self.conversion.get()

        if not self.value_to_convert.get():
            self.converted_value.set("Enter a Value.")
            return

        value_to_convert_local = float(self.value_to_convert.get())

        match conversion:
            case 'km --> mi':
                self.converted_value.set(f'{value_to_convert_local * 0.621371: .2f}')
            case 'mi --> km':
                self.converted_value.set(f'{value_to_convert_local * 1.60934: .2f}')
            case 'kg --> lbs':
                self.converted_value.set(f'{value_to_convert_local * 2.20462: .2f}')
            case 'lbs --> kg':
                self.converted_value.set(f'{value_to_convert_local * 0.453592: .2f}')
            case '°F --> °C':
                self.converted_value.set(f'{(value_to_convert_local - 32) * 5 / 9: .2f}')
            case '°C --> °F':
                self.converted_value.set(f'{(value_to_convert_local * (9 / 5)) + 32: .2f}')
            case 'm² --> ft²':
                self.converted_value.set(f'{value_to_convert_local * 10.7639: .2f}')
            case 'ft² --> m²':
                self.converted_value.set(f'{value_to_convert_local / 10.7639: .2f}')
            case 'hectare --> acre':
                self.converted_value.set(f'{value_to_convert_local * 2.47105: .2f}')
            case 'acre --> hectare':
                self.converted_value.set(f'{value_to_convert_local / 2.47105: .2f}')


operating_system = sys.platform
root = tk.Tk()
unit_converter_app = UnitConverter(root)
root.title('Unit Converter')

if 'win' in operating_system:
    root.geometry('450x210')
elif 'linux' in operating_system:
    root.geometry('450x210')
elif 'darwin' in operating_system:
    root.geometry('450x230')

root.resizable(width=False, height=False)
root.mainloop()