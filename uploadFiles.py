import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_files(self,file_from,file_to):
            dbx=dropbox.Dropbox(self.access_token)

            f=open(file_from,'rb')
            dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BGWD413qvpqTou4FSy5EYcoYzzka1_BGnLfFYoATIv5wRZqS6WqLlXDB0Gagzob-YdDOgKQNRhW12FxybomNfdiua24aPzv76vvgkplx23d0MJP1rJKjIByHeQfZjOyHh0_M5-k'
    transferfiles=TransferData(access_token)

    file_from= input('Enter the file path to transfer: ')
    file_to= input('Enter the path to upload to dropbox: ')

    transferfiles.upload_files(file_from,file_to)
    print('File has been moved successfully')

main()