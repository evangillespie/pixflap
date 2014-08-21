
from PIL import Image
from .config import WIDTH, HEIGHT

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

		return img

	@classmethod
	def _resize_image(cls, img):
		"""
		resize an image object to the size defined in the config and return it.
		"""
		# TODO: make sure that the new width is never less than it should be (rounding error)
		old_w, old_h = img.size
		resize_ratio = float(WIDTH) / float(old_w)
		img = img.resize((int(old_w*resize_ratio), int(old_h*resize_ratio)), Image.ANTIALIAS)

		return img

	@classmethod
	def _crop_image(cls, img):
		"""
		crop an image to the ratio defined in the config and return it.
		Image is not resized here. Assume that the image is the right size(ish) already
		"""
		old_h, old_w = img.size
		new_h = HEIGHT
		new_w = WIDTH

