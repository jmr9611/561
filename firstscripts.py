# my first file
import subprocess

# string -> string
# returns all DNS query responses with "Answers" -- includes IP Addresses from DNS payload
# tshark -nr $pcapFileName -Y "dns" -V
def getResponses(pcapFileName):
    return subprocess.check_output(
    "tshark -nr " + pcapFileName + " -Y \"dns\" -V",
    shell=True)

# string, string -> string
# returns initial RTT (delay between SYN and SYN-ACK)
# tshark -r $pcapFileName -Y 'ip.addr == $ipName' -T fields -e tcp.analysis.initial_rtt
def getRTT(pcapFileName, ipName):
    return subprocess.check_output(
    "tshark -r " + pcapFileName + " -Y \'ip.addr == " + ipName + "\' -T fields -e tcp.analysis.initial_rtt",
    shell=True)

def test():
    netflixPcapFileName = "netflix.pcapng"
    testPcapFileName = "testpcap.pcapng"
    testIP = "10.8.106.202"
    print(getResponses(netflixPcapFileName))
    print(getRTT(testPcapFileName, testIP))

test()
