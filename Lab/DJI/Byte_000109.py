# Proce byte 00 02 09 -> 00 01 09
def Byte_000109(file):
	# Read file
	with open(file, "rb") as r:
		data = bytearray(r.read())

	count = 0
	while True:
		# Find byte 00 02 09
		hex_str = bytes.fromhex('000209')
		hex_check = bytes.fromhex('0824680000030001')
		offset = data.find(hex_str, count)
		
		# Break if haven't
		if offset == -1:
			break

		#============main==============
		start = offset + len(hex_str)
		end = start + 50
		# Read 50 byte
		next50Bytes = data[start:end]

		if hex_check in next50Bytes:
			print(f"Found byte at offset {hex(offset)}")

			data[offset:offset + 3] = bytes.fromhex('000109')
		count = offset + len(hex_str) + 50
	
	with open("NAL2", "wb") as w:
		w.write(data)

Byte_000109("NAL")