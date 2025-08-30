# 🔢 Greater Value Function (*args)

A non-interactive script that showcases a Python function designed to find the largest number from a variable-length list of arguments. This is achieved using the `*args` syntax (`*numbers` in the code).

## Features

* **Variable Arguments (`*args`)**: The `greater()` function can accept any number of numerical arguments without being defined with a fixed number of parameters.
* **Input Analysis**: Before providing the result, the function first prints all the numbers it received and their total count.
* **Maximum Value Detection**: It uses the built-in `max()` function to efficiently find and display the largest number from the provided arguments.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `greater_value_function.py`).
3.  Run the script from your terminal:
    ```sh
    python greater_value_function.py
    ```
4.  The script will automatically run the function with a predefined set of numbers and display the analysis and the result. You can easily modify the script to call the `greater()` function with your own numbers.

### Script Output

```
------Greater Value Function------
Number informed: 1 
Number informed: 2 
Number informed: 9 
Number informed: 3 
Number informed: 10 
5 numbers were reported in total
The greater value informed was 10
```
