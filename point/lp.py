# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
# 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
# 'with', 'our', 'python', '3', 'overview', 'python')
# print("кол python", text_tuple.count('python') + text_tuple.count('Python'))        
            
def unique(word):
    word_dict = list(word)
    no_double = set(word)
    if len(word_dict) == len(no_double):
        return True
    else:
        return False
print(unique('здарово'))
print(unique('привет'))


