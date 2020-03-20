Python practice for coursework.

Question 1 is to implement a function random_converter(x) that takes a variable x. It then returns the value of x that has been randomly converted into int, float, bool, string or complex. For instance, for x = 12 (an integer) random_converter(x) can return ’12’ (a string) or 12.0 (a float).
But the restrict is no use of advanced methods and functions like try/except. RE is allowed.

Question 2 contains three tasks.
First task is to implement a function report(), which takes as input the json file(nobelprizes.json) loaded as a Python dictionary. This function should return a Pandas DataFrame, where includes the years and categories in which a Nobel Prize was awarded and those in which it was not.

Second task is to implement a function get_laureates_and_motivation() which takes as input three arguments: the nobel prize dictionary (same as in the first task), year (a string) and category (a string). This function returns a Pandas DataFrame containing one row per laureate (i.e., a person who has won the Nobel prize).
Already set four self-test arguments: chemistry in 2010, medicine in 1967, literature in 1973, physics in 1937.

The lask task is to implement a function plot_freqs() which generates six plots, one for each category. The xaxis should contain the 1st, 10th, 20th, 30th, 40th and 50th most frequent word across the motivation sections for each category. The y-axis should refer to the frequency of each word in that category.
This function will only count the words provided in whitelist.txt.
