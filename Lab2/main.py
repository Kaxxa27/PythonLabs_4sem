import fileservice
import regexservice
import constants
#regex = r"[A-Z][^.!?]*((\.{3})|(\.)|(\!?\??\!?))"
regex = r"\S[^.?!]+[.!?]*"

MY_CONST = constants.CONSTANTS
# Для чтения и записи. Создаст новый файл для записи, если не найдет с указанным именем.
# file = open("text.txt", "r")
# with file as file:
#     content = file.read()
#     my_list = re.findall(regex, content)

my_list = regexservice.text_analysis(regex, fileservice.open_file("text.txt", "r"))

i = 0
new_list = []
while i < len(my_list):
    my_str = str(my_list[i])
    for const in MY_CONST:
        if my_str.__contains__(const):
            if i == (len(my_list) - 1):
                break
            my_str = my_str + my_list[i+1]
            i += 1

    new_list.append(my_str)
    i += 1

# for item in my_list:
#     print(item)
for item in new_list:
    print(item)
print(len(new_list))


#if __name__ == '__main__':
    #print(sent for sent in re.findall(regex, string))
