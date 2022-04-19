# -*- coding: utf-8 -*-
'''
Created on 2022-04-19

@author: Enzo
'''
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true

提示：
    1 <= s.length <= 104
    s 仅由括号 '()[]{}' 组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# def isValid(s):
#     #长度为奇数时直接返回false
#     if len(s)%2 == 1:
#         return False
#     else:
#         #循环替换
#         while "()" in s or "[]" in s or "{}" in s:
#             s = s.replace("()","")
#             s = s.replace("[]","")
#             s = s.replace("{}","")
#         return s == ""

#栈的方式实现

def isValid(s):
    if len(s) == 0:
        return False
    #stack存放左括号
    stack = []
    #构建左右括号对应关系：key:左括号，value:右括号,加快查询
    pairs = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for i in s:
        if i in pairs:
        #i为右括号时
            if not stack or stack[-1] != pairs[i]:
            #stack为空，或者栈顶与i的括号不对应时直接返回False
                return False
            #出栈
            stack.pop()
        else:
        #i为左括号时，添加到stack里（入栈）
            stack.append(i)
    #最终stack为空时返回True，否则False
    return True if len(stack)==0 else False

if __name__ == '__main__':
    print(isValid("()[]{}"))
    print(isValid("([)]"))
    print(isValid("()[]{"))
