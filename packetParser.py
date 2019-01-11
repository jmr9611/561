# string -> [string]
# returns list of ip addresses...?
def parseResponsesOutput(output):
    return

# string -> double
# returns round trip time as a single number
def parseRTTOutput(output):
    bitrate = output;
    return

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
