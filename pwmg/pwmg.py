import json, sys, os, shutil, time, base64

class pwmg:
    def __init__(self) -> None:
        self.dir          = os.path.dirname(os.path.abspath(__file__))
        self.jsonfilepath = self.dir + '/password.json'
        self.tmpdir       = self.dir + '/.tmp'
        self.secret_key   = b'16バイトの任意の文字列を指定する'
        self.check_masterpass()
        self.mknewfile()

    def get_pass(self):
        try:
            with open(self.jsonfilepath, 'r') as json_data:
                json_obj     = json.load(json_data)
                target_label = sys.argv[2]
                target_key   = sys.argv[3]
                return_value = self.decrypt(json_obj[target_label][target_key])
                print(return_value)
        except IOError:
            print('IOError: ファイルを開くことができませんでした。')
        except KeyError:
            print('KeyError: 指定した値がパスワードリストにない可能性があります。')
        except IndexError: 
            print('IndexError: 引数の数に問題がある可能性があります。')
        except Exception as e:
            raise e

    # Create backup json file
    def backup(self):
        self.mkdir()
        shutil.copy(self.jsonfilepath, self.tmpdir + '/tmp.' + str(time.time()))

    # Create backup directory
    def mkdir(self):
        if os.path.isdir(self.tmpdir) is False:
            os.mkdir(self.tmpdir)