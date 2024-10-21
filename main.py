file_path = './books/frankenstein.txt'
print("--- Begin report of " + file_path + " ---")
try:
    with open(file_path, 'r') as file:
        file_content = file.read()
        #print({file_content})

        
        result = len(file_content.split())
        print("The number of words in the document is: " + str(result))

        result_2= file_content.lower()
        res_dict = {}
        for a in result_2:
            if(a in res_dict):
                res_dict[a] += 1
            else:
                res_dict[a] = 1
        
        for b in res_dict:
            print("The " + b + " character was found " + str(res_dict[b]) + " times")

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error has occured")
