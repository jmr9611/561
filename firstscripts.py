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

 # string -> string
 # returns bytes and duration for obtaining bitrate
 # tshark -r $pcapFileName -q -z conv,tcp 
def getBitrate(pcapFileName):
    return subprocess.check_output(
    "tshark -r " + pcapFileName + " -q -z conv,tcp", shell=True)

# string -> [string]
# returns list of ip addresses...?
def parseResponsesOutput(output):
    return

# string -> double
# returns round trip time as a single number
def parseRTTOutput(output):
    return

def testShellCmds():
    netflixPcapFileName = "netflix.pcapng"
    testPcapFileName = "testpcap.pcapng"
    testIP = "10.8.106.202"
    print(getResponses(netflixPcapFileName))
    print(getRTT(testPcapFileName, testIP))
    print(getBitrate(testPcapFileName))

def testParsing():
    return

testShellCmds()
