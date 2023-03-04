class PropertyROI:
    def __init__(self):
    
        self.monthly_income = 0
        self.expenses = {
        'water':0,'HOA':0, 'lawn':0, 'vacancy':0, 'repairs':0, 'CapEx':0, 'property_management':0,'mortgage':0, 'misc_fees':0 } 

    def get_information(self):
        self.monthly_income = float(input("Enter monthly income: "))
        for expense in self.expenses:
            self.expenses[expense] = float(input(f"Enter {expense} expense: $"))
        self.expenses['taxes'] = float(input("Enter tax expense total: $"))
        self.expenses['insurance'] = float(input("Enter insurance expense total: $"))
        self.expenses['misc_fees'] = (float(input("Enter potential fees total: $")))
        self.total_investment = sum([
            float(input("Enter down payment: ")),
            float(input("Enter closing cost: ")),
            float(input("Enter rehab budget: "))
        ])

    def calculate_roi(self):
        annual_cash_flow = (self.monthly_income * 12) - sum(self.expenses.values())* 12
        print(f"Monthly Income: {self.monthly_income}")

        print(f"Annual cash flow: {annual_cash_flow:.2f}")
        
        roi = annual_cash_flow / self.total_investment
        print(roi)
        return roi
        
        
    
    def generate_receipt(self, roi):
        print("==== RENTAL PROPERTY RECEIPT ====")
        print(f"Monthly Income: ${self.monthly_income}")
        print("\nExpenses:")
        for expense in self.expenses:
            print(f"{expense}: ${self.expenses[expense]}")
        print(f"Total Investment: ${self.total_investment}")
        print(f"\nReturn on Investment: {100*roi:.2f}%")
        print("==== RENTAL PROPERTY RECEIPT ====")
calculator = PropertyROI()
calculator.get_information()
roi = calculator.calculate_roi()
calculator.generate_receipt(roi)


        

            
 
  

