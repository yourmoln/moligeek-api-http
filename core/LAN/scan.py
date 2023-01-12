import os
import threading

if os.name == "nt":
    def scan_device(ip):
        address = ip
        response = os.popen("ping -n 1 " + address).read()

        if "ttl" in response.lower():
            print(address, 'is up!')
else:
    def scan_device(ip):
        address = ip
        response = os.system("ping -c 1 " + address)
        
        if "ttl" in response.lower():
            print(address, 'is up!')
def scan(ip_range):
    # Create a list of threads
    threads = []
    # Scan
    for i in range(1, 255):
        ip = ip_range + "." + str(i)
        t = threading.Thread(target=scan_device, args=(ip,))
        threads.append(t)
        t.start()
    # Wait for all threads to complete
    for t in threads:
        t.join()
        