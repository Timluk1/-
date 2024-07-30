'''Вам даны два файла third-task-A.txt и third-task-B.txt, содержащие не более 10 ** 4 целыx чисел, необходимо
определить максимальную длину возрастающей подпоследовательности в ответе укажите ее длину сначала для файла А, а затем
для файла B'''


def solv(file_path):
    ls = [int(i) for i in open(file_path)]
    n = len(ls)
    d = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if ls[j] < ls[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    return max(d)


print(solv("files/third-task-A.txt"), solv("files/third-task-B.txt"))
