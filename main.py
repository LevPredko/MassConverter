import tkinter as tk

def convert_mass():
    mass = float(entry_mass.get())
    from_unit = combo_from.get()
    to_unit = combo_to.get()

    unit_to_kilograms = {
        "grams": 0.001,
        "kilograms": 1,
        "tons": 1000,
        "centners": 100,
        "carats": 0.0002,
        "micrograms": 0.000000001,
        "milligrams": 0.000001,
        "pounds": 0.45359237,
        "ounces": 0.0283495,
        "stones": 6.35029,
        "quarters": 12.7006,
        "slugs": 14.5939,
        "short tons": 907.185,
        "Stones": 6350.29,
        "Pounds": 453.59237,
        "Drahrns": 1.77184519905875,
        "Grains": 0.06479891148,
    }

    if from_unit != "kilograms":
        mass = mass * unit_to_kilograms[from_unit]

    result = mass / unit_to_kilograms[to_unit]
    result_var.set(f"{result:.3f} {to_unit}")


window = tk.Tk()
window.resizable(False, False)
window.title("Mass Converter")

label_mass = tk.Label(window, text="Enter Mass:")
label_mass.grid(row=0, column=0, padx=10, pady=10)

entry_mass = tk.Entry(window)
entry_mass.grid(row=0, column=1, padx=10, pady=10)

combo_from = tk.StringVar(window)
combo_from.set("grams")
dropdown_from = tk.OptionMenu(window, combo_from, "grams", "carats", "kilograms", "centners", "tons",
                             "micrograms", "milligrams", "pounds", "ounces", "stones", "quarters", "slugs", "short tons",
                             "Stones", "Pounds", "Drahrns", "Grains")
dropdown_from.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(window, text="Result:")
result_label.grid(row=1, column=0, padx=10, pady=10)

result_var = tk.StringVar(window)
result_var.set("")
result_entry = tk.Entry(window, textvariable=result_var, state="readonly")
result_entry.grid(row=1, column=1, padx=10, pady=10)

combo_to = tk.StringVar(window)
combo_to.set("grams")
dropdown_to = tk.OptionMenu(window, combo_to, "grams", "carats", "kilograms", "centners", "tons",
                           "micrograms", "milligrams", "pounds", "ounces", "stones", "quarters", "slugs", "short tons",
                           "Stones", "Pounds", "Drahrns", "Grains")
dropdown_to.grid(row=1, column=2, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=convert_mass)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
