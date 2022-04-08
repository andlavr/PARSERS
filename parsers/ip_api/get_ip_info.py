import time
import requests

if __name__ == "__main__":

    a = 135
    b = 25
    c = 12
    d = 25

    ip_start = 0
    ip_end = 256 ** 0
    start = time.time()

    for _ in range(256 ** 4):
        # ip_start += 1
        #
        # a = ip_start // (256 ** 3)
        # ost = ip_start % (256 ** 3)
        #
        # b = ost // (256 ** 2)
        # ost = ip_start % (256 ** 2)
        #
        # c = ost // 256
        # d = ip_start % 256

        if b == 255 and c == 255 and d == 255:
            print(time.time() - start)
            print(f"")
        time.sleep(0.7)
        response = requests.get(f"http://ip-api.com/json/{a}.{b}.{c}.{d}?fields=66846719")
        print(response)
        response = response.json()
        print(response)

    fin = time.time()
    print(fin - start)


# http://ip-api.com/json/85.26.25.65?fields=66846719
