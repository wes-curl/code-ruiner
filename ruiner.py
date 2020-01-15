import glob, os

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
    
    #on each line,
    #regex for variables, adding them to a list of found variables
    
    #create a table, connecting each found variable to a new, terrible name
    
    #for each line, replace the old variables with terrible new ones

    #on each line,
    #regex for functions, adding them to a list of found functions
    
    #create a table, connecting each found function to a new, terrible name
    
    #for each line, replace the old function with terrible new ones

    #overwrite the previous file with the new lines
    open_file = open(file, "w")
    open_file.writelines(temp_lines)


#returns if a given line is not a comment
def not_comment(line):
    for char in line:
        if char != " " and char != "\t":
            if char == "#":
                return False
            else:
                return True
    return True

main()