"""extract tile_size, width and height from a dzi xml document"""
# def parse_dzi_xml(dzi: xml.dom.minidom.Document):
#     image_el = dzi.firstChild
#     tile_size = int(image_el.getAttribute("TileSize"))
#     size_el = image_el.firstChild
#     width = int(size_el.getAttribute("Width"))
#     height = int(size_el.getAttribute("Height"))
#     return tile_size, width, height


"""Parse pyramid.dzi file given a pyramid.dzi file path"""
# dzi = xml.dom.minidom.parse(path)
# tile_size, width, height = parse_dzi_xml(dzi)


""" read an image from an S3 bucket"""
# import boto3
# import cv2
# s3_client = boto3.client('s3')
# response = s3_client.get_object(Bucket=bucket, Key=key)
# buf = response['Body'].read()
# image = np.asarray(bytearray(buf), dtype="uint8")
# image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
# return image


"""Parse pyramid.dzi file given a pyramid.dzi in s3"""
# s3_client = boto3.client('s3')
# response = s3_client.get_object(Bucket=bucket, Key=key)
# dzi_stream = response['Body'].read()
# dzi = xml.dom.minidom.parseString(dzi_stream)
# tile_size, width, height = parse_dzi_xml(dzi)


# pip install opencv-python numpy

# >>> import cv2
# >>> Import numpy as np
# 
# >>> image = cv2.imread('/path/to/image.jpg') # return None when failed and an ndarray when succeeded
# 
# >>> image.shape # shape of the image (height, width, 3 bgr colors)
# (100, 100, 3)
# 
# >>> cv2.imwrite('/path/to/output.jpg', image) # write the ndarray of image to the specified file
# 
# >>> image[y_start:y_end, x_start:x_end, :] = sub_image # embed sub_image into image. The axes start at the top left corner of the image
# 
# >>> cv2.resize(image, dsize=(50, 50)) # resize to height 50 and width 50
# 
# >>> np.full((256, 256, 3), 255, dtype='uint8') # blank white image of 256x256
#
# >>> np.hstack([im1, im2, ...]) # stack (concatenate) images horizontally
# >>> np.vstack([im1, im2, ...]) # stack (concatenate) images vertically
