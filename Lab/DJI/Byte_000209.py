# Proce 00 02 09 + 2 byte -> 00 00 01
def Byte_000209(file):
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
		next50Byte = data[start:end]

		if hex_check in next50Byte:
			print(f"Found byte at offset {hex(offset)}")

			data[offset + 5:offset + 8] = bytes.fromhex('000001')
		count = offset + len(hex_str) + 50

	with open("NAL2", "wb") as w:
		w.write(data)

Byte_000209("NAL")