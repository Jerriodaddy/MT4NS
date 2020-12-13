import nmap
import json
import masscan
import threading
import time

nm = nmap.PortScanner()
# nm.scan('47.240.84.0/24', ports='22,80,8080', arguments='--max-rate 1000')
# print("Nmap scan finish")

# class myThread (threading.Thread):
#     def __init__(self, threadID, threadName, address, ports, arguments):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.threadName = threadName
#         self.address = address
#         self.ports = ports
#         self.arguments = arguments
#
#     def run(self):
#         print ("Starting " + self.threadName)
#         nmap_scan(self.threadName, self.address, self.ports, self.arguments)
#         print ("Exiting " + self.threadName)
#
# def nmap_scan(threadName, address, ports, arguments):
#     nm = nmap.PortScanner()
#     nm.scan(address, ports=ports, arguments=arguments)
#     print("===================================")
#     print("Nmap:" + threadName + " scan finish")
#     print(nm.command_line())
#     print(nm.scaninfo())
#     print(nm.scanstats())
#
# # Create New Threads
# thread1 = myThread(1, "T1", '47.240.0.0/24', ports='22', arguments='--max-rate 1000')
# thread2 = myThread(2, "T2", '47.240.0.0/24', ports='22,80,8080', arguments='--max-rate 1000')
# thread3 = myThread(3, "T3", '47.240.1.0/24', ports='22,80,8080', arguments='--max-rate 1000')
# thread4 = myThread(4, "T4", '47.240.0.0/23', ports='22,80,8080', arguments='--max-rate 1000')
#
# # Start Threads
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# print("Scan Over - Exit main thread.")

nm.scan("127.0.0.1", arguments="-O")
if 'osclass' in nm['127.0.0.1']:
    for osclass in nm['127.0.0.1']['osclass']:
        print('OsClass.type : {0}'.format(osclass['type']))
        print('OsClass.vendor : {0}'.format(osclass['vendor']))
        print('OsClass.osfamily : {0}'.format(osclass['osfamily']))
        print('OsClass.osgen : {0}'.format(osclass['osgen']))
        print('OsClass.accuracy : {0}'.format(osclass['accuracy']))
        print('')

# mas = masscan.PortScanner()
# mas.scan('125.65.0.0/24', ports='22,80,8080', arguments='--max-rate 1000')
#
# mas.command_line
# print(mas.scan_result)
