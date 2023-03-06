class PropertyROI:
   
    # __init__ Includes monthly income set to 0 and expenses dictionary with expense values set to 0
    def __init__(self):
        self.monthly_income = 0
        self.expenses = {
        'water':0,'HOA':0, 'lawn':0, 'vacancy':0, 'repairs':0, 'CapEx':0, 'property_management':0,'mortgage':0, 'misc_fees':0 } 
    
    # function to get all input *get_information*
    def get_information(self):
        self.monthly_income = float(input("Enter monthly income: "))
        # Foor loop to get all input *get_expenses*
        for expense in self.expenses:
            self.expenses[expense] = float(input(f"Enter {expense} expense: $"))
        # Expenses and total investment inputs and summations    
        self.expenses['taxes'] = float(input("Enter tax expense total: $"))
        self.expenses['insurance'] = float(input("Enter insurance expense total: $"))
        self.expenses['misc_fees'] = (float(input("Enter potential fees total: $")))
        self.total_investment = sum([
            float(input("Enter down payment: $")),
            float(input("Enter closing cost: $")),
            float(input("Enter rehab budget: $"))
        ])
    # calculation function
    def calculate_roi(self):
        annual_cash_flow = (self.monthly_income * 12) - sum(self.expenses.values()) * 12
        print(f"Monthly Income: {self.monthly_income}")

        print(f"Annual cash flow: {annual_cash_flow:.2f}")
        
        roi = annual_cash_flow / self.total_investment
        print(roi)
        return roi
        
    # "reciept" summation function
    def generate_receipt(self, roi):
        print("==== RENTAL PROPERTY RECEIPT ====")
        print("\n**********************************")
        print(f"     Monthly Income: ${self.monthly_income}")
        print("**********************************")
        print("\nExpenses:")
        for expense in self.expenses:
            print(f"{expense}: ${self.expenses[expense]}")
        print(f"\n   Total Investment: ${self.total_investment}")
        print("\n**********************************")
        print(f"    Return on Investment: {100*roi:.2f}%")
        print("**********************************")
        print("\n==== RENTAL PROPERTY RECEIPT ====")

# Make the calculator object from the PropertyROI class
calculator = PropertyROI()
# Call the get_information function
calculator.get_information()
# Make the roi calculation 
roi = calculator.calculate_roi()
# Call the generate_receipt function
calculator.generate_receipt(roi)


        

            
 
  

