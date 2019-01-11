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

# string, string -> string
# returns lost segments for obtaining packet loss
# tshark -r $pcapFileName -Y 'ip.addr == $ipName' -T fields -e tcp.analysis.lost_segment
def getPacketLoss(pcapFileName, ipName):
    return subprocess.check_output(
    "tshark -r " + pcapFileName + " -Y \'ip.addr == " + ipName + "\' -T fields -e tcp.analysis.lost_segment",
    shell=True)
