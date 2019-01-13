# string -> [string : [string]]
# returns a mapping from service name to the set of addresses
# it contains
def parseDNSResponses(output):
    dnsEntryKeyword = "Domain Name System (response)"

    entries = output.split(dnsEntryKeyword)

    for entry in entries:
        print(parseDNSEntry(entry))

    ## TODO : use the parse entry helper method to map the service names to
    ## all its ips
    return {}

# string -> [string : string]
# returns a mapping from service name to ip address mapped in this entry
def parseDNSEntry(entry):
    for line in iter(entry.splitlines()):
        if " addr " in line:
            data = line.split()

            serviceName = data[0]
            ip = data[6]
            return { serviceName : ip }

    print("Failed to find a valid service name and ip mapping")
    return {}

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
