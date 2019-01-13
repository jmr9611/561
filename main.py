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
            serviceNameToStatsMap[serviceName] = statsList

    return serviceNameToStatsMap

# Takes mapping from service names to their relevant statistics and
# ...?
## TODO: FILL THIS IN
def analyzeData(serviceNameToStatsMap):
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
