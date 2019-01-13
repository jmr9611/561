# string -> [string : set(string)]
# returns a mapping from service name to the set of addresses
# it contains
def parseDNSResponses(output):
    serviceNameToAllIPMap = {}

    for line in iter(output.splitlines()):
        if " addr " in line:
            data = line.split()

            serviceName = data[0]
            ip = data[6]

            if serviceName in serviceNameToAllIPMap:
                serviceNameToAllIPMap[serviceName].add(ip)
            else:
                serviceNameToAllIPMap[serviceName] = set([ip])

    return serviceNameToAllIPMap

# string -> double
# returns round trip time as a single number
def parseRTTOutput(output):
    totalRTT = 0.0
    totalPackets = 0

    rawLines = output.split()
    # filter out empty lines
    relevantVals = list(filter(lambda line: line is not None, rawLines))

    for val in relevantVals:
        totalRTT += float(val)
        totalPackets += 1

    return totalRTT / totalPackets

# string -> double
# returns the average bitrate as a single number, calculated from bits/duration
def parseBitrate(output):
    rawLines = output.split("\n")

    # 5 is the index that contains the packet information
    relevantLine = rawLines[5]

    pktInfo = relevantLine.split()

    totalBits = float(pktInfo[8]) / 8.0
    duration = float(pktInfo[10])

    if duration <= 0:
        return None

    return totalBits / duration

# string -> double
# returns the percent of packets dropped
def parsePacketLoss(output):
    totalPacketCount = 0.0
    lostPacketCount = 0.0
    for line in output:
        totalPacketCount += 1
        if line == "1":
            lostPacketCount += 1

    return lostPacketCount / totalPacketCount
