l = [19,2,31,45,1,11,121,27]

for i in range(1, len(l)):
        j = i-1
        nxt_element = l[i]

		
        while (l[j] > nxt_element) and (j >= 0):
            l[j+1] = l[j]
            j=j-1
        l[j+1] = nxt_element
print(l)

