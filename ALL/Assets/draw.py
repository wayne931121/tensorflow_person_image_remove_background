from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps
import numpy as np

def draw_bounding_box_on_image(image,
                               ymin,
                               xmin,
                               ymax,
                               xmax,
                               color = list(ImageColor.colormap.values())[0],
                               font = ImageFont.load_default(),
                               thickness=4,
                               display_str_list=()):
  """Adds a bounding box to an image."""
  image = Image.fromarray(np.uint8(image)).convert("RGB")
  draw = ImageDraw.Draw(image)
  im_width, im_height = image.size
  (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                ymin * im_height, ymax * im_height)
  draw.line([(left, top), (left, bottom), (right, bottom), (right, top),
             (left, top)],
            width=thickness,
            fill=color)

  # If the total height of the display strings added to the top of the bounding
  # box exceeds the top of the image, stack the strings below the bounding box
  # instead of above.
  display_str_heights = [font.getsize(ds)[1] for ds in display_str_list]
  # Each display_str has a top and bottom margin of 0.05x.
  total_display_str_height = (1 + 2 * 0.05) * sum(display_str_heights)

  if top > total_display_str_height:
    text_bottom = top
  else:
    text_bottom = top + total_display_str_height
  # Reverse list and print from bottom to top.
  for display_str in display_str_list[::-1]:
    text_width, text_height = font.getsize(display_str)
    margin = np.ceil(0.05 * text_height)
    draw.rectangle([(left, text_bottom - text_height - 2 * margin),
                    (left + text_width, text_bottom)],
                   fill=color)
    draw.text((left + margin, text_bottom - text_height - margin),
              display_str,
              fill="black",
              font=font)
    text_bottom -= text_height - 2 * margin
  return image  


def draw_boxes(
     image, 
     class_names, 
     boxes):
  ymin, xmin, ymax, xmax = tuple(boxes)
  colors = list(ImageColor.colormap.values())
  font_type = 'LiberationSansNarrow-Regular.ttf'
  font_size = 10
  #font = ImageFont.truetype(font_type,10 ,encoding='utf-8')
  font = ImageFont.load_default()
  display_str = (class_names)
  color = colors[hash(class_names) % len(colors)]
  image_pil = Image.fromarray(np.uint8(image)).convert("RGB")
  draw_bounding_box_on_image(
        image_pil,
        ymin,
        xmin,
        ymax,
        xmax,
        color,
        font,
        display_str_list=[display_str])
  ds( Image.fromarray(np.uint8( np.array(image_pil) )).convert("RGB") )
  #return image
  
def draw_boxes_s(
     image, 
     class_names, 
     boxes,
     scores,
     score_limit):
  now_image_np=np.zeros((image.shape))
  np.copyto(now_image_np , image)

  for i in range(0,len(boxes)):
    if(float(scores[i])>score_limit):
      box , score , class_name = boxes[i] , scores[i] , class_names[i]
      class_name=label_map[class_name]
      ymin, xmin, ymax, xmax = tuple(box)
      colors = list(ImageColor.colormap.values())
    
      font = ImageFont.load_default()
      display_str = (class_name+":"+str(score))
      color = colors[hash(class_name) % len(colors)]

      image_pil = Image.fromarray(np.uint8(now_image_np)).convert("RGB")

      draw_bounding_box_on_image(
            image_pil,
            ymin,
            xmin,
            ymax,
            xmax,
            color,
            font,
            display_str_list=[display_str])
    
      np.copyto(now_image_np, np.array(image_pil) )

  ds(Image.fromarray(np.uint8( np.array(now_image_np) )).convert("RGB") )  
  #return image  