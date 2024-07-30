# Proce byte 33 or 37 (! or %)
def Byte_3337(file):
	# Read file
	with open(file, "rb") as r:
		data = bytearray(r.read())

	count = 0
	while True:
		# Find byte 08 24
		hex_str = bytes.fromhex('0824680000030001')
		offset = data.find(hex_str, count)

		# Break if haven't
		if offset == -1:
			break

		#============main==============
		start = offset + len(hex_str)
		end = start + 12
		# Read 12 byte
		next12Bytes = data[start:end]

		# Check if 33 or 37 (! or %)
		for index, byte in enumerate(next12Bytes):
			if byte == 0:
				print(f"Found byte {byte} at offset {hex(start + index)}")

				replace = start + index + 1
				if replace >= offset + len(hex_str):
					data[replace:replace + 3] = bytes.fromhex('000001')
				break

		count = offset + len(hex_str) + 12

	with open("NAL2", "wb") as w:
		w.write(data)


Byte_3337("NAL2")