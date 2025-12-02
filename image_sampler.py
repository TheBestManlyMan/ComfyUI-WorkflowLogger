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
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "sample_images"
    CATEGORY = "utils"

    def sample_images(self, images, count):
        batch_size = images.shape[0]

        if count >= batch_size:
            return (images,)

        step = batch_size // count
        indices = [i * step for i in range(count)]

        sampled = images[indices]

        return (sampled,)
