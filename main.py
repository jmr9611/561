import packetScraper as scraper
import packetParser as parser

import sys

REQUIRED_ARGS = 2

def main():
    if len(sys.argv) != REQUIRED_ARGS:
        print("Wrong number of arguments -- script should take pcap file name as sole arg")
        return

    # 1: get a list of service names and map them to their ip addresses
    pcapFileName = sys.argv[1]
    serviceNameToIPMap = parser.parseDNSResponses(scraper.getResponses(pcapFileName))

    # 2: for every service, find the relevant ip addresses and aggregate the statistics
    # into a service name -> stats map

    # string -> [(double, double, double)]
    serviceNameToStatsMap = {}

    for serviceName, ipSet in serviceNameToIPMap:
        statsList = []
        for ip in ipSet:
            rtt = parser.parseRTTOutput(scraper.getRTT(pcapFileName, ip))
            bitrate = parser.parseBitrate(scraper.getBitrate(pcapFileName, ip))
            packetLossPct = parser.parsePacketLoss(scraper.getPacketLoss(pcapFileName, ip))

            statsTuple = (rtt, bitrate, packetLossPct)
            statsList.append(statsTuple)

        serviceNameToStatsMap.insert(serviceName, statsList)

    # 3: analyze the data
    # TODO: -- Fill this in
