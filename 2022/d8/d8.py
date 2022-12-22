lines = open("data.txt").readlines()

mat = [[int(c) for c in l.rstrip()] for l in lines]
res_mat = [[] for i in range(100)]
count = 0
s1 = len(mat)
s2 = len(mat[0])
for i in range(1, len(mat)-1):
    for j in range(1, len(mat[i])-1):
        cur = mat[i][j]
        col = [mat[x][j] for x in range(0, len(mat[i]))]
        max_l = max(mat[i][0:j])
        max_r = max(mat[i][j+1:])
        max_u = max(col[0:i])
        max_d = max(col[i+1:])

        if cur > max_l or \
            cur > max_r or \
            cur > max_u or \
            cur > max_d:
            count += 1
print(count + 2*s1 + 2*s2 -4)