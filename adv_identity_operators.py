#Task 1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submit_attend =[]

for x in attended:
    if "Alice" in x:
        submit_attend.append(x)
    elif "Bob" in x:
        submit_attend.append(x)
    elif "Charlie" in x:
        submit_attend.append(x)
    elif "David" in x:
        submit_attend.append(x)

print(submit_attend)



#Task 2
#check if the 2 lists are identical in terms of content, regardless of order

#set a place holder boolean that will determine if the lists are identical with content
identical_list = False
for x in attended:
    if "Alice" in x:
        identical_list = True
    elif "Bob" in x:
        identical_list = True
    elif "Charlie" in x:
        identical_list = True
    elif "David" in x:
        identical_list = True
    else:
        identical_list = False
        break

print(identical_list)


#Task 3
#using list methods, remove students from attended who did not submit


for x in attended:
    if "Alice" in x:
        pass
    elif "Bob" in x:
        pass
    elif "Charlie" in x:
        pass
    elif "David" in x:
        pass
    else:
        attended.remove(x)
print(attended)