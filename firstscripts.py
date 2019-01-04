# my first file

# returns all DNS query responses with "Answers" -- includes IP Addresses from DNS payload
tshark -nr netflix.pcapng -Y "dns" -V 