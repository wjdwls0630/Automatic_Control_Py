from math import pi, sqrt


T_3904 = [308, 11.5, 3.54, 4.38]
T_4401 = [212, 13.2, 2.79,	7.69]


def del_T (t_3904, t_4401):
    result = []
    for i in range(0, len(t_3904)):
        result.append(abs((t_3904[i]-t_4401[i])/t_3904[i])*100)

    return result


print(del_T(T_3904, T_4401))









