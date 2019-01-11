import packetScraper as scraper
import packetParser as parser

netflixPcapFileName = "netflix.pcapng"
testPcapFileName = "testpcap.pcapng"
testIP = "10.8.106.202"

def testScraper():
    print(scraper.getResponses(netflixPcapFileName))
    print(scraper.getRTT(testPcapFileName, testIP))
    print(scraper.getBitrate(testPcapFileName))
    print(scraper.getPacketLoss(testPcapFileName, testIP))

def testParsing():
    #print(parser.parseBitrate(scraper.getBitrate(testPcapFileName)))
    print(parser.parseRTTOutput(scraper.getRTT(testPcapFileName, testIP)))

#testScraper()
testParsing()
