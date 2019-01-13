import packetScraper as scraper
import packetParser as parser
import main

netflixPcapFileName = "netflix.pcapng"
testPcapFileName = "testpcap.pcapng"
testIP = "10.8.106.202"
testIP2 = "192.229.173.136"

def testScraper():
    #print(scraper.getResponses(netflixPcapFileName))
    #print(scraper.getRTT(testPcapFileName, testIP))
    #print(scraper.getBitrate(testPcapFileName, testIP2))
    #print(scraper.getPacketLoss(testPcapFileName, testIP))
    return

def testParsing():
    #print(parser.parseDNSResponses(scraper.getResponses(testPcapFileName)))
    #print(parser.parseBitrate(scraper.getBitrate(testPcapFileName, testIP2)))
    #print(parser.parseRTTOutput(scraper.getRTT(testPcapFileName, testIP)))
    print(parser.parsePacketLoss(scraper.getPacketLoss(testPcapFileName, testIP)))
    return

testScraper()
testParsing()
