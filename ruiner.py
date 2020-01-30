import glob, os, re, random

def main():
    #this will look through the folder for everything (credit https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python)
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    for fil in glob.glob("*.py"):
        #only keeps files that end in .py and are not called "ruiner.py"
        if fil[-3:] == ".py" and fil != "ruiner.py":
            #each file is ruined
            ruin(fil)

def ruin(fil):
    #open the file
    open_file = open(fil, "r")
    lines = open_file.readlines()
    open_file.close()
    #for each line, 
    temp_lines = []
    for line in lines:
        #if the first non-tab, non-space character is a "#", the line is deleted
        if not_comment(line):
            temp_lines.append(line)
    
        #on the full text,
    full_text = ""
    for line in lines:
        full_text += line

    #get a list of all variables
    variables = get_variables(full_text)
    #make a table of the old variables to new, terrible variable names
    variable_dictionary = {X : X for X in variables}
    for key in variable_dictionary:
        variable_dictionary[key] = stupid_variable_name(key)
    #replaces all the instances of the old name with the new, terrible ones
    for key in variable_dictionary:
        full_text = re.sub(key, variable_dictionary[key], full_text)
    
    #get a list of all functions
    functions = get_functions(full_text)
    #make a table of the old variables to new, terrible variable names
    function_dictionary = {X : X for X in functions}
    for key in function_dictionary:
        function_dictionary[key] = stupid_function_name(key)
    #replaces all the instances of the old name with the new, terrible ones
    for key in function_dictionary:
        full_text = re.sub(key, function_dictionary[key], full_text)

    #take the full text and turn it back into lines
    final_lines = full_text.split("\n")
    final_lines = [X + "\n" for X in final_lines]

    #overwrite the previous file with the new lines
    write_file = open(fil, "w")
    write_file.writelines(final_lines)
    write_file.close()
    


#returns if a given line is not a comment
def not_comment(line):
    for char in line:
        if char != " " and char != "\t":
            if char == "#":
                return False
            else:
                return True
    return True

#takes in a string and returns a list of all the functions definined within the text of that string
def get_functions(full_text):
    #regex for custom functions used in the file
    function = r"def [A-Za-z][A-Za-z0-9_]*\("
    #this is all of the functions defined in the file
    functions_used = re.findall(function, full_text)
    functions_used = [string[4:-1] for string in functions_used] 
    return functions_used   


#takes in a function name an scrambles it to worthlessness
def stupid_function_name(name):
    letter_list = [char for char in name]
    #get rid of half the letters at random
    random.shuffle(letter_list)
    letter_list = letter_list[0:len(letter_list) // 2]
    #insert a number of underscores within the word (letters / 3 -> 0)
    num_underscores = random.randint(0, len(letter_list) // 3)
    underscores = []
    for i in range(0, num_underscores):
        underscores.append("_")
    letter_list = letter_list + underscores
    #move the letters around
    random.shuffle(letter_list)
    #if the list creates an invalid function name
    while(letter_list[0] == "_"):
        #remove the invalidity
        letter_list = letter_list[1:]
    #return it!
    output = ""
    return output.join(letter_list)

def get_variables(full_text):
    #regex for functions used in the file
    function = r"[A-Za-z][A-Za-z0-9]*\("
    #this is all of the functions defined in the file
    functions_used = re.findall(function, full_text)
    functions_used = [string[:-1] for string in functions_used]

    #all the python keywords
    key_words = ["False","class","finally","is","return","None","continue","for","lambda","try","True","def","from",
    "nonlocal","while","and","del","global","not","with","as","elif","if","or","yield","assert","else",
    "import","pass","break","except","in","raise"]

    #regex for variables
    variable = r"[A-Za-z][A-Za-z0-9]*"
    #this is all of the functions called, defined, AND the variables! oh no!
    variables = re.findall(variable, full_text)
    variables = [var for var in variables if var not in functions_used and var not in key_words]

    #cull multiples
    final_variables = []
    for variable in variables:
        if variable not in final_variables:
            final_variables.append(variable)
    return final_variables

#picks a random, meaningless name, based on name inputted.
def stupid_variable_name(old_name):
    #if it contains an "_"
    if "_" in old_name:
        #split the name by "_"
        name_parts = old_name.split("_")
        #shorten each part and add meaningless symbols
        name_parts = [meaning_less(shorten(X)) for X in name_parts]
        #reconnect them
        output = "_"
        return output.join(name_parts)
    #if it does not
    else:        
        #shorten and add meaningless symbols
        return meaning_less(shorten(old_name))



#shortens a string randomly, from the front and back
def shorten(string):
    center = len(string) // 2
    front = random.randint(0, center)
    back = - (random.randint(0, center) + 1)
    return string[front:back]

#adds random symbols to the front or end of a string
def meaning_less(string):
    bad_stuff = ["_","x","X"]
    mess_amount = random.randint(1,4)
    mess = ""
    for i in range(0, mess_amount):
        mess += random.choice(bad_stuff)
    options = ["front", "back"]
    front_or_back = random.choice(options)
    if front_or_back == "front":
        return mess + string
    else:
        return string + mess
        

main()
