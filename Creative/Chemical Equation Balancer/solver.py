"""
[
    [reactant a, reactant b..., porduct a, porduct b...],       element a
    [reactant a, reactant b..., porduct a, porduct b...],       element b
    [reactant a, reactant b..., porduct a, porduct b...],       ...
]
"""
import re
import sympy as sp

reactants = input("Reactants: ").replace(" ", "").split("+")
products = input("Product(s): ").replace(" ", "").split("+")

compounds = reactants + products

elements = []
elements_ct = []
is_reactant = ""
for compound in range(len(compounds)):
    if compound + len(products) == len(compounds):
        is_reactant = "-"

    sections = re.split("(\([A-Za-z0-9]*\)[0-9]*)", compounds[compound])
    section_splitted = []

    for section in sections:
        if section[:1] == "(":
            section = re.split("\)([0-9]*)", section)
            multi = section[1]
            section = section[0][1:]
        else:
            multi = 1
        if section:
            splitted = re.findall("[A-Z][a-z]*|[0-9]*", section)[:-1]

            temp = []
            for i in range(len(splitted)):
                temp.append(splitted[i])
                if (i == len(splitted) - 1 and splitted[i].isalpha()) or (
                    splitted[i].isalpha() and splitted[i + 1].isalpha()
                ):
                    temp.append("1")
            splitted = temp

            for i in range(len(splitted)):
                if splitted[i].isnumeric():
                    splitted[i] = is_reactant + str(int(splitted[i]) * int(multi))
            section_splitted += splitted

    for i in range(len(section_splitted)):
        if section_splitted[i].isalpha():
            if section_splitted[i] not in elements:
                elements.append(section_splitted[i])
                elements_ct.append(["0" for i in range(len(compounds))])

            element_loc = elements.index(section_splitted[i])
            elements_ct[element_loc][compound] = str(
                int(elements_ct[element_loc][compound]) + int(section_splitted[i + 1])
            )

elements_ct = sp.Matrix(elements_ct)
ans = list(elements_ct.nullspace()[0])
multiple = sp.lcm([i.q for i in ans])
solution = [num * multiple for num in ans]
factor = sp.gcd([i for i in solution])
solution = [num * multiple for num in ans]

display = " + ".join([str(solution[i]) + reactants[i] for i in range(len(reactants))])
display += " --> "
display += " + ".join(
    [str(solution[len(reactants) + i]) + products[i] for i in range(len(products))]
)
display = display.replace("1", "")

print("\nBalanced Equation:", display, "\n")


# O2 + C6H12O6 --> H2O + CO2
