import os
from PIL import Image

path_common=os.path.abspath('.') #获取当前文件夹的绝对路径
path_grey = '\灰色'
path_blue = '\蓝色'
#存放拼接后图像的文件夹
path_output = '\拼图'


def main():
    """
    根据文件名的对应关系，将“灰色”文件夹和“蓝色”文件夹内不同色彩的图标image1和imgae2
    拼接成以(image1,image1,image2)方式排布的图标，最后创建并存放到“拼图“文件夹中
    """
    #检查输出路径是否存在，若不存在则创建
    if not os.path.exists(path_common+path_output):
        os.makedirs(path_common+path_output)

    #获取灰色图标文件夹中图片的文件路径和文件名
    for root, dirs, filenames in os.walk(path_common+path_grey):
        for name in filenames:
            # 根据图标名字name，拼合出灰色图标的完整的文件路径
            file_grey = os.path.join(root, name)

            #由于个别灰色图标的文件名不规范，需进行规范化
            name=name.split('.')[0].strip(' (1)')+'.png'

            #蓝色图标文件夹中对应的图标完整路径
            file_blue = os.path.join(path_common+path_blue, name)

            if os.path.exists(file_blue):
                stitch_pictures(name, (file_grey, file_grey, file_blue), path_common + path_output)
            else:
                print(f"{file_blue} doesn't exist!\n")

def stitch_pictures(key, images, path):
    """ 拼接图像
        key-文件名
        images-要拼接的图像序列
        path-拼接后的图像保存路径
    """
    # 获取当前文件夹中所有图像
    im_list = [Image.open(fn) for fn in images]
    # 把图片存入ims列表中
    ims = []
    for i in im_list:
        ims.append(i)
    # 单幅图像尺寸
    width, height = ims[0].size
    # 创建符合拼接后尺寸的空白图片
    result = Image.new('RGB', (width * len(ims), height))
    # 拼接图片
    for i, im in enumerate(ims):
        result.paste(im, box=(i * width, 0))
    # 保存图片
    path = os.path.join(path, f'{key}.jpg')
    result.save(path)

    print(f'{key}.jpg saved!')

if __name__ == '__main__':
    main()
