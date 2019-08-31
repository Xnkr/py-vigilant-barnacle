def main():
    infile_name = "cowfind.in"
    outfile_name = "cowfind.out"

    grass = ""
    with open(infile_name) as infile:
        grass = infile.readline()

    open_count = 0
    result = 0

    for i in range(len(grass)-1):
        if grass[i] is '(' and grass[i+1] is '(':
            open_count += 1
        elif grass[i] is ')' and grass[i+1] is ')':
            result += open_count


    with open(outfile_name, 'w') as outfile:
        outfile.write(str(result))

def attempt1():
    grass = ""
    result = 0
    for i in range(len(grass)-1):
        if grass[i] is '(' and grass[i+1] is '(':
            for j in range(i+2, len(grass)-1):
                if grass[j] is ')' and grass[j+1] is ')':
                    result += 1 
    

if __name__ == "__main__":
    main()