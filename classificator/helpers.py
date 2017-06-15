import re

def tokenizer(text):
    result = text
    result = result.replace('.', ' . ')
    result = result.replace(' . . . ', ' ... ')
    result = result.replace(',', ' , ')
    result = result.replace(':', ' : ')
    result = result.replace(';', ' ; ')
    result = result.replace('!', ' ! ')
    result = result.replace('?', ' ? ')
    result = result.replace('\"', ' \" ')
    result = result.replace('\'', ' \' ')
    result = result.replace('(', ' ( ')
    result = result.replace(')', ' ) ') 
    result = result.replace('/', ' ')
    result = re.sub(r'\s+', ' ', result)
    result = result.replace('^', ' ^ ')
    result = result.strip()
    result = result.split(' ')
    return result