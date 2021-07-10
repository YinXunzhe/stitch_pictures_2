import os
from PIL import Image

#根据文件名的对应关系，将“灰色”文件夹和“蓝色”文件夹内
#不同色彩的对应图标拼接成一张图存放到“Elements“文件夹中

path1=os.path.abspath('.') #获取当前文件夹的绝对路径
path_grey = '\灰色'
path_blue = '\蓝色'
path_output = '\Elements'

def pinjie(key, images, path):
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

def main():
    #获取灰色图标文件夹中图片的文件路径和文件名
    for root, dirs, filenames in os.walk(path1+path_grey):
        for name in filenames:
            #排除文件名中包含括号的图片
            if '(' in name:
                pass
            else:
                # 根据图标名字name，拼合出完整的文件路径
                file_path = os.path.join(root, name)
                #因为灰色图标文件夹中图标的文件名有两种格式，因此图片的完整路径也有以下两种
                file0 = file_path
                file1 = os.path.join(root, f"{name.split('.')[0]} (1).png")

                #蓝色图标文件夹中同名的图标完整路径
                file2 = os.path.join(path1+path_blue, name)

                print('file0', file0)
                print('file1', file1)
                print('file2', file2)

                #如果存在file1，先去看file2是否存在，若存在就拼接file1、file2
                if os.path.exists(file1):
                    print('nice1')
                    if os.path.exists(file2):
                        print('nice2')
                        pinjie(name.split('.')[0], (file1, file1, file2),path1+path_output)
                #如果存在file2，就直接拼接file0、file2
                elif os.path.exists(file2):
                    pinjie(name.split('.')[0], (file0, file0, file2),path1+path_output)

if __name__ == '__main__':
    main()
