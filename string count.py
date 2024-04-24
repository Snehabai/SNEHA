def s(string):
    words = string.split()

    s_freq = {}

    for s in words:
        if s in s_freq:
            s_freq[s] +=1
        else:
            s_freq[s] =1 

    return s_freq

# Example usage:
string = '''mangos
city use
single qts
inside double qts'''
s_frequency = s(string)
print(s_frequency)