from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        i = 0
        for i in range(len(strs[0])):
            flag = -1
            temp = strs[0][0:i+1]
            for j in range(1,len(strs)):
                if temp == strs[j][0:i + 1]:
                    flag = 1
                else:
                    return temp[0:len(temp)-1]
            count = i

        if len(temp[0:count+1]) == 0:
            print("no result")
        else:
            return(temp[0:count+1])
#
# class Solution17:
#     def letterCombinations(self, digits: str) -> List[str]:
#         length = len(digits)
#         dic = {
#             '2': ['a', 'b', 'c'],
#             '3': ['d', 'e', 'f'],
#             '4': ['g', 'h', 'i'],
#             '5': ['j', 'k', 'l'],
#             '6': ['m', 'n', 'o'],
#             '7': ['p', 'q', 'r', 's'],
#             '8': ['t', 'u', 'v'],
#             '9': ['w', 'x', 'y', 'z']
#         }
#
#         def make_letter(idx: int, letter: str) -> None:
#             # base condition
#             if idx == len(digits):
#                 ans.append(letter)
#                 return
#             print(letter)
#
#             # dfs 깊이 별로(번호 2 -> 3) 가능한 모든 조합 호출
#             for i in dic[digits[idx]]:
#                 make_letter(idx + 1, letter + i)
#
#         ans = []
#         make_letter(0, "")
#         print(ans)
#
# def isValid(s):
#     stack = []
#     identifier_dict = {")": "(", "]": "[", "}": "{"}
#     print(identifier_dict)
#     for l in s:
#         if l in identifier_dict:
#
#             if stack and identifier_dict[l] == stack[-1]:
#                 stack.pop()
#
#             else:
#                 return False
#         else:
#             stack.append(l)
#
#     if not stack:
#         return True
#     else:
#         return False

# def generateParenthesis22(num):
#     s=[]
#
#     for i in range(num-1):
#
#         tem=""
#         tem= "("*(i+1)
#         tem0= tem+"()" * (num -i-1)
#         tem = tem+")" * (i + 1)
#         tem1 = tem + "("*(num-i-1)+")"*(num-i-1)
#         tem2= tem+"()" * (num -i-1)
#         tem3= tem0 +")" * (i + 1)
#         # print("#####")
#         s.append(tem1)
#         s.append(tem2)
#         s.append(tem3)
#
#     print(set(s))

def generateParenthesis_official(n):

    res = []
    def solve(close, free, temp):
        if close <= free and close <= n and free <= n:
            if close == n and free == n:
                print("the final temp is {}".format(res))
                res.append("".join(temp))
                return
            temp.append("(")
            solve(close, free+1,temp)
            print("free is {0} and temp is {1}".format(free,temp))
            print("the poped is {}".format(temp))
            temp.pop()
            temp.append(")")
            solve(close+1, free, temp)
            print("close is {0} and temp is {1}".format(close+1,temp))
            print("the poped is {}".format(temp))

            temp.pop()
    solve(0,0,[])

    return res

def test(a,b):
    loop1 = len(a) if len(a)>=len(b) else len(b)
    loop2 = len(b) if len(a) >= len(b) else len(a)
    # if len(a)>= len(b):
    #     loop1=len(a)
    #     loop2=len(b)
    # else:
    #     loop1 = len(b)
    #     loop2 = len(a)

    res=[]
    for i in range(loop1) :
        for j in range(loop2):
            if (int(a[i])+int(b[j]))==10 :
                temp=[a[i],b[j]]
                res.append(temp)
    return res

def count(par,*args):

    head = temp = par
    res = {}
    sp=args
    print(sp)
    for i in range(len(head)):
        if head[i] in res.keys():
            res[head[i]]+=1
        else:
            res[head[i]]=1
    return res

def recon(list,n):
    newList=[]
    if len(list)< n:
        return list
    else:
        for i in range(int(len(list)/n)):
            for j in range(n):

              newList.append(list[(i+1)*(n)-1-j])

        if int(len(list)/n)<len(list)/n:
            j=1
            point= len(list)-n*int(len(list)/n)

            while j<=point:

                newList.append(list[len(list)-j])
                j+=1

        return newList





if __name__ == '__main__':
    # s = Solution()
    # a = s.longestCommonPrefix(["fliow", "aflp", "fliat"])
    # print(count([1,4,5,6,4,3,6],6))
    print(recon([1,3,4,8,6,7,8,6,2,3,4,5,6],4))


    # s = Solution17()
    # s.letterCombinations("234")

    # dic = {"(": ")", "[": "]", "{": "}" }
    #
    # s= input("input key")
    #
    # if  s in dic:
    #     print(s)
    # else:
    #     print("not match")

    # s = "()[]{}"
    # print(isValid(s))


    # run_22= generateParenthesis22(3)
    # run_22=generateParenthesis_official(3)
    # print(run_22)