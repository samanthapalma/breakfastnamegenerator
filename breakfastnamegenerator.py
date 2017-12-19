print ('Welcome to the Recipe Generator')
name = input("Please, Enter Your Name!")
print (name)

if len(name) == 0:
  print ("Oops, Try Again")
else:
  print (name)

def main():
  Recipe = [
    ("Baby Spinach Omlet Recipe"),
    ("No Cook Overnight Oatmeal Recipe"),
    ("Oven Scrambled Eggs Recipe"),
    ("Morning Muffin Recipe"),
    ("Baked French Toast Recipe")

  ]

def main():
  Ingredients = [
    ("Baby Spinah Omlet Ingredients"),
    ("No Cook Overnight Oatmeal Ingredients"),
    ("Oven Scrambled Eggs Ingredients"),
    ("Morning Muffin Ingredients"),
    ("Baked French Toast Ingredients")

  ]

def main():
  Directions = [
    ("Baby Spinach Omlet Directions"),
    ("No Cook Overnight Oatmeal Directions"),
    ("Oven Scrambled Eggs Directions"),
    ("Morning Muffin Directions"),
    ("Baked French Toast Directions")

  ]

  printHeader()
  selection = int(getUserSelection())
  if selection == 0:
    printBabySpinachOmletRecipe(Recipe)
  elif selection == 1:
    printNoCookOvernightOatmealRecipe(Recipe)
  elif selection == 2:
    printOvenScrambledEggsRecipe(Recipe)
  elif selection == 3:
    printMorningMuffinRecipe(Recipe)
  elif selection == 4:
    printBakedFrenchToastRecipe(Recipe)
  elif selection == 5:
    printBabySpinachOmletIngredients(Ingredients)
  elif selection == 6:
    printNoCookOvernightOatmealIngredients(Ingredients)
  elif selection == 7:
    printOvenScrambledEggsIngredients(Ingredients)
  elif selection == 8:
    printMorningMuffinIngredients(Ingredients)
  elif selection == 9:
    printBakedFrenchToastIngredients(Ingredients)
  elif selection == 10:
    printBabySpinachOmletDirections(Directions)
  elif selection == 11:
    printNoCookOvernightOatmealDirections(Directions)
  elif selection == 12:
    printOvenScrambledEggsDirections(Directions)
  elif selection == 13:
    printMorningMuffinDirections(Directions)
  elif selection == 14:
    printBakedFrenchToastDirections(Directions)


class Recipe:
  def __init__(self, name):
    self.name = name

class Ingredients:
  def __init__(self, name):
    self.name = name

class Directions:
  def __init__(self, name):
    self.name = name

inputQuestions = [
  "For Baby Spinach Omlet Recipe, type 0",
  "For No Cook Overnight Oatmeal Recipe, type 1",
  "For Oven Scrambled Eggs Recipe, type 2",
  "For Morning Muffin Recipe, type 3",
  "For Baked French Toast Recipe, type 4",
  "For Baby Spinach Omlet Ingredients, type 5",
  "For Baby Spinach Omlet Directions, type 6",
  "For No Cook Overnight Oatmeal Ingredients, type 7",
  "For No Cook Overnight Oatmeal Directions, type 8",
  "For Oven Scrambled Eggs Ingredients, type 9",
  "For Oven Scrambled Eggs Directions, type 10",
  "For Morning Muffin Ingredients, type 11",
  "For Morning Muffin Directions, type 12",
  "For Baked French Toast Ingredients, type 13",
  "For Baked French Toast Directions, type 14",

]

def getUserSelection():
    inputQuestions = ["inputQuestions[0]", "inputQuestions[1]", "inputQuestions[2]", "inputQuestions[3]", "inputQuestions[4]", "inputQuestions[5]",
    "inputQuestions[6]", "inputQuestions[7]", "inputQuestions[8]", "inputQuestions[9]", "inputQuestions[10]", "inputQuestions[11]", "inputQuestions[12]", "inputQuestions[13]",
    "inputQuestions[14]"]
    for Questions in inputQuestions:
        print (Questions)

        return input("Type the recipe, ingredient list and/or directions you would like to view, and  press enter:")

def printHeader():
    print("Select a [Recipe/Ingredient List/Directions] Below:                               "

    "Baby Spinach Omlet  [0, 5, 10],                                                 "
    "No Cook Overnight Oatmeal [1, 6, 11],                                           "
    "Oven Scrambled Eggs [2, 7, 12],                                                 "
    "Morning Muffins [3, 8, 13],                                                     "
    "Baked French Toast [4, 9, 14]")

def printBabySpinachOmletRecipe(Recipe):
  print ("---- Baby Spinach Omlet Recipe -----")
  print ("Ingredients: 2 Eggs + 1 cup of Torn Baby Spinach Leaves + 1 1/2 tbl. grated Parmesan Cheese +1/4 tsp. Onion Powder"
  "+ 1/8 tsp. Ground Nutmeg + Salt/Pepper to Taste."
  "Directions: In a bowl, beat the eggs, and stir in the baby spinach and Parmesan cheese. Season with onion powder,"
  "nutmeg, salt,and pepper.In a small skillet coated with cooking spray over medium heat, cook the egg mixture about"
  "3 minutes, until partially set. Flip with a spatula, and continue cooking 2 to 3 minutes. Reduce heat to low, and"
  "continue cooking 2 to 3 minutes, or to desired doneness.")

def printNoCookOvernightOatmealRecipe(Recipe):
  print ("---- No Cook Overnight Oatmeal Recipe -----")
  print ("Ingredients: 1/3 cup of Milk + 1/4 cup of Rolled Oats + 1/4 cup of Greek Yogurt + 2 tsp. Chia Seeds + 2"
  "tsp. Honey + 1 tsp. Ground Cinnamon + 1/4 cup of Fresh   Blueberries."
  "  Directions: Combine milk, oats, Greek yogurt, chia seeds, honey and  cinnamon in a 1/2 pint jar with a lid:"
  "cover and shake until combined.  Remove   lid and fold in blueberries.  Cover jar with a lid.  Refriderate "
  "oatmeal, 8 hours to overnight.")

def printOvenScrambledEggsRecipe(Recipe):
  print ("---- Oven Scrambled Eggs Recipe -----")
  print ("Ingredients: 1/2 cup of Butter or Margarine Melted + 24 Eggs + 2 1/4 tsp. of Salt + 2 1/2 cups of Milk."
  "Directions: Preheat the oven to 350 degrees F (175 degrees C).  Pour melted butter into a glass 9x13 in baking dish."
  "In a large bowl, whisk together eggs and salt until well blended.  Gradually whisk in milk.  Pour egg mixture into the baking dish."
  "Bake uncovered for 10 minutes, then stir, and bake an additional 10 to 15 minutes, or until eggs are set.  Serve immediately.")

def printMorningMuffinRecipe(Recipe):
  print ("---- Morning Muffin Recipe -----")
  print ("Ingredients: 2/3 cups of Raisins + 2 cups of King Arthur White Whole Wheat Flour + 1 cup plus 2 tbl. Light Brown Sugar"
  " + 2 tsp. Baking Soda + 1 tablespoon ground cinnamon + 1 tsp. Ground Ginger + 1/2 tsp. Salt + 2 cups of Grated Carrots + 1 Large "
  "Tart Apple Grated (w/o core) + 1/2 cup of Shredded Coconut (sweetened or unsweetened) + 2/3 cup of Chopped Walnuts + 1/3 cup of "
  "Wheat Germ + 3 Large Eggs + 2/3 cup of Vegetable Oil + 2 tsp. of Vanilla Extract + 1/4 cup of Orange Juice.  Directions: "
  "Preheat the oven to 375°F.  Lightly grease in a 12 cup muffin tin.  In a small bowl, cover the raisins with hot water.  Set them "
  "aside to soak while you assemble the rest of the recipe.  In a large bowl, whisk together the flour, brown sugar, baking soda, "
  "cinnamon, giner and salt.  Stir in the carrots, apple, coconut, walnuts and wheat germ.  In a seperate bowl, beat together the eggs, "
  "oil, vanilla, and orange juice.  Add to the flour mixture and stir until evenly moistened.  Drain the rasins, squeezing out any "
  "excess water with your hands, and stir them in.  Divide the batter among the wells of the prepared pan.  They will be very full.  "
  "Bake the muffins for 25 to 28 minutes, until they are nicely domed and a cake tester inserted into the center of one of the inner domes"
  "comes out clean.  Remove the muffins from the oven and let cool in the pan on a rack for about 5 minutes.  Turn the muffins out onto "
  "the rack to cool completely.  Cover and store at room temperature for several days, or freeze for longer storage.")

def printBakedFrenchToastRecipe(Recipe):
  print ("---- Baked French Toast Recipe -----")
  print ("Ingredients: 1/2 cup of Butter Melted + 3/4 cup of Brown Sugar + 1 tbl. Ground Cinnamon + 12 slices of Sandwich Bread + "
  "6 Eggs + 1/2 cup of Milk + 1 pinch of Salt.  Directions: Coat a 9x13-inch baking dish with melted butter.  Spread any remaining "
  "melted butter over bottom of dish.  Sprinkle brown sugar and cinnamon evenly over melted butter.  Arrange bread in two layers over "
  "brown sugar mixture.  Beat eggs, milk, and salt in a bowl; pour over bread.  Cover and refriderate overnight.  Preheat oven to "
  "350 degrees F (175 degrees C).  Bake in the preheated oven until golden brown, about 30 minutes.")

def printBabySpinachOmletIngredients(Ingredients):
  print ("---- Baby Spinach Omlet Ingredients -----")
  print ("Ingredients: 2 Eggs + 1 cup of Torn Baby Spinach Leaves + 1 1/2 tbl. grated Parmesan Cheese +1/4 tsp. Onion Powder"
  "+ 1/8 tsp. Ground Nutmeg + Salt/Pepper to Taste.")

def printNoCookOvernightOatmealIngredients(Ingredients):
  print ("---- No Cook Overnight Oatmeal Ingredients -----")
  print ("Ingredients: 1/3 cup of Milk + 1/4 cup of Rolled Oats + 1/4 cup of Greek Yogurt + 2 tsp. Chia Seeds + 2"
  "tsp. Honey + 1 tsp. Ground Cinnamon + 1/4 cup of Fresh   Blueberries.")

def printOvenScrambledEggsIngredients(Ingredients):
  print ("---- Oven Scrambled Eggs Ingredients -----")
  print ("Ingredients: 1/2 cup of Butter or Margarine Melted + 24 Eggs + 2 1/4 tsp. of Salt + 2 1/2 cups of Milk.")

def printMorningMuffinIngredients(Ingredients):
  print ("---- Morning Muffin Ingredients -----")
  print ("Ingredients: 2/3 cups of Raisins + 2 cups of King Arthur White Whole Wheat Flour + 1 cup plus 2 tbl. Light Brown Sugar"
  " + 2 tsp. Baking Soda + 1 tablespoon ground cinnamon + 1 tsp. Ground Ginger + 1/2 tsp. Salt + 2 cups of Grated Carrots + 1 Large "
  "Tart Apple Grated (w/o core) + 1/2 cup of Shredded Coconut (sweetened or unsweetened) + 2/3 cup of Chopped Walnuts + 1/3 cup of "
  "Wheat Germ + 3 Large Eggs + 2/3 cup of Vegetable Oil + 2 tsp. of Vanilla Extract + 1/4 cup of Orange Juice.")

def printBakedFrenchToastIngredients(Ingredients):
  print ("---- Baked French Toast Ingredients -----")
  print ("Ingredients: 1/2 cup of Butter Melted + 3/4 cup of Brown Sugar + 1 tbl. Ground Cinnamon + 12 slices of Sandwich Bread + "
  "6 Eggs + 1/2 cup of Milk + 1 pinch of Salt.")

def printBabySpinachOmletDirections(Directions):
  print ("---- Baby Spinach Omlet Directions -----")
  print ("Directions: In a bowl, beat the eggs, and stir in the baby spinach and Parmesan cheese. Season with onion powder,"
  "nutmeg, salt,and pepper.In a small skillet coated with cooking spray over medium heat, cook the egg mixture about"
  "3 minutes, until partially set. Flip with a spatula, and continue cooking 2 to 3 minutes. Reduce heat to low, and"
  "continue cooking 2 to 3 minutes, or to desired doneness.")

def printNoCookOvernightOatmealDirections(Directions):
  print ("---- No Cook Overnight Oatmeal Directions -----")
  print ("Directions: Combine milk, oats, Greek yogurt, chia seeds, honey and  cinnamon in a 1/2 pint jar with a lid:"
  "cover and shake until combined.  Remove   lid and fold in blueberries.  Cover jar with a lid.  Refriderate "
  "oatmeal, 8 hours to overnight.")

def printOvenScrambledEggsDirections(Directions):
  print ("---- Oven Scrambled Eggs Directions -----")
  print ("Directions: Preheat the oven to 350 degrees F (175 degrees C).  Pour melted butter into a glass 9x13 in baking dish."
  "In a large bowl, whisk together eggs and salt until well blended.  Gradually whisk in milk.  Pour egg mixture into the baking dish."
  "Bake uncovered for 10 minutes, then stir, and bake an additional 10 to 15 minutes, or until eggs are set.  Serve immediately.")

def printMorningMuffinDirections(Directions):
  print ("---- Morning Muffin Directions -----")
  print ("Directions:  Preheat the oven to 375°F.  Lightly grease in a 12 cup muffin tin.  In a small bowl, cover the raisins with hot water.  Set them "
  "aside to soak while you assemble the rest of the recipe.  In a large bowl, whisk together the flour, brown sugar, baking soda, "
  "cinnamon, giner and salt.  Stir in the carrots, apple, coconut, walnuts and wheat germ.  In a seperate bowl, beat together the eggs, "
  "oil, vanilla, and orange juice.  Add to the flour mixture and stir until evenly moistened.  Drain the rasins, squeezing out any "
  "excess water with your hands, and stir them in.  Divide the batter among the wells of the prepared pan.  They will be very full.  "
  "Bake the muffins for 25 to 28 minutes, until they are nicely domed and a cake tester inserted into the center of one of the inner domes"
  "comes out clean.  Remove the muffins from the oven and let cool in the pan on a rack for about 5 minutes.  Turn the muffins out onto "
  "the rack to cool completely.  Cover and store at room temperature for several days, or freeze for longer storage.")

def printBakedFrenchToastDirections(Directions):
  print ("---- Baked French Toast Directions -----")
  print ("Directions: Coat a 9x13-inch baking dish with melted butter.  Spread any remaining "
  "melted butter over bottom of dish.  Sprinkle brown sugar and cinnamon evenly over melted butter.  Arrange bread in two layers over "
  "brown sugar mixture.  Beat eggs, milk, and salt in a bowl; pour over bread.  Cover and refriderate overnight.  Preheat oven to "
  "350 degrees F (175 degrees C).  Bake in the preheated oven until golden brown, about 30 minutes.")

main()
