import tkinter as tk
from tkinter import ttk, messagebox

class UnitConverter(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        # Final color palette
        self.color1 = '#1E2022'  # Rich Navy for main background
        self.color2 = '#00ADB5'  # Vibrant Cyan for accents and buttons
        self.color3 = '#EEEEEE'  # Light Gray for text and input backgrounds
        self.color4 = '#393E46'  # Muted Silver for borders and highlights
        self.user_defined_conversions = []
        self.conversions_available = [
            'km --> mi', 'mi --> km', 'kg --> lbs', 'lbs --> kg',
            '°F --> °C', '°C --> °F', 'm² --> ft²', 'ft² --> m²',
            'hectare --> acre', 'acre --> hectare'
        ]
        self.setup_ui()

    def setup_ui(self):
        self.configure(bg=self.color1)
        self.pack(fill=tk.BOTH, expand=True)
        
        # Main Heading with border and background
        self.title_frame = tk.Frame(self, bg=self.color2, highlightbackground=self.color4, highlightthickness=2)
        self.title_frame.grid(row=0, columnspan=3, pady=(10, 10), padx=20, sticky=tk.EW)
        self.title_label = tk.Label(self.title_frame, text="Unit Converter", bg=self.color2, fg=self.color1, font=('Arial', 28, 'bold'))
        self.title_label.pack(pady=5)
        
        # Sections Heading Row with underline
        self.basic_conversions_label = tk.Label(self, text="Basic Conversions", bg=self.color1, fg=self.color3, font=('Arial', 20, 'bold', 'underline'))
        self.basic_conversions_label.grid(row=1, column=0, padx=20, pady=(5, 10), sticky=tk.W)

        self.new_conversions_label = tk.Label(self, text="Add New Conversions", bg=self.color1, fg=self.color3, font=('Arial', 20, 'bold', 'underline'))
        self.new_conversions_label.grid(row=1, column=2, padx=20, pady=(5, 10), sticky=tk.W)
        
        # Vertical separator line
        self.separator = tk.Frame(self, bg=self.color4, width=2)
        self.separator.grid(row=2, column=1, rowspan=3, sticky="ns", pady=(10, 10))
        
        # Basic Conversions Section
        self.conversion_var = tk.StringVar(value=self.conversions_available[0])
        self.select_conversion = ttk.Combobox(
            self, values=self.conversions_available, textvariable=self.conversion_var,
            justify=tk.CENTER, state='readonly', font=('Arial', 16)
        )
        self.select_conversion.grid(row=2, column=0, padx=20, sticky='ew')
        self.select_conversion.bind("<<ComboboxSelected>>", lambda event: self.convert_value())

        # Input and output frame with black border
        self.value_frame = tk.Frame(self, bg=self.color1, highlightthickness=2, highlightbackground=self.color4)
        self.value_frame.grid(row=3, column=0, padx=20, pady=20, sticky='ew')
        
        self.value_to_convert = self.create_entry(self.value_frame, 0)
        self.value_to_convert.bind("<KeyRelease>", lambda event: self.convert_value())

        self.arrow_label = tk.Label(self.value_frame, text="→", font=('Arial', 32), bg=self.color1, fg=self.color3)
        self.arrow_label.grid(column=1, row=0)
        
        self.converted_value = self.create_entry(self.value_frame, 2, state=tk.DISABLED)

        # Add New Conversions Section
        self.add_user_defined_section()

    def create_entry(self, parent, column, state=tk.NORMAL):
        entry = tk.Entry(parent, font=('Arial', 18), bg=self.color3, fg=self.color1,
                         justify=tk.CENTER, state=state, width=15, highlightthickness=1, highlightbackground=self.color4)
        entry.grid(column=column, row=0, ipady=5)
        return entry

    def add_user_defined_section(self):
        self.user_frame = tk.Frame(self, bg=self.color1)
        self.user_frame.grid(row=2, column=2, rowspan=2, padx=20, pady=20, sticky='nsew')
        
        self.var1_label = tk.Label(self.user_frame, text="From:", bg=self.color1, fg=self.color2, font=('Arial', 16))
        self.var1_label.grid(column=0, row=0)
        self.var1_entry = tk.Entry(self.user_frame, bg=self.color3, width=15, font=('Arial', 16), highlightthickness=1, highlightbackground=self.color4)
        self.var1_entry.grid(column=1, row=0)
        
        self.var2_label = tk.Label(self.user_frame, text="To:", bg=self.color1, fg=self.color2, font=('Arial', 16))
        self.var2_label.grid(column=2, row=0)
        self.var2_entry = tk.Entry(self.user_frame, bg=self.color3, width=15, font=('Arial', 16), highlightthickness=1, highlightbackground=self.color4)
        self.var2_entry.grid(column=3, row=0)

        self.formula_label = tk.Label(self.user_frame, text="Formula (e.g., x * 2):", bg=self.color1, fg=self.color2, font=('Arial', 16))
        self.formula_label.grid(column=0, row=1, columnspan=2)
        self.formula_entry = tk.Entry(self.user_frame, bg=self.color3, font=('Arial', 16), highlightthickness=1, highlightbackground=self.color4)
        self.formula_entry.grid(column=2, row=1, columnspan=2, sticky='ew')
        
        # Add conversion and delete buttons with black border
        self.add_conversion_button = tk.Button(self.user_frame, text="Add Conversion", bg=self.color2, font=('Arial', 16),
                                               command=self.add_user_defined_conversion, highlightthickness=1, highlightbackground=self.color4)
        self.add_conversion_button.grid(column=1, row=2, pady=10, padx=10)
        
        # Delete selected and delete all conversions buttons
        self.delete_selected_conversion_button = tk.Button(self.user_frame, text="Delete Selected Conversion", bg=self.color2, font=('Arial', 16),
                                                           command=self.delete_selected_conversion, highlightthickness=1, highlightbackground=self.color4)
        self.delete_selected_conversion_button.grid(column=2, row=2, pady=10, padx=10)

        self.delete_conversions_button = tk.Button(self.user_frame, text="Delete All Added Conversions", bg=self.color2, font=('Arial', 16),
                                                   command=self.delete_added_conversions, highlightthickness=1, highlightbackground=self.color4)
        self.delete_conversions_button.grid(column=3, row=2, pady=10, padx=10)

    def add_user_defined_conversion(self):
        var1, var2, formula = self.var1_entry.get(), self.var2_entry.get(), self.formula_entry.get()
        if var1 and var2 and formula:
            new_conversion = f"{var1} --> {var2}"
            self.user_defined_conversions.append((new_conversion, var1, var2, formula))
            self.conversions_available.append(new_conversion)
            self.select_conversion['values'] = self.conversions_available

            # Clear entries after adding
            self.var1_entry.delete(0, tk.END)
            self.var2_entry.delete(0, tk.END)
            self.formula_entry.delete(0, tk.END)

            messagebox.showinfo("Conversion Added", f"'{new_conversion}' added successfully.")
            
            # After adding new conversion, reset and recalculate the result
            self.conversion_var.set(new_conversion)
            self.convert_value()

    def delete_selected_conversion(self):
        current_conversion = self.conversion_var.get()
        # Only remove if the selected conversion is user-defined
        for conversion in self.user_defined_conversions:
            if conversion[0] == current_conversion:
                self.user_defined_conversions.remove(conversion)
                self.conversions_available.remove(current_conversion)
                self.select_conversion['values'] = self.conversions_available
                self.reset_conversion()
                messagebox.showinfo("Conversion Deleted", f"Deleted '{current_conversion}' successfully.")
                return
        messagebox.showwarning("Cannot Delete", "Selected conversion is a default conversion and cannot be deleted.")

    def delete_added_conversions(self):
        self.user_defined_conversions.clear()
        self.conversions_available = [
            'km --> mi', 'mi --> km', 'kg --> lbs', 'lbs --> kg',
            '°F --> °C', '°C --> °F', 'm² --> ft²', 'ft² --> m²',
            'hectare --> acre', 'acre --> hectare'
        ]
        self.select_conversion['values'] = self.conversions_available
        self.reset_conversion()

        messagebox.showinfo("All Conversions Deleted", "All user-defined conversions have been deleted.")

    def reset_conversion(self):
        if self.conversion_var.get() not in self.conversions_available:
            self.conversion_var.set(self.conversions_available[0])
            self.convert_value()  # Recalculate the conversion result and update the output

    def convert_value(self):
        conversion = self.conversion_var.get()
        input_value = self.value_to_convert.get()
        try:
            value = float(input_value)
        except ValueError:
            self.display_result("Invalid input")
            return

        # Check for negative values for Celsius and Fahrenheit
        if conversion == '°C --> °F' and value < -273.15:
            messagebox.showwarning("Invalid Input", "Temperature in Celsius cannot be below -273.15°C.")
            return
        elif conversion == '°F --> °C' and value < -459.67:
            messagebox.showwarning("Invalid Input", "Temperature in Fahrenheit cannot be below -459.67°F.")
            return

        result = None
        if conversion in [x[0] for x in self.user_defined_conversions]:
            for conv, var1, var2, formula in self.user_defined_conversions:
                if conversion == conv:
                    local_dict = {var1: value}
                    try:
                        result = eval(formula, {"__builtins__": None}, local_dict)
                    except Exception as e:
                        result = f"Error: {e}"
                    break
        else:
            result = self.perform_basic_conversion(conversion, value)

        self.display_result(result)

    def display_result(self, result):
        self.converted_value.config(state=tk.NORMAL)
        self.converted_value.delete(0, tk.END)
        self.converted_value.insert(0, result)
        self.converted_value.config(state=tk.DISABLED)

    def perform_basic_conversion(self, conversion, value):
        match conversion:
            case 'km --> mi': return value * 0.621371
            case 'mi --> km': return value * 1.60934
            case 'kg --> lbs': return value * 2.20462
            case 'lbs --> kg': return value * 0.453592
            case '°F --> °C': return (value - 32) * 5 / 9
            case '°C --> °F': return (value * 9 / 5) + 32
            case 'm² --> ft²': return value * 10.7639
            case 'ft² --> m²': return value / 10.7639
            case 'hectare --> acre': return value * 2.47105
            case 'acre --> hectare': return value / 2.47105

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1400x350')
    root.title('Unit Converter')
    UnitConverter(root)
    root.mainloop()
