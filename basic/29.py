color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

# Print out colors that are in one list and not the other

ans = [x for x in color_list_1 if x not in color_list_2]
print(ans)

ans = ans + [y for y in color_list_2 if y not in color_list_1]

print(ans)


