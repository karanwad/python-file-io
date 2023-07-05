import re, string 

def main():
    
    with open('origin.txt', 'r') as input_stream:
        line_count = 0

        for eachLine in input_stream:
            line_count += 1
            line = eachLine.strip()
            words = line.replace("--", " ").split()

            for eachWord in words:
                if re.search("inherit", eachWord, flags = re.IGNORECASE):
                    with open("origin_output.txt", "a") as output_stream:
                        output_stream.write(f"{line_count} {eachWord}\n")
       

if __name__=='__main__':
    main()
            


