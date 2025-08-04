'''
DEVELOPER: Safia U.
COLLABORATORS: ---
DATE: May 2025
'''
'''
=====================================================
*               Class: Family                   
=====================================================
attributes:
* + household_size : int >=1
* - household_monthly_income : float >= 0
* + location: str # one of 3 LOCATIONS
=====================================================
methods:
* + __init__(household_size: int, household_monthly_income: float, location: str)
* + set_household_threshold(): void
* + calc_household_threshold(): float 
* - annual_income() : float 
* + is_below_poverty_line(): bool 
* + poverty_level_percentage(): float 
* + income_level(): str void
* + __str__(): str                                       *
=====================================================
'''
##########################################
# IMPORTS:
#   <list modules needed for program and their purpose>
##########################################
#<replace this line with import statement(s)>


##########################################
# FUNCTIONS:
##########################################
#<replace this line with function definitions, each needs a description>

class Family():
    def __init__(self, household_size=1, household_monthly_income=0.1, location="location"):
        self.household_size = household_size
        self.household_monthly_income = household_monthly_income
        self.location = location

    @property
    def household_size(self):
        return self._household_size 

    @household_size.setter
    def household_size(self, household_size):
        if household_size >= 1:
            self._household_size = household_size
        else:
            raise ValueError('Household size must be superior or equal 1')

    @property
    def household_monthly_income(self):
        return self._household_monthly_income

    @household_monthly_income.setter
    def household_monthly_income(self, household_monthly_income):
        if household_monthly_income >= 0:
            self._household_monthly_income = household_monthly_income
        else:
            raise ValueError('Household monthly income must be positive')

    def set_household_threshold(self):
        if self.location == '48states+dc':
            self.thresholds = { 
                1: 15650, 2: 21150, 3: 26650, 4: 32150,
                5: 37650, 6: 43150, 7: 48650, 8: 54150
                }
            self.extra_amount = 5500


        elif self.location == 'alaska':
            self.thresholds = {
                1: 19550, 2: 26430, 3: 33310, 4: 40190,
                5: 47070, 6: 53950, 7: 60830, 8: 67710
                }
            self.extra_amount = 6880
        elif self.location == 'hawaii':
            self.thresholds = {
                1: 17990, 2: 24320, 3: 30650, 4: 36980,
                5: 43310, 6: 49640, 7: 55970, 8: 62300
                } 
            self.extra_amount = 6330
        else:
            raise ValueError("Invalid location")

    def calc_household_threshold(self):
        self.set_household_threshold()
        if self.household_size <=8:
            self.household_threshold =  self.thresholds[self.household_size]
            return self.household_threshold
        else:
            self.household_threshold = self.thresholds[8] + (self.extra_amount * (self.household_size - 8))
            return self.household_threshold

    def annual_income(self):
        return self.household_monthly_income*12

    def is_below_poverty_line(self):
        return self.annual_income() <= self.calc_household_threshold()

    def poverty_level_percentage(self):
        return (self.annual_income() / self.calc_household_threshold() )* 100


    def income_level(self):
        if self.poverty_level_percentage() <= 50:
            return f"Income level: Extreme poverty"
        elif 50 < self.poverty_level_percentage() <= 100:
            return f"Income level: Below the poverty line"
        elif 100 < self.poverty_level_percentage() <= 150:
            return f"Income level: Near Poverty (Vulnerable)"
        elif 150 < self.poverty_level_percentage() <= 200:
            return f"Income level: Low income but above poverty line"
        else:
            return f"Income level: Moderate to high income"
            
    def __str__(self):
        return (
            f"Your annual income is: {self.annual_income():,.0f}$\n"
            f"Your threshold is: {self.calc_household_threshold():,.0f}$\n"
            f"Below poverty line?:{self.is_below_poverty_line()}\n"
            f"Your poverty level percentage is: {self.poverty_level_percentage():,.2f}%\n"
            f"{self.income_level()}")




##########################################
# MAIN PROGRAM:
##########################################
#<replace this line with your main program>
def main():
    household_size = int(input('Enter household size: '))
    household_monthly_income = float(input("Enter household monthly income (in dollars): "))
    location = input("Enter location (48states+DC, Alaska, or Hawaii): ").strip().lower()
    result = Family(household_size, household_monthly_income, location)
    print(result)

#main()

### GUI:
import tkinter as tk 
from tkinter import messagebox 
from tkinter import ttk 

def on_submit():
    size = size_entry.get()
    monthly_income = monthly_income_entry.get()
    location = location_combobox.get().strip().lower()
    
    if not size or not monthly_income or not location:
        messagebox.showerror("Missing entry", "Please complete the information")
         
    try:
        size = int(size)
        monthly_income = float(monthly_income)
          
        result = Family(size, monthly_income, location)
        output_popup = str(result)

        output_field.config(state='normal')
        output_field.delete(1.0, tk.END)
        output_field.insert(tk.END, output_popup)
        output_field.config(state='disabled')
        
        messagebox.showinfo("Submission received", "Thanks! Your data was submitted successfully!")

    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

LOCATIONS = ["48states+dc", "alaska", "hawaii"]

root = tk.Tk()# main window
root.title("POVERTY LEVEL CALCULATOR")# set title

size_label = tk.Label(root, text="Household size")
size_label.grid(row=0, column=0)
size_entry = tk.Entry(root)
size_entry.grid(row=0, column=1)

monthly_income_label = tk.Label(root, text="Household Monthly Income($)")
monthly_income_label.grid(row=1, column=0)
monthly_income_entry = tk.Entry(root)
monthly_income_entry.grid(row=1, column=1)

location_label = tk.Label(root, text="Location")
location_label.grid(row=2, column=0)
location_combobox = ttk.Combobox(root, values=LOCATIONS)
location_combobox.grid(row=2, column=1)

#button

button= tk.Button(root, text= "Submit", command=on_submit)
button.grid(row=3, columnspan=2)

#text field
output_field = tk.Text(root, height=10, width=50, state='disabled') # 'disabled' makes it read-only no input
output_field.grid(row=4, columnspan=2)

root.mainloop()# main loop for app




  
