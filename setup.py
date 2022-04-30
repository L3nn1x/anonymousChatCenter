import os

def main():

    try:
        if os.name in 'nt':
            os.system('python.exe -m pip install --upgrade pip')
            os.system('pip3 install colorama')
            os.system('pip3 install sucket')
            os.system('pip3 install threading')


        else:
            os.system('sudo apt-get install python3')
            os.system('sudo apt-get install pip')
            os.system('sudo pip3 install colorama')
            os.system('sudo pip3 install sucket')
            


    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
