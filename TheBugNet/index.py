from AI.detector import process_image, predict
from Proxy import Server, ForwarderServer
from time import sleep
from threading import Thread

loading_char = ['⠦', '⠖', '⠲', '⠴']
loading_message = ["Staging sniffer",
				   "Loading AI",
				   "Placing sniffer at core",
				   "Fetching nothing"]
proxy_forwarder_server = ForwarderServer('127.0.0.1', 2891, True, fwd_addr='127.0.0.1', fwd_port=2892)
proxy_server = Server('127.0.0.1', 2892, True)
print(
"""
TheBugNet
~~~~~~~~~~~~~~~~
"""
)
for i in range(100):
	print(f"[{loading_char[i % 4]}] " +
		   f"{loading_message[i // 25]}{'.' * (i % 4)}{' ' * 15}", end='\r')
	sleep(.025)

print()

forward_server_thread = Thread(target=proxy_forwarder_server.start, daemon=True)
forward_server_thread.start()

proxy_server.start()
