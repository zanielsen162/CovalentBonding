# Molecular Geometry Calculator

This program calculates the molecular geometry of a molecule based on the number of edge atoms, the central atom, and other factors. It uses a set of predefined elements and their charges, along with specific atomic arrangements.

## Prerequisites

Ensure you have Python installed on your system to run this program.

## Usage

1. Open the terminal or command prompt.
2. Run the program by executing the following command:

    ```bash
    python molecular_geometry_calculator.py
    ```

3. Follow the on-screen prompts to input the central atom and edge atom.

4. The program will then prompt you to select the amount of edge atoms. Choose from the available options based on the molecular geometry rules.

5. The program will output the molecular structure, including the atoms and bonds, as well as information about lone pairs and molecular geometry.

## Elements and Charges

The program uses a predefined set of elements with their corresponding charges (as well as the number of electrons needed for a complete shell):

```python
elemSym = ['H', 'B', 'C', 'N', 'O', 'F', 'Si', 'P', 'S', 'Cl', 'Se', 'Br', 'I']
elemCharge = [1, 3, 4, 5, 6, 7, 4, 5, 6, 7, 6, 7, 7]
elemNeeded = [2, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
```

## Important Notes

- The program ensures that the selected atoms are valid and prompts for a different selection if necessary.
- The molecular geometry is determined based on the number of edge atoms and lone pairs.

## Example

Here is an example of program output with user input:

```bash
['H', 'B', 'C', 'N', 'O', 'F', 'Si', 'P', 'S', 'Cl', 'Se', 'Br', 'I']
Center Atom: N
Edge Atom: H
Amount of Edge Options: [3]
Amount of Edge: 3


    H
    │
H ─ N ─ H


Edge Lone Pairs: [0, 0, 0]
Center Lone Pairs: 1
Molecular Geometry: Trigonal Pyramid
```

In this example, the molecular geometry is determined to be "Trigonal Pyramid" based on the input parameters.

Feel free to experiment with different inputs to explore various molecular geometries!
