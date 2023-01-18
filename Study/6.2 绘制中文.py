# 安装pillow
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = np.full((200, 200, 3), fill_value=255, dtype=np.uint8)
# 导入字体文件.
font_path = 'msyhbd.ttc'
font = ImageFont.truetype(font_path, 15)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((10, 150), '绘制中文', font=font, fill=(0, 255, 0, 0))
img = np.array(img_pil)

# 中文会显示问号
cv2.putText(img, '中文', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
