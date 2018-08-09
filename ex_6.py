default_order = "{},{} and {}".format('john','bill','sean')
print('\n---Default Order---')
print(default_order)


positional_order = "{1},{0} and{2}".format('john','bill','sean')
print('\n---positional Order---')
print(positional_order)

keyword_order = "{s} , {b} and {j}".format(j='john', b='Bill',s='sean')
print('\n---keyword Order---')
print(keyword_order)


