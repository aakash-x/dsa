# Example Input: 
# 3 2 // Number of cols Number of rows
# A2 // A1 = 20
# 4 5 * // A2 = 4 * 5 = 20
# A1 // A2 = 20
# A1 B2 / 2 + // B1 = A1/B2 + 2 =  20/3 + 2 = 8.6667
# 3 // B2 = 3 
# 39 B1 B2 * / // B3 =  39 / ( B1 * B2 ) = 39/26 = 3/2 = 1.5


# 1
# 2
# 3
# A
# A2
# 4 5 *
# A1 = 20
# B
# A1 B2 / 2 + = 20 / 3 + 2 = 6.6 + 2 = 8.6
# 3
# 39 B1 B2 * / = 39 / (8.6 * 3) = 1.5





# Example Output: 
# 3 2
# 20.0
# 20.0
# 20.0
# 8.6667


mat = [[]]
def post_fix(expression):
    stack = list()
    res = 0
    for i in expression.split(" "):
        if i in ['+', '-', '/', '*']:
            if len(stack) >= 2:
                print(stack[-1]+i+stack[-2])
                res += eval(stack[-1]+i+stack[-2])
                stack.pop(-1)
                stack.pop(-1)
            if len(stack):
                res += eval(i+stack[-1])
                stack.pop(-1)
        elif ord(i[0]) in range(65, 92):
            row, col = convert(i)
            res_i = post_fix(mat[i])
            mat[row][col] = res_i
            stack.append(res_i)
            continue
        # elif typeeval(i) in int:
        #     res
        stack.append(i)
    return res

print(post_fix('5 20 - 1 *'))


for row in mat:
    for col in row:
        


class Demo:
    def add(a: int, b: int)-> int:
        return a+b
    
    def add()
    
class Child(Demo):
    def add(a: str, b: str) -> str:
        return f"StringConcated  {a+b}"
    

        
        
        
        