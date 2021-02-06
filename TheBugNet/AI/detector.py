from PIL import Image

# YCbCr Reference:
# http://www.naun.org/multimedia/NAUN/computers/20-462.pdf

def process_image(image_path):
	image = Image.open(image_path)

	if image.mode != 'YCbCr':
		image = image.convert('YCbCr')
	return image

def predict(image, threshold=0.2):
	ycbcr_data = image.getdata()
	width, height = image.size
	skin_pixel_count = 0

	for i, data in enumerate(ycbcr_data):
		y, cb, cr = data
		if 80 <= cb <= 127 and 130 <= cr <= 168:
			skin_pixel_count += 1

	if skin_pixel_count > threshold * width * height:
		return True
	else:
		return False

if __name__ == '__main__':
	import sys, os
	argv = sys.argv[1:]

	if argv[0]:
		if os.path.isfile(argv[0]):
			processed_image = process_image(argv[0])
			print(predict(processed_image))
		elif os.path.isdir(argv[0]):
			from glob import glob
			for file_path in glob(argv[0] + '*'):
				processed_image = process_image(file_path)
				predicted = predict(processed_image)
				if not predicted:
					print(f"{file_path}: {predicted}")
