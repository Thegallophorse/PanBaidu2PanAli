# https://github.com/foyoux/aligo

from aligo import Aligo

ali = Aligo()

def save_shared_file_to_netdisk(save_dir, share_id, share_pwd=''):
    info = ali.get_share_info(share_id)
    share_token = ali.get_share_token(share_id, share_pwd)
    share_file_list = ali.get_share_file_list(share_id, share_token.share_token)
    file_id_list =[i.name for i in ali.get_file_list(save_dir.file_id)]
    print(file_id_list)
    for i in share_file_list:
        print(i)
        if i.name not in file_id_list:
            save_file = ali.share_file_saveto_drive(share_id, file_id=i.file_id, share_token=share_token.share_token, to_parent_file_id=save_dir.file_id)

def batch_save_shared_file_to_netdisk(filename, netdiskpath):
    file = ali.get_file_by_path(f'{netdiskpath}')
    name = file.name
    print(name)
    print(file.file_id)
    with open(f"{filename}", 'r', encoding='utf-8') as f:
        url_list = f.readlines()

    for url in url_list:
        if url.find('/') != -1:
            print(url)
            share_id = url.split('/')[-1].strip()
            print(share_id)
            save_shared_file_to_netdisk(file, share_id)
            # time.sleep(10)

# def batch_upload_file_to_netdisk(filepath, netdiskpath):



info = ali.get_personal_info()
total_size = info.personal_space_info.total_size
used_size = info.personal_space_info.used_size
#隐藏福利
ali.rewards_space('今天要开心哦')
batch_save_shared_file_to_netdisk('file_list.txt', '/kindle专属/书库')