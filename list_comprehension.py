#list comprehensions

# Create a list of the input text
def new_input_text_list():
    input_text = open_input()
    new_list = []
    for item in input_text:
        text = item['Text']
        new_list.append(text)
    print(new_list)

def main():
    new_input_text_list()
    translate_loop()

def new_list_comprehension():
    input_text = open_input()
    list_comprehension = [item['Text'] for item in input_text]
    print(list_comprehension)

def main():
    new_input_text_list()
    translate_loop()
    new_list_comprehension()

