from object_analysis import MonoProcessor, ColorProcessor, add_hu_moments

class ImageFactory:
    @staticmethod
    def create_processor(img_path, type='mono'):
        if type == 'mono':
            return add_hu_moments(MonoProcessor)(img_path)
        elif type == 'color':
            return add_hu_moments(ColorProcessor)(img_path)
        else:
            raise ValueError("Unknown image type")
