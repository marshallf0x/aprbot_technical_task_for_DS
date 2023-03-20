#Task 1.

#Use English SpaCy lib, find all tokens with only digits and all proper nouns 
#(PROPN, aka, personal nouns ) in the text, count it and output it right-aligned in the HTML.
#For example, for the text "we need 2 tickets to Dublin, and 1/2 a spoon of milk" 
#read from the stdin (use python myprogram.py < input.txt >output.html ) 
#the program should output that "2" was found twice (output "2"), "1" was found once (output "1"), 
#"Dublin" was found once (output "1").


import spacy 


model = spacy.load('en_core_web_sm')
model.tokenizer.infix_finditer = spacy.util.compile_infix_regex(model.Defaults.infixes + [r"/"]).finditer

tokens = model(input())

result_dict = dict()
get_rkeys = result_dict.keys

for token in tokens:
    if token.is_digit or token.pos_ == 'PROPN':
        if token.text in get_rkeys():
            result_dict[token.text] += 1
        else:
            result_dict[token.text] = 1
            
html_out = """
<html><body>\n
"""

for key in sorted(get_rkeys()):
    html_out += f"""<div>{key} : {result_dict[key]}</div>\n"""
    
html_out += """
</body></html>
"""

print(html_out)
