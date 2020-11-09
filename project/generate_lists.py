"""
    Generate a list of benign and malignant samples
"""
import os

def main():
    malignos_40 = []
    malignos_100 = []
    malignos_200 = []
    malignos_400 = []

    benign_40 = []
    benign_100 = []
    benign_200 = []
    benign_400 = []

    for c in os.listdir('storage/BreaKHis_v1/histology_slides/breast/malignant/SOB'):
        for i in os.listdir(f'storage/BreaKHis_v1/histology_slides/breast/malignant/SOB/{c}'):
            for name in os.listdir(f'storage/BreaKHis_v1/histology_slides/breast/malignant/SOB/{c}/{i}/40X'):
                ext = name.split('.')[len(name.split('.')) - 1]
                if ext in ['png']:
                    malignos_40.append(f'storage/BreaKHis_v1/histology_slides/breast/malignant/SOB/{c}/{i}/40X/{name}')

            for name in os.listdir(f'storage/BreaKHis_v1/histology_slides/breast/malignant/SOB/{c}/{i}/100X'):
                ext = name.split('.')[len(name.split('.')) - 1]
                if ext in ['png']:
                    malignos_100.append(f'storage/BreaKHis_v1/histology_slides/breast/malignant/SOB/{c}/{i}/100X/{name}')

            for name in os.listdir(f'storage/BreaKHis_v1/histology_slides/breast/malignant/SOB/{c}/{i}/200X'):
                ext = name.split('.')[len(name.split('.')) - 1]
                if ext in ['png']:
                    malignos_200.append(f'storage/BreaKHis_v1/histology_slides/breast/malignant/SOB/{c}/{i}/200X/{name}')

            for name in os.listdir(f'storage/BreaKHis_v1/histology_slides/breast/malignant/SOB/{c}/{i}/400X'):
                ext = name.split('.')[len(name.split('.')) - 1]
                if ext in ['png']:
                    malignos_400.append(f'storage/BreaKHis_v1/histology_slides/breast/malignant/SOB/{c}/{i}/400X/{name}')


    for c in os.listdir('storage/BreaKHis_v1/histology_slides/breast/benign/SOB'):
        for i in os.listdir(f'storage/BreaKHis_v1/histology_slides/breast/benign/SOB/{c}'):
            for name in os.listdir(f'storage/BreaKHis_v1/histology_slides/breast/benign/SOB/{c}/{i}/40X'):
                ext = name.split('.')[len(name.split('.')) - 1]
                if ext in ['png']:
                    benign_40.append(f'storage/BreaKHis_v1/histology_slides/breast/benign/SOB/{c}/{i}/40X/{name}')

            for name in os.listdir(f'storage/BreaKHis_v1/histology_slides/breast/benign/SOB/{c}/{i}/100X'):
                ext = name.split('.')[len(name.split('.')) - 1]
                if ext in ['png']:
                    benign_100.append(f'storage/BreaKHis_v1/histology_slides/breast/benign/SOB/{c}/{i}/100X/{name}')

            for name in os.listdir(f'storage/BreaKHis_v1/histology_slides/breast/benign/SOB/{c}/{i}/200X'):
                ext = name.split('.')[len(name.split('.')) - 1]
                if ext in ['png']:
                    benign_200.append(f'storage/BreaKHis_v1/histology_slides/breast/benign/SOB/{c}/{i}/200X/{name}')

            for name in os.listdir(f'storage/BreaKHis_v1/histology_slides/breast/benign/SOB/{c}/{i}/400X'):
                ext = name.split('.')[len(name.split('.')) - 1]
                if ext in ['png']:
                    benign_400.append(f'storage/BreaKHis_v1/histology_slides/breast/benign/SOB/{c}/{i}/400X/{name}')

    benigns = [
        {
            'name': 'BENIGN_40PX.txt',
            'items': benign_40
        },
        {
            'name': 'BENIGN_100PX.txt',
            'items': benign_100
        },
        {
            'name': 'BENIGN_200PX.txt',
            'items': benign_200
        },
        {
            'name': 'BENIGN_400PX.txt',
            'items': benign_400
        }
    ]

    for i in benigns:    
        f = open(i['name'],'w')
        for item in i['items']:
            f.write(item+'\n')
        f.close()

    malignant = [
        {
            'name': 'MALIGNANT_40PX.txt',
            'items': malignos_40
        },
        {
            'name': 'MALIGNANT_100PX.txt',
            'items': malignos_100
        },
        {
            'name': 'MALIGNANT_200PX.txt',
            'items':malignos_200
        },
        {
            'name': 'MALIGNANT_400PX.txt',
            'items':malignos_400
        }
    ]


    for i in malignant:    
        f = open(i['name'],'w')
        for item in i['items']:
            f.write(item+'\n')
        f.close()

if __name__ == '__main__':
    main()