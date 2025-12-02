class StringToBoolean:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": False,
                    "default": "yes"
                }),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "convert"
    CATEGORY = "utils"

    def convert(self, text):
        cleaned = text.strip().lower()
        result = cleaned == "yes"
        return (result,)
