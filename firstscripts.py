# my first file

# returns all DNS query responses with "Answers" -- includes IP Addresses from DNS payload
tshark -nr netflix.pcapng -Y "dns" -V 

# returns initial RTT (delay between SYN and SYN-ACK)
tshark -r test1.pcap -Y 'ip.addr == 10.0.0.230' -T fields -e tcp.analysis.initial_rtt