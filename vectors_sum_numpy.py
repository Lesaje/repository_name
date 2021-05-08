import numpy as np

vectors_num = int(input("Enter number of vectors: "))
vectors_dim = int(input("Enter dimension of vectors: "))
vector_list = list()
for i in range (vectors_num):
    print("Enter your vector:")
    try:
        tmp = list(map(int, input().split()))
        if len(tmp) != vectors_dim:
            raise ValueError ("Vector dimension must be the same")
        vector_list.append(tmp)
    except ValueError as e:
        print(e)
print(list(map(lambda list: sum(list), np.array(vector_list).T)))
