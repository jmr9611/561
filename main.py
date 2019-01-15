import packetScraper as scraper
import packetParser as parser

import sys

REQUIRED_ARGS = 2

# Takes mapping from ip addresses to their service names and returns
# a mapping from service names to their relevant statistics
# [string : [string]] -> [string : [(double, double, double)]]
def nameIPMapToNameStatsMap(serviceNameToIPMap):
    pcapFileName = sys.argv[1]
    serviceNameToStatsMap = {}

    for serviceName, ipSet in serviceNameToIPMap.iteritems():
        statsList = []
        for ip in ipSet:
            rtt = parser.parseRTTOutput(scraper.getRTT(pcapFileName, ip))
            bitrate = parser.parseBitrate(scraper.getBitrate(pcapFileName, ip))
            packetLossPct = parser.parsePacketLoss(scraper.getPacketLoss(pcapFileName, ip))

            if rtt is not None and bitrate is not None and packetLossPct is not None:
                statsTuple = (rtt, bitrate, packetLossPct)
                statsList.append(statsTuple)

        if len(statsList) != 0:
            totalRTT = 0
            totalBitrate = 0
            totalPacketLoss = 0
            for st in statsList:
                totalRTT += st[0]
                totalBitrate += st[1]
                totalPacketLoss += st[2]
            avgSt = (totalRTT / len(statsList), totalBitrate / len(statsList), totalPacketLoss / len(statsList))
            serviceNameToStatsMap[serviceName] = avgSt

    return serviceNameToStatsMap

# Filters all non-video keys from the map
def filterNameToStatsMap(serviceNameToStatsMap):
    validKeys = ['nflx', 'youtube', 'netflix', 'hulu', 'youtbe']
    newDict = {}

    for key, val in serviceNameToStatsMap.iteritems():
        for validKey in validKeys:
            if validKey in key:
                newDict[key] = val
    return newDict

# Takes mapping from service names to their relevant statistics and analyzes it
def analyzeData(serviceNameToStatsMap):
    filteredMap = filterNameToStatsMap(serviceNameToStatsMap)

    for name, val in filteredMap.iteritems():
        rtt = val[0]
        bitrate = val[1]
        plp = val[2]
        qos = 0

        if rtt < .05:
            qos += 1
        if bitrate > 5000:
            qos += 2
        if plp < .02:
            qos += 2

        print('\n ' + name + 'RTT - ' + str(rtt) + ' Bitrate - ' + str(bitrate) + ' Packet Loss Pct. - ' + str(plp) + '\n')
        print('Overall QoS - ' + str(qos) + '\n')
    return

def main():
    if len(sys.argv) != REQUIRED_ARGS:
        print("Wrong number of arguments -- script should take pcap file name as sole arg")
        return

    # 1: get a list of service names and map them to their ip addresses
    pcapFileName = sys.argv[1]
    serviceNameToIPMap = parser.parseDNSResponses(scraper.getResponses(pcapFileName))

    # 2: for every service, find the relevant ip addresses and aggregate the statistics
    # into a service name -> stats map
    serviceNameToStatsMap = nameIPMapToNameStatsMap(serviceNameToIPMap)

    # 3: analyze the data
    analyzeData(serviceNameToStatsMap)

main()
