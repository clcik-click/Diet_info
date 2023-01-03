# Diet information

# To-do list:
# 1. Add information into txt files
# 2. Intergrate questions and modify answers
# 3.

project_folder = "Project_03"
chosen_diet_str = ""

# Choose a diet for today
diet_options_str =""" 
Types of meals:
                        Protein             Carb            Fat
Mixed Meal              30%                 40%             30%
Paleo Meal              40%                 20%             40%
Low-carb Meal           40%                 10%             50%
Ketogenic Meal          20%                 5%              75%
"""

diet_info_list ="""
1. History
2. Definition
3. Pros and cons
4. Meals
5. Go back
"""

print(diet_options_str)

def ask_questions():
    
    question_1 ="""
    Do you want to 
    1. lose weight quick"
    2. maintain weight
    3. gain weight
    """

    question_2 ="""
    Do you want to 
    1. feel good all year around"
    2. look good for a short amount of time
    """
    answer_1 = int(input(question_1))
    answer_2 = int(input(question_2))
    
    if question_1 == 1 and question_2 == 1:
        print("Scenario #1")
        pass
    elif question_1 == 2 and question_2 == 1:
        print("Scenario #2")
        pass
    elif question_1 == 3 and question_2 == 1:
        print("Scenario #3")
        pass
    elif question_1 == 1 and question_2 == 2:
        print("Scenario #4")
        pass
    elif question_1 == 2 and question_2 == 2:
        print("Scenario #5")
        pass
    elif question_1 == 3 and question_2 == 2:
        print("Scenario #6")
        pass


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
        print("Example breakfasts of {diet}".format(diet = self.diet))
        print(self.ex_breakfast)
        print("Example lunches of {diet}".format(diet = self.diet))
        print(self.ex_lunch)
        print("Example dinners of {diet}".format(diet = self.diet))
        print(self.ex_dinner)
        print("Example snacks of {diet}".format(diet = self.diet))
        print(self.snack)


def get_diet_info(project_folder, diet_type):
    path = ""
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

while True:
    # Asking for the diet
    diet_type = int(input("1 - Mixed diet,\n2 - Paleo diet,\n3 - Low carb diet,\n4 - Ketogenic diet .\n5- Exit\nEnter 1 or 2 or 3 or 4 to start explore: "))
    # Getting info from .txt file about the diet
    info_str, chosen_diet_str = get_diet_info(project_folder, diet_type)
    # Organize the diet info by creating a class
    chosen_diet = diet(chosen_diet_str, organize_diet_info(info_str))

    item_num = 0
    print("\n")
    print(chosen_diet_str + " in deep")
    while item_num < 5:
        print(diet_info_list)
        item_num = int(input("Enter a number: "))
        if item_num == 1:
            chosen_diet.write_history()
        elif item_num == 2:
            chosen_diet.write_definition()
        elif item_num == 3:
            chosen_diet.write_pros_and_cons()
        elif item_num == 4:
            chosen_diet.write_meals()
        elif item_num == 5:
            print("\n")
            break

    if not(diet_type >= 1 and diet_type <= 4):
        print("Exiting program")
        break 

print(chosen_diet.write_history())
print(chosen_diet.write_definition())
print(chosen_diet.write_pros_and_cons())
print(chosen_diet.write_meals())
