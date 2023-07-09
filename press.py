from wand.image import Image
import os

# 输入和输出文件夹路径
input_folder = "img"
output_folder = "img2"

# 如果输出文件夹不存在，就创建一个
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有图片
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)

        file_size = os.stat(input_file).st_size
        rate=100
        if(file_size>1024000):
            rate = 100000 * 1024 / file_size
            rate = int(rate)

        # 读取JPEG文件
        with Image(filename=input_file) as image:
            # 压缩图像
            image.compression_quality = rate
            image.save(filename=output_file)

        # 获取压缩前后的文件大小
        input_size = os.path.getsize(input_file)
        output_size = os.path.getsize(output_file)

        # 计算压缩比
        compression_ratio = output_size / input_size

        # 输出压缩前后的文件大小和压缩比
        print(f"{filename}: 压缩前的文件大小: {input_size} bytes")
        print(f"{filename}: 压缩后的文件大小: {output_size} bytes")
        print(f"{filename}: 压缩比: {compression_ratio:.2f}")