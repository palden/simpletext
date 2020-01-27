buffer_text = ""


def questionOrNot(_):
    qlist = ['How', 'When', 'Where', 'How', 'Why', 'Is', 'Are', 'Who', 'Should', 'Would', 'Can', 'Could', 'Can\'t']
    first_word = _.split()[0].capitalize()
    # Can use this instead that returns true or not  _.startswith('What', 'Why' ,'When')
    if first_word in qlist:
        return _.capitalize() + "? "
    else:
        return _.capitalize() + ". "


user_input = ""
while True:
    user_input = input('Enter a sentence: ')
    formatted = questionOrNot(user_input)
    if user_input == '\\end':
        break
    else:
        buffer_text += formatted
        continue


print(buffer_text)
