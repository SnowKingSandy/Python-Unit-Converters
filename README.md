# Python Tkinter Unit Converter Collection 

This repository houses two distinct, fully functional unit converter applications developed using Python and its standard GUI library, Tkinter. These applications serve as excellent examples of Tkinter's capabilities, showcasing two different approaches to UI design and application logic. One is a powerful, extensible tool for users who need custom functionality, while the other is a streamlined, minimalist application designed for speed and simplicity.

Both projects are self-contained and demonstrate core concepts of GUI development, including widget management, event handling, and state management.

-----

## Advanced Unit Converter with Custom Functions (`UC + User-Def Ftns WIP.py`)

This application is a feature-rich and highly flexible unit converter designed for power users. Its most significant feature is the ability for users to define, save, and use their own custom conversion formulas on the fly, making it an adaptable tool for specialized or niche calculations not covered by standard converters.

The user interface is thoughtfully designed with a two-panel layout, separating the primary conversion tool from the section where new conversions are created. This is achieved using Tkinter's `grid` layout manager, which allows for precise control over widget placement. A modern, high-contrast color scheme (`#1E2022` navy, `#00ADB5` cyan) is used to enhance readability and provide a professional aesthetic.

### Key Features 

  * **User-Defined Conversions**: The core feature allows users to input "From" and "To" units and a corresponding mathematical `formula` to create new, reusable conversions. The application dynamically updates the dropdown list of available conversions.
  * **Conversion Management**: Users have full control over their custom entries. They can delete a specific conversion from the dropdown list or use a dedicated button to delete all user-added conversions at once, resetting the list to the default set.
  * **Robust Error Handling**: The application provides user-friendly feedback using `messagebox`. It warns users about invalid numerical input and includes specific checks to prevent physically impossible calculations, such as temperatures below absolute zero.
  * **Dynamic Calculation Engine**: For user-defined formulas, the application safely uses Python's `eval()` function to parse and execute the mathematical expression. This is implemented securely by providing a restricted scope, which prevents the execution of malicious code.
  * **Live Updates**: Conversions are performed in real-time as the user types, using a simple `<KeyRelease>` event binding to trigger the calculation logic.

-----

## Simple Unit Converter (`Unit Converter.py`)

This application is the epitome of simplicity and efficiency. It is designed for users who need a quick, no-fuss tool for the most common unit conversions. Its lightweight nature and immediate responsiveness make it a highly practical utility.

The UI is clean and minimalist, presenting all necessary information in a single, compact window. It focuses on an intuitive user experience where the conversion happens instantly without requiring extra clicks or confirmations.

### Key Features 

  * **Minimalist Design**: A straightforward and uncluttered interface that is immediately understandable to any user.
  * **Core Conversion List**: It comes pre-loaded with a fixed set of ten essential conversions, including distance, mass, temperature, and area.
  * **Instantaneous Feedback**: The application calculates and displays the converted value as the user types. This is achieved using an `after()` method, which introduces a tiny 100ms delay to ensure a smooth user experience without overwhelming the system with constant updates on every single keystroke.
  * **Input Validation**: A `validatecommand` is registered with the input entry widget. This function ensures that only numbers (or a leading hyphen for negative temperatures) can be entered, preventing runtime errors from non-numeric input.
  * **Cross-Platform Window Sizing**: The application intelligently detects the user's operating system (Windows, macOS, or Linux) to set an appropriate default window size, ensuring a consistent look and feel across different platforms.
  * **Formatted Output**: All conversion results are neatly formatted to two decimal places, providing clean and readable output.

-----

### How to Run

To use these applications, ensure you have Python installed on your system.

1.  **Download** the `.py` file for the application you wish to run.

2.  **Navigate** to the file's directory in your terminal or command prompt.

3.  **Execute** the script using the following command:

    For the advanced converter:

    ```bash
    python "UC + User-Def Ftns WIP.py"
    ```

    For the simple converter:

    ```bash
    python "Unit Converter.py"
    ```

### Technologies Used

  * **Language**: Python 3
  * **GUI Library**: Tkinter (`tkinter` and `tkinter.ttk`)
