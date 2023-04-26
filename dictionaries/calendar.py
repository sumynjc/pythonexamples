"""
Birthdays
According to the known list of all birthdays learn how to determine who has a birthday in a given month.

Input format.

The first line contains an integer N (1 ≤ N ≤ 1000) - the number of friends. The next N lines contain information about their birthdays. Each line consists of three parts separated by a space - name, day and month of his birth. The name is a string, the day is a number from 1 to 31, and the month is a string of the set "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sen", "Oct", "Nov", "Dec".

The names are different.

The next line contains an integer M (1 ≤ M ≤ 100) - the number of questions to answer. The next M lines contain the questions themselves. The question is the name of the month in the same format as they are given above.

Output format
For each question on a separate line, print the names of all friends who were born in the month specified. Arrange the names in lexicographical order.

If no one was born in the given month, print the message "No data".
"""
def read_lines(i):
    return [input() for _ in range(i)]

data = sorted(read_lines(int(input())))
months = read_lines(int(input()))
d = dict()

lines = [l.split() for l in data]
name, day, month = 0,1,2
for line in lines:
    key, val = line[month], line[name]
    d.setdefault(key, []).append(val)

[print(*d.get(m,['No data'])) for m in months]
