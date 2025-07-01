import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class DispenserApp:
    """
    A GUI application for an ingredient dispenser built with Tkinter.
    """

    def __init__(self, root):
        """
        Initialize the application's UI.
        """
        self.root = root
        self.root.title("Ingredient Dispenser")
        # Increased the height from 400 to 550 to fit all widgets
        self.root.geometry("450x550")
        self.root.resizable(False, False)  # Make window not resizable

        # Style configuration
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 11))
        style.configure("TRadiobutton", background="#f0f0f0", font=("Helvetica", 10))
        style.configure("TButton", font=("Helvetica", 12, "bold"), padding=10)
        style.configure(
            "Result.TLabel", font=("Helvetica", 12, "italic"), foreground="#333"
        )

        # --- Data ---
        self.ingredients = ["Salt", "Sugar", "Flour", "Baking Soda", "Cocoa Powder"]
        self.units = ["Gallon", "Quart", "Pint", "Cup"]

        # --- Tkinter Variables ---
        # These variables will hold the current state of the selections.
        self.ingredient_var = tk.StringVar(value=self.ingredients[0])
        self.unit_var = tk.StringVar(value=self.units[0])
        self.amount_var = tk.StringVar()

        # --- Main Frame ---
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Ingredient Selection ---
        ingredient_frame = ttk.LabelFrame(
            main_frame, text="1. Select Ingredient", padding="10 10 10 10"
        )
        ingredient_frame.pack(fill=tk.X, pady=5)

        for ingredient in self.ingredients:
            rb = ttk.Radiobutton(
                ingredient_frame,
                text=ingredient,
                variable=self.ingredient_var,
                value=ingredient,
            )
            rb.pack(anchor=tk.W, padx=5, pady=2)

        # --- Unit Selection ---
        unit_frame = ttk.LabelFrame(
            main_frame, text="2. Select Units", padding="10 10 10 10"
        )
        unit_frame.pack(fill=tk.X, pady=5)

        for unit in self.units:
            rb = ttk.Radiobutton(
                unit_frame, text=unit, variable=self.unit_var, value=unit
            )
            rb.pack(anchor=tk.W, padx=5, pady=2)

        # --- Quantity Input ---
        amount_frame = ttk.Frame(main_frame)
        amount_frame.pack(fill=tk.X, pady=10)

        amount_label = ttk.Label(amount_frame, text="3. Enter Amount:")
        amount_label.pack(side=tk.LEFT, padx=(0, 10))

        self.amount_entry = ttk.Entry(
            amount_frame, textvariable=self.amount_var, width=15, font=("Helvetica", 11)
        )
        self.amount_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # --- Action Button ---
        self.start_button = ttk.Button(
            main_frame, text="Dispense", command=self.dispense
        )
        self.start_button.pack(pady=20, fill=tk.X)

        # --- Result Display ---
        self.result_label = ttk.Label(
            main_frame,
            text="Ready to dispense...",
            style="Result.TLabel",
            wraplength=400,
        )
        self.result_label.pack(pady=(10, 0))

    def dispense(self):
        """
        This function is called when the 'Dispense' button is clicked.
        It retrieves the user's selections and displays the result.
        """
        # Get values from the Tkinter variables
        ingredient = self.ingredient_var.get()
        unit = self.unit_var.get()
        amount_str = self.amount_var.get().strip()

        # --- Input Validation ---
        if not amount_str:
            messagebox.showerror("Input Error", "Please enter an amount.")
            return

        try:
            # Ensure the amount is a positive number
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        except ValueError:
            messagebox.showerror(
                "Input Error", "Please enter a valid positive number for the amount."
            )
            self.amount_var.set("")  # Clear invalid input
            return

        # Format the amount to remove unnecessary decimals if it's a whole number
        if amount == int(amount):
            amount_display = int(amount)
        else:
            amount_display = amount

        # Construct the output message
        result_text = f"Dispensing {amount_display} {unit} of {ingredient}."

        # Update the result label to show the user what is happening
        self.result_label.config(text=result_text)
        print(result_text)  # Also print to console as in the original script


if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    # Instantiate and run the application
    app = DispenserApp(root)
    # Start the Tkinter event loop
    root.mainloop()
