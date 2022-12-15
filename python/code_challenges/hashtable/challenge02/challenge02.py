# Write here the code challenge solution
def repeated(exaple ):
    content  = {}
    all_word = exaple.split()
    for i in all_word:
        if i not in content :
            content [i] = True
        else:
            return i
    
    return "No Repetition"
if __name__ == "__main__":
    ex1 =   'ASAC is a department at LTUC. ASAC teaches programming in LTUC'
    print(repeated(ex1))
    ex2 ="I am learning programming at ASAC"
    print(repeated(ex2))
