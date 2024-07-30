# Proce byte 33 or 37 (! or %)
def Byte_3337(data):
	# Read file
	# with open(file, "rb") as r:
	# 	data = bytearray(r.read())

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

	with open("DJI_FIX.h264", "ab") as w:
		w.write(data)
	# return data


# Proce byte 00 02 09 -> 00 01 09 & 00 02 09 + 2 byte -> 00 00 01
def Byte_010209(data_in):
	# Read file
	# with open(file, "rb") as r:
	# 	data = bytearray(r.read())
	data = bytearray(data_in)
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
			data[offset + 5:offset + 8] = bytes.fromhex('000001')
		count = offset + len(hex_str) + 50
	
	Byte_3337(data)

# Byte_010209("NAL")