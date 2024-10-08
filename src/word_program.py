def check_count(line):
    words = line.split()
    cn = {}

    for i in words:
        if i in cn:
            cn[i] += 1
        else:
            cn[i] = 1

    sorted_cn = sorted(cn.items())
    return sorted_cn
