# 从任意长度的可迭代对象中分解元素
def avg(self):
    if len(self.sequence) < 1:
        return None
    else:
        return sum(self.sequence) / len(self.sequence)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)
