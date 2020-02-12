my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# indexes  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# list[start:end:step]

print(my_list[-1])
print(my_list[0:6])
print(my_list[:6])
print(my_list[1:-1])
print(my_list[5:])
does_it_mutate = my_list[:]
does_it_mutate.append(10)
another_test = my_list[:].append(11)
print(does_it_mutate)
print(my_list)
print(another_test) # None

print(my_list[2:-1:2])
print(my_list[6:2]) # -> empty since default step is 1
print(my_list[6:2:-1]) # -> goes in reverse

sample_url = 'https://google.com'

reversed_url = sample_url[::-1]
print(reversed_url)
top_level_domain = sample_url[-4:]
print(top_level_domain)
without_http = sample_url[8:]
print(without_http)
domain = sample_url[8:-4]
print(domain)

