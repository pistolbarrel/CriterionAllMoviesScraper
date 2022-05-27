import os

from bs4 import BeautifulSoup



def main():
    with open("top.txt", encoding='utf-8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    # table = soup.find('tbody', attrs={'class': 'criterion-channel__tbody'})
    print("Souped it")
    table = soup.find('tbody', attrs={'class': 'criterion-channel__tbody'})
    print("found it")
    ret_str = ""
    if table:
        cnt = 0
        line_count = 1
        for string in table.stripped_strings:
            cnt += 1
            if string == ',':
                if cnt == 3:
                    ret_str += ','
                    cnt += 1
                    print(line_count)
                if cnt != 4:
                    ret_str += ','
                    print("problem " + str(cnt) + " " + str(line_count))
                    cnt = 4
                continue
            ret_str += string.replace(',','&CM^').strip() + ","
            if cnt > 4:
                ret_str = ret_str[:-1] + '\n'
                cnt = 0
                line_count += 1
                # if line_count % 100 == 0:
                    # print("Processed " + str(line_count))

    print(ret_str)
    # with open('helloworld.txt', 'w', encoding='ansi') as filehandle:
    #     filehandle.write(ret_str)
    a=10


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
