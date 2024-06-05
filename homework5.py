immutable_var=12, 'time', True
print(immutable_var)
#immutable_var[2]=False
#print(immutable_var)#невозможно изменинить, так как впринципе кортеж не изменяемый, не поддерживает обращения по элементам

mutable_list=[12, 'time', True]
mutable_list[2]=False
print(mutable_list)