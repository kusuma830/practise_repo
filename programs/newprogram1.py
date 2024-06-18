def add_wording(word):
    if len(word) > 2:
        if word[-3:] == "ing":
            word += "ly"
        else:
            word += "ing"
        return word
    else:
        return word


output = add_wording("amazing")
print(output)
