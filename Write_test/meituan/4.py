string = 'abcabcabc'
k = 2
lenght = len(string)
result = 0
matrix = [[0 for col in range(lenght+1)]for row in range(lenght+1)]

for i in range(lenght):
    for j in range(i+1, lenght+1):

        temp_str = string[i:j]
        if len(temp_str)-2*k >= 1:
            if 
            if left == right:
                result += 1
                print(i, j)
print(result)
拆分
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
给定长度为n的串S，仅包含小写字母。定义



公式中，|A|代表字符串A的长度

也就是说如果子串是一个ABA型的字符串，且满足长度限制，则f(l,r)=1，否则等于0。（注意：形如“ababab”也可视为ABA型）



例如当n=2时，原式为f(1,1)+f(1,2)+f(2,2)。

输入
第一行一个字符串S

第二行一个数字k

输出
输出题目描述中式子的值


样例输入
abcabcabc
2
样例输出
8

提示
1<=n<=2000 , S[i]为小写字母

样例解释：
在这个字符串中，有f(1,5),f(1,8),f(1,9),f(2,6),f(2,9),f(3,7),f(4,8),f(5,9)的值为1，其他为0，故和为8。以f(1,5)为例，选择的子串是abcab，令A=“ab”，B=“c”,则|A|>=k且|B|>=1,因此f(1,5)等于1，以此类推。
规则
请尽量在全场考试结束10分钟前调试程序，否则由于密集排队提交，可能查询不到编译结果
点击“调试”亦可保存代码
编程题可以使用本地编译器，此页面不记录跳出次数


max xor min
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
 给你一个长度为n的序列a，请你求出对每一个1<=l<r<=n的区间中最大值和最小值的异或和的异或和。

例如序列为{1,3,5},不同的a(1,2)=1^3,a(1,3)=1^5,a(2,3)=(3^5),a(1,2)^a(1,3)^a(2,3)=0，所以最后的答案是0。

输入
输入第一行仅包含一个正整数n，表示序列的长度。(1<=n<=10^5)

接下来一行有n个正整数a_i，表示序列a。(1<=a_i<=10^9)

输出
输出仅包含一个整数表示所求的答案。


样例输入
3
1 3 5
样例输出
0

规则
请尽量在全场考试结束10分钟前调试程序，否则由于密集排队提交，可能查询不到编译结果
点击“调试”亦可保存代码
编程题可以使用本地编译器，此页面不记录跳出次数