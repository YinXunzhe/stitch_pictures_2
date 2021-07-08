import os
from PIL import Image

#根据文件名的对应关系，将“灰色”文件夹和“蓝色”文件夹内
#不同色彩的对应图标拼接成一张图存放到“Elements“文件夹中

path1=os.path.abspath('.') #获取当前文件夹的绝对路径
path_grey = '\灰色'
path_blue = '\蓝色'
path_output = '\Elements'

def pinjie(key, images, path1):
    # 获取当前文件夹中所有JPG图像
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
    path = os.path.join(path1+path_output, f'{key}.jpg')
    result.save(path)

def main():
    for root, dirs, filenames in os.walk(path1+path_grey):
        for name in filenames:
            file_path = os.path.join(root, name)
            # print(file_path)
            if '(' in name:
                pass
            else:
                file0 = file_path
                file1 = os.path.join(root, f"{name.split('.')[0]} (1).png")
                file2 = os.path.join(path1+path_blue, name)
                print('file0', file0)
                print('file1', file1)
                print('file2', file2)
                if os.path.exists(file1):
                    print('nice1')
                    if os.path.exists(file2):
                        print('nice2')
                        pinjie(name.split('.')[0], (file1, file1, file2),path1)
                elif os.path.exists(file2):
                    pinjie(name.split('.')[0], (file0, file0, file2),path1)

if __name__ == '__main__':
    main()
