import socket, time

def connect_to_server(ip, port, retry = 10):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        print(e)
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(ip, port,retry)
    return s

def get_source(s, ip, page):
    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get += 'Host: '
    get += ip
    get += CRLF 
    get += CRLF
    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    return response

def get_request(list_links, response,visited_links=0):
    beg = 0
    while visited_links < 50:
        beg_str = response.find('href="', beg)   
        if beg_str == -1:
           return list_links
        end_str = response.find('"', beg_str + 6)      
        link = response[beg_str + 6:end_str]
        ip = 'www.optimazadar.hr'
        port = 80
        page = '/' + link
        print("\nNew Page: ", page, "\n")
        test_socket = connect_to_server(ip, port)
        test_response = get_source(test_socket, ip, '/' + link)
        print("\nTest Response: ", test_response)
        if link.find(".css")== -1 and link.find(".jpg")== -1  and "200 OK" in test_response:
            if link not in list_links:
                visited_links += 1
                print("\n\n\n ----------------NEW LINK----------------\n\n\n")
                list_links.append(link)
                get_request(list_links, test_response, visited_links)
        beg = end_str + 1

ip = 'www.optimazadar.hr'
port=80
page="/"
s = connect_to_server(ip,port)
print(s)
response = get_source(s, ip, page)
list_links=[]
print(get_request(list_links, response))