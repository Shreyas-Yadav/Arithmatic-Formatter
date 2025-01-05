import re


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    
    lists = generate_parts(problems)
    if isinstance(lists, str):
        return lists

    

    problems = format_problems(lists,show_answers)
    print(problems.rstrip())
    return problems.rstrip()
    

def generate_parts(problems):
    f_line = []
    s_line = []
    t_line = []
    l_line = []
    for problem in problems:
        if not re.search(r'[+-]',problem):
            return "Error: Operator must be '+' or '-'."
             
        parts = re.split(r"[+-]",problem)
        

        if not (parts[0].strip().isdigit() and parts[1].strip().isdigit()) :
            return "Error: Numbers must only contain digits."
       
        ans = ''
        operator = '-'
        if '+' in problem:
            operator = '+'
            ans = str(int(parts[0].strip()) + int(parts[1].strip()))
        elif '-' in problem:
            ans = str(int(parts[0].strip()) - int(parts[1].strip()))
       

        
        

        maxLen = max(len(parts[0]),len(parts[1]))+1
        
        if len(parts[0].strip()) > 4 or len(parts[1].strip()) > 4:
            return "Error: Numbers cannot be more than four digits."

            

        f_line.append(' '*(maxLen-len(parts[0].strip())) + parts[0].strip())
        s_line.append(operator+' '*(maxLen-1-len(parts[1].strip())) + parts[1].strip())
        t_line.append('-'*maxLen)
        l_line.append(' '*(maxLen-len(ans))+ans)
        
    return [f_line,s_line,t_line,l_line]

        
def format_problems(lists,show_answers=False):
    problems = []
    problems.append(display_list(lists[0]))
    problems.append(display_list(lists[1]))
    problems.append(display_list(lists[2]))
    if show_answers == True:
        problems.append(display_list(lists[3]))
     
    return ''.join(problems)    



def display_list(my_list):
    return '    '.join(my_list) + '\n'



problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arithmetic_arranger(problems,True)
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')