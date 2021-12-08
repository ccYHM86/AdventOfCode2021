"""binary_diagnostic.py"""


def main():
    print("---------Binary Diagnostic----------")

    with open('../resources/binary_diagnostic_input.txt', 'r') as data:
        lines = data.readlines()

    most_common_bit_01 = 0
    most_common_bit_02 = 0
    most_common_bit_03 = 0
    most_common_bit_04 = 0
    most_common_bit_05 = 0
    most_common_bit_06 = 0
    most_common_bit_07 = 0
    most_common_bit_08 = 0
    most_common_bit_09 = 0
    most_common_bit_10 = 0
    most_common_bit_11 = 0
    most_common_bit_12 = 0

    for line in lines:
        temp = list(line)
        if int(temp[0]) == 1:
            most_common_bit_01 += 1
        else:
            most_common_bit_01 -= 1

        if int(temp[1]) == 1:
            most_common_bit_02 += 1
        else:
            most_common_bit_02 -= 1

        if int(temp[2]) == 1:
            most_common_bit_03 += 1
        else:
            most_common_bit_03 -= 1

        if int(temp[3]) == 1:
            most_common_bit_04 += 1
        else:
            most_common_bit_04 -= 1

        if int(temp[4]) == 1:
            most_common_bit_05 += 1
        else:
            most_common_bit_05 -= 1

        if int(temp[5]) == 1:
            most_common_bit_06 += 1
        else:
            most_common_bit_06 -= 1

        if int(temp[6]) == 1:
            most_common_bit_07 += 1
        else:
            most_common_bit_07 -= 1

        if int(temp[7]) == 1:
            most_common_bit_08 += 1
        else:
            most_common_bit_08 -= 1

        if int(temp[8]) == 1:
            most_common_bit_09 += 1
        else:
            most_common_bit_09 -= 1

        if int(temp[9]) == 1:
            most_common_bit_10 += 1
        else:
            most_common_bit_10 -= 1

        if int(temp[10]) == 1:
            most_common_bit_11 += 1
        else:
            most_common_bit_11 -= 1

        if int(temp[11]) == 1:
            most_common_bit_12 += 1
        else:
            most_common_bit_12 -= 1


    gamma_rate = ""
    epsilon_rate = ""

    if most_common_bit_01 > 0:
        gamma_rate = '1'
        epsilon_rate = '0'
    else:
        gamma_rate = '0'
        epsilon_rate = '1'

    if most_common_bit_02 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    if most_common_bit_03 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    if most_common_bit_04 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    if most_common_bit_05 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    if most_common_bit_06 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    if most_common_bit_07 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    if most_common_bit_08 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    if most_common_bit_09 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    if most_common_bit_10 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    if most_common_bit_11 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    if most_common_bit_12 > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

    print(int(gamma_rate, 2))
    print(int(epsilon_rate, 2))

    print("Solution is: {} * {} = {}".format(int(gamma_rate, 2), int(epsilon_rate, 2), (int(gamma_rate, 2) * int(epsilon_rate, 2))))

if __name__ == "__main__":
    main()
