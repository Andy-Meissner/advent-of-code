signal = open('data.txt').read()

def find_first_distinct_substr_of_len(length: int):
    for i in range(0,len(signal)-length, 1):
        substr = signal[i:i+length]
        if len(set(substr)) == length:
            return(i + length)

print(find_first_distinct_substr_of_len(4))
print(find_first_distinct_substr_of_len(14))