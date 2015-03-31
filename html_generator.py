def generate_concept_HTML(title, content):
    text1 = '''
<div class="concept">
    <div class="concept_title">
        ''' + '<center><b>' + title + '</b></center>'
    text2 = '''
    </div>
    <div class="concept_content">
        <p>
            ''' + content
    text3 = '''
        </p>
    </div>
</div>'''
    entire_document = text1 + text2 + text3
    return entire_document

def generate_HTML(concept):
    title = concept[0]
    content = concept[1]
    return generate_concept_HTML(title, content)

def generate_HTML_multiple(concept_list):
    HTML = ""
    for concept in concept_list:
        concept_HTML = generate_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

def write_HTML_file(concept_list):
    title = '''
<!DOCTYPE html>
<center><h2>Introduction to Programming Nanodegree - Lesson 1 and 2</h2></center>
<center><h2>Notes by: Rebecca Frezza </h2></center><br>
            '''
    file.write(title)
    file.write(generate_HTML_multiple(concept_list))
    return 0

# main program
concept_list = [ ['Computers & Programming', 'A computer is a machine. Unlike other machines that have a specific purpose (like a toaster), computers have many abilities. Programming is the act of giving a computer precise directions so that it will perform what we need it to do. An advantage of programming a computer is the speed at which it can run computations. By writing programs, we can make the most of a computers ability.'],
                 ['Python', 'Python is a high level programming language. One of the advantages of a high level language is the relative ease of use. Python uses a program called an interpreter. The interpreter converts the code into a language that the computer can understand. The interpreter also allows for portability of code across multiple systems. '],
                 ['Grammars & Backus-Naur Form', 'The purpose of Backus-Naur Form is to describe a language simply and concisely. This is the example of an idea used in computer science. We can break down the langage into two primary types, Non-terminals (something that is not finished) and Terminals (something that is completed). Non-terminals can be paired with terminals or other non-terminals.  Non-terminal rules dictate which other non-terminals it can be "linked" with.'],
                 ['The Variable','Variables make our code easier to read and more expressive. A variable is the name for a location in a computers memory. Using a variable name such as "miles_per_hour" in place of the number "60" increases the readibility of your code. A variable can be given a value of many data types. In the example "miles_per_hour = 60"..."miles_per_hour" is the variable and "60" is the value. The assignment operator = gives the variable a value. Should not be confused with the equals sign in arithmetic.'],
                 ['Strings','A string is a sequence of characters. In Python, a string can be written between single or double quotes. One advantage of strings over numbers is the feature of indexing. Indexing allows us to use square brackets "[ ]" to select a character in a string. If there is a variable that contains the string "udacity" and your code includes the line "print udacity[3]" it will print the fourth character "c". You can also select a substring, which is a subsequence of characters within the string. This is done by placing a colon between two index positions, "udacity[0:4]". If the string "udacity" has the value 123456, the code would print "123." '],
                 ['The Method Find','The Find method allows us to locate substrings within a string.  To use Find, you provide the method two strings. It will return the first index of the "target string". If the string is not found, it returns -1. You can pass a number in the second parameter of Find, this causes Find to begin searching at that index.'],
                 ['The Function','A function is a set of instructions defined by the programmer and is an important part of a program. It allows for readability and reduces redundancy in your code. When defining a function, we list arguments that can be passed to the function. The arguments are like variables used only inside of the function. To use a function, you only need the name and the number and type of arguments you can safely pass.']]

file = open('generated.html','w')
write_HTML_file(concept_list)
file.close()
print('Program has finished. Please view the file "generated.html."')