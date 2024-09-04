import requests
    
        
def decode_doc(url):
    response = requests.get(url).text
    
    begin = response.find('y-coordinate')
    response = response[begin:]
    begin = response.find('<td')
    response = response[begin+3:]
    end = response.find('/table')
    response = response[:end]
    
    #parse the text into a list of the contents of each cell in the table
    cell_list = response.split('<td')
    for i, cell in enumerate(cell_list):
        cell = cell.split('</span')[0]
        cell = cell.split('>')[-1]
        cell_list[i] = cell
    
    #create a dictionary with keys (x,y)-coordinates and values unicode characters
    char_dict = {}
    x_max = 0
    y_max = 0
    for row_num in range(int(len(cell_list) / 3)):
        x_val = int(cell_list[row_num*3])
        y_val = int(cell_list[row_num*3 + 2])
        char_val = cell_list[row_num*3 + 1]
        
        x_max = max(x_max, x_val)
        y_max = max(y_max,y_val)
        char_dict[(x_val,y_val)] = char_val
    
    #print the secret message
    for j in range(y_max+1):
        y_index = y_max - j
        row = ''
        for i in range(x_max+1):
            if (i,y_index) in char_dict.keys():
                row = row + char_dict[(i,y_index)]
            else:
                row = row + ' '
        print(row)
