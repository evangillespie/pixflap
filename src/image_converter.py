
from PIL import Image
from .config import WIDTH, HEIGHT
from .exceptions import ImageSizeError

__author__ = ('evan',)

class ImageConverter(object):
	"""
	class to convert images into a shape usable by the pix flap
	"""

	def __init__(self):
		pass

	@classmethod
	def convert_image(cls, img):
		"""
		open an image file and process it into the right shape

		:return Image: the PIL image object ready to compute
		"""
		img = cls._resize_image(img)
		img = cls._crop_image(img)
		cls._verify_final_dimensions(img)

		return img

	@classmethod
	def _resize_image(cls, img):
		"""
		resize an image object to the size defined in the config and return it.
		"""
		old_w, old_h = img.size
		resize_ratio = max([float(WIDTH)/float(old_w), float(HEIGHT)/float(old_h)])
		img = img.resize((int(old_w*resize_ratio), int(old_h*resize_ratio)), Image.ANTIALIAS)
		print img
		return img

	@classmethod
	def _crop_image(cls, img):
		"""
		crop an image to the ratio defined in the config and return it.
		Image is not resized here. Assume that the image is the right size(ish) already
		"""
		old_w, old_h = img.size
		new_h = HEIGHT
		new_w = WIDTH
		top = 0
		bottom = old_h
		left = 0
		right = old_w

		if old_h > new_h:
			diff = old_h-new_h
			top = diff/2
			bottom = old_h-diff/2
			if bottom-top > new_h:
				bottom -= bottom-top-new_h
		if old_w > new_w:
			diff = old_w-new_w
			left = diff/2
			right = old_w-diff/2
			if right-left > new_w:
				right -= right-left-new_w

		return img.crop((left, top, right, bottom))

	@classmethod
	def _verify_final_dimensions(cls, img):
		"""
		check that the final image is the correct size.
		raise an exception if it isnt
		"""
		w, h = img.size
		if w != WIDTH or h != HEIGHT:
			raise ImageSizeError("your image is the wrong size. It is: %s x %s and should be: %s x %s" % (w, h, WIDTH, HEIGHT))