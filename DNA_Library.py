DNAtranscript = {"A": "U", "T": "A", "C": "G", "G": "C",
                 "a": "u", "t": "a", "c": "g", "g": "c"}
DNAcompl = {"A": "T", "T": "A", "C": "G", "G": "C",
            "a": "t", "t": "a", "c": "g", "g": "c"}
RNAcompl = {"A": "U", "U": "A", "C": "G", "G": "C",
            "a": "u", "u": "a", "c": "g", "g": "c"}

# appendable list of commands
commands_made = ["exit", "transcribe", "reverse",
                 "complement", "reverse complement"]


# clears flags
def cleanup():
    global rerun, isDNA, isRNA, output
    rerun, isDNA, isRNA, output = 0, 0, 0, ''


# looks for wrong nucleotides
def normalize(n):
    global isDNA, isRNA, rerun
    if n == "t" or n == "T":
        isDNA = 1
    elif n == "u" or n == "U":
        isRNA = 1
    elif n not in DNAtranscript:
        print("Organic chemists are never without work I see")
        rerun = 1


def transcribe(string):
    global isRNA, rerun, output
    for n in string:
        normalize(n)
        if rerun == 1:
            break
        if isRNA == 1:
            print("You can't transcribe RNA here! Please type something else")
            rerun = 1
            break
        output += DNAtranscript[n]
    return output


def reverse(string):
    global output
    output = string[::-1]
    return output


def complement(string):
    global isDNA, isRNA, rerun, output
    for n in string:
        normalize(n)
        if rerun == 1:
            break

    if rerun == 0:
        if isRNA == 0 and isDNA == 0:
            types = input("Please specify what your sequence is (DNA/RNA?):")
            if types == "RNA":
                isRNA = 1
            elif types == "DNA":
                isDNA = 1
            else:
                print("Where did you take it from?")
                rerun = 1

        if isRNA == 1:
            if isDNA == 1:
                print("Looks to be a hybrid sequence. Maybe try another one?")
                rerun = 1
            elif isDNA == 0:
                for n in string:
                    output += RNAcompl[n]
        elif isDNA == 1:
                for n in string:
                    output += DNAcompl[n]
    return output


while True:
    cleanup()
    check = input("""Enter your command here.
Available commands: transcribe, reverse, complement, reverse complement.
To escape, type exit:""")
    if check == "exit":
        print("Have a nice day!")
        break
    elif check in commands_made:
        while True:
            cleanup()
            string = input("Enter your sequence here")
            if check == "transcribe":
                transcribe(string)
            elif check == "reverse":
                reverse(string)
            elif check == "complement":
                complement(string)
            elif check == "reverse complement":
                c = complement(string)
                output = reverse(c)

            if rerun == 1:
                continue
            else:
                print(output)
                break
    else:
        print("try again!")
        continue
