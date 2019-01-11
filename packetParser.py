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
# returns the average bitrate as a single number, calculated from bytes/duration
def parseBitrate(output):
    totalBitrate = 0.0
    totalPackets = 0

    rawLines = output.split("\n")

    # 5 is the index where packet information starts,
    # -2 is the index where it ends
    relevantLines = rawLines[5:-2]

    for line in relevantLines:
        pktInfo = line.split()

        totalBits = float(pktInfo[8]) / 8.0
        duration = float(pktInfo[10])

        if duration <= 0:
            continue
        else:
            totalBitrate += totalBits / duration
            totalPackets += 1

    return totalBitrate / totalPackets

# string -> int
# returns the number of dropped packets as a single number
def parsePacketLoss(output):
    totalPacketCount = 0 # in case this is necessary later
    lostPacketCount = 0
    for line in output:
        totalPacketCount += 1
        if line == "1":
            lostPacketCount += 1

    return lostPacketCount
