# 1. Diet information
# 2. Some kind of quizzes to decide what diet is good for the user

# To-do list:
# 1. Read and write from txt files
# 2. Display menu

project_folder = "Project_03"
chosen_diet_str = ""

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

    def __init__(self, diet_type, info_string):
        self.diet = diet_type
        self.history = info_string[1]
        self.definition = info_string[2]
        self.pros = info_string[3]
        self.cons = info_string[4]
        self.ex_breakfast = info_string[5]
        self.ex_lunch = info_string[6]
        self.ex_dinner = info_string[7]
        self.snack = info_string[8]

    def write_history(self):
        print("The history of {diet}".format(diet = self.diet))
        print(self.history)

    def write_definition(self):
        print("The definition of {diet}".format(diet = self.diet))
        print(self.definition)
    
    def write_pros_and_cons(self):
        print("The pros and cons of {diet}".format(diet = self.diet))
        print(self.pros)
        print(self.cons)
    
    def write_meals(self):
        print("Example breakfast of {diet}".format(diet = self.diet))
        print(self.ex_breakfast)
        print("Example lunch of {diet}".format(diet = self.diet))
        print(self.ex_lunch)
        print("Example dinner of {diet}".format(diet = self.diet))
        print(self.ex_dinner)
        print("Example snack of {diet}".format(diet = self.diet))
        print(self.snack)


def get_diet_info(project_folder, diet_type):
    if diet_type == 1:
        path = project_folder + "\\Mixed_diet.txt"
        chosen_diet_str = "Mixed diet"
    elif diet_type == 2:
        path = project_folder + "\\Paleo_diet.txt" 
        chosen_diet_str = "Paleo diet"
    elif diet_type == 3:
        path = project_folder + "\\Low_carb_diet.txt"
        chosen_diet_str = "Low-carb diet"
    elif diet_type == 4:
        path = project_folder + "\\Ketogenic_diet.txt"
        chosen_diet_str = "Ketogenic diet"
    file = open(path, "r")
    info_string = ""
    for line in file:
        info_string += line
    file.close()
    return info_string, chosen_diet_str

def organize_diet_info(info_string):
    divide_string = info_string.split('~')
    return divide_string

diet_type = 4
info_str, chosen_diet_str = get_diet_info(project_folder, diet_type)
print(organize_diet_info(info_str))
print(chosen_diet_str)
chosen_diet = diet(chosen_diet_str, organize_diet_info(info_str))


print(chosen_diet.write_history())
print(chosen_diet.write_definition())
print(chosen_diet.write_pros_and_cons())
print(chosen_diet.write_meals())
