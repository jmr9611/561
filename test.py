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
    output = scraper.getBitrate(testPcapFileName)
    print(parser.parseBitrate(output))

testScraper()
testParsing()
