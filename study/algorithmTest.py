# 二分法查找
def binarySearch(attr, vaule):
    start = 0
    end = len(attr)
    while start <= end:
        middle = int((start + end) / 2)
        guessValue = attr[middle]
        if guessValue == vaule:
            return middle
        elif guessValue > vaule:
            end = middle
        else:
            start = middle
    return None


# 选择排序
def selectSort(attr):
    newArray = []
    for i in range(len(attr)):
        smallIndex = selectSmall(attr)
        newArray.append(attr.pop(smallIndex))
    return newArray


def selectSmall(attr):
    small = attr[0]
    smallIndex = 0
    for i in range(1, len(attr)):
        if attr[i] < small:
            small = attr[i]
            smallIndex = i
    return smallIndex


# 第二种选择排序
def selectSort2(attr):
    for i in range(len(attr)):
        selectSmall2(i, attr)


def selectSmall2(start, attr):
    small = attr[start]
    smallIndex = start
    for i in range(start + 1, len(attr)):
        if attr[i] < small:
            small = attr[i]
            smallIndex = i
    attr[smallIndex] = attr[start]
    attr[start] = small


# 使用递归求数组的和
def recursionSum(attr):
    if len(attr) < 2:
        return attr[0]
    else:
        return attr[0] + recursionSum(attr[1:])


# 快速排序
def fastSort(attr):
    if len(attr) < 2:
        return attr
    else:
        mi = attr[0]
        left = [i for i in attr[1:] if i <= mi]
        right = [i for i in attr[1:] if i > mi]
        return fastSort(left) + [mi] + fastSort(right)


if __name__ == '__main__':
    # attr = (1, 3, 6, 9, 12, 18, 19, 20, 34, 39, 40, 41, 41, 55, 56, 60, 61, 62, 63, 64, 65, 70)
    attr = [11, 30, 16, 29, 2, 13, 19, 24, 314, 39, 80, 101, 41, 55, 56, 60, 61, 62, 673, 14, 6, 7]
    # selectSort(attr)

    print(fastSort(attr))
