import glob, os, re

def main():
    #this will look through the folder for everything (credit https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python)
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    for file in glob.glob("*.py"):
        #only keeps files that end in .py and are not called "ruiner.py"
        if file[-3:] == ".py" and file != "ruiner.py":
            #each file is ruined
            ruin(file)

def ruin(file):
    #open the file
    open_file = open(file, "r")
    lines = open_file.readlines()
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
        variable_dictionary[key] = stupid_variable_name()

    #replaces all the instances of the old name with the new, terrible ones
    for key in variable_dictionary:
        full_text = re.sub(key, variable_dictionary[key], full_text)

    #overwrite the previous file with the new lines
    #open_file = open(file, "w")
    #open_file.writelines(temp_lines)


#returns if a given line is not a comment
def not_comment(line):
    for char in line:
        if char != " " and char != "\t":
            if char == "#":
                return False
            else:
                return True
    return True

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

#picks a random, meaningless name
def stupid_variable_name():
    return "TEST"
    

main()