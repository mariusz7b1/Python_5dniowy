# sposób tradycyjny
lst0 = []
for i in range(4):
    lst0.append(str(i))
print(lst0)

pass
# wyrazenie listowe
lst1 = [str(i) for i in range(4)]
print(lst1)


lst2 = [pow(ele, 3) for ele in range(11)]
lst3 = [ele**3 for ele in range(11)]
print(lst2)
print(lst3)
