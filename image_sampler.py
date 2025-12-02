import torch


class ImageBatchSampler:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "count": ("INT", {
                    "default": 5,
                    "min": 1,
                    "max": 1000,
                    "step": 1
                }),
                "use_every_x": ("BOOLEAN", {
                    "default": False
                }),
                "every_x": ("INT", {
                    "default": 2,
                    "min": 1,
                    "max": 1000,
                    "step": 1
                }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "sample_images"
    CATEGORY = "utils"

    def sample_images(self, images, count, use_every_x, every_x):
        batch_size = images.shape[0]

        if use_every_x:
            indices = list(range(0, batch_size, every_x))
        else:
            if count >= batch_size:
                return (images,)
            step = batch_size // count
            indices = [i * step for i in range(count)]

        sampled = images[indices]

        return (sampled,)
