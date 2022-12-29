# 1. Diet information
# 2. Some kind of quizzes to decide what diet is good for the user

# To-do list:
# 1. Read and write from txt files
# 2. Display menu

# Choose a diet for today
option_string =""" 
Types of meals:
                        Protein             Carb            Fat
Mixed Meal              30%                 40%             30%
Paleo Meal              40%                 20%             40%
Low-carb Meal           40%                 10%             50%
Ketogenic Meal          20%                 5%              75%
"""
print(option_string)

class diet:

    def __init__(self, diet_type):
        self.diet = diet_type
        self.history = ""
        self.definition = ""
        self.pros = ""
        self.cons = ""
        self.ex_breakfast = ""
        self.ex_lunch = ""
        self.ex_dinner = ""
        self.snack = ""

    def history(self):
        print("The history of {diet}".format(diet = self.diet))
        #Read from the diet txt file and fill in the information to self.field then display it

    def definition(self):
        print("The definition of {diet}".format(diet = self.diet))
        #Read from the diet txt file and fill in the information to self.field then display it
    
    def pros_and_cons(self):
        print("The pros and cons of {diet}".format(diet = self.diet))
        #Read from the diet txt file and fill in the information to self.field then display it
    
    def meals(self):
        print("Example breakfast of {diet}".format(diet = self.diet))
        #Read from the diet txt file and fill in the information to self.field then display it
        print("Example lunch of {diet}".format(diet = self.diet))
        #Read from the diet txt file and fill in the information to self.field then display it
        print("Example dinner of {diet}".format(diet = self.diet))
        #Read from the diet txt file and fill in the information to self.field then display it
        print("Example snack of {diet}".format(diet = self.diet))



