import time
import json

class Recieve():
    def __init__(self):
        self.old_guild = []
        self.new_messages = []
        self.main()

    def cleanup(self, text):
        text = list(text)

        while True:
            if '§' in ''.join(text):
                pos = text.index('§')
                text.pop(pos)
                text.pop(pos)
            else:
                break

        return ''.join(text)
                
    def remove_dup(self, longer, shorter):
        new = []
        for msg in longer:
            if not(msg in shorter):
                new.append(msg)
        return new

    def main(self):
        while True:
            running = True
            with open(r"C:\Users\Ethan\AppData\Roaming\.minecraft\logs\latest.log", "r") as f:
                self.guild = []
                while running:
                    line = f.readline()
                    if line:
                        if "[Client thread/INFO]: [CHAT] §2Guild >" in line:
                            self.guild.append(self.cleanup(line.replace('[Client thread/INFO]: [CHAT] §2Guild >', '').replace('\n', '')[12:]))
                        elif "[Client thread/INFO]: [CHAT] Guild >" in line:
                            self.guild.append(self.cleanup(line.replace("[Client thread/INFO]: [CHAT] Guild >",'').replace('\n','')[12:]))
                    else:
                        running = False
                self.update()

    def update(self):
        if self.guild != self.old_guild:
            new_messages = self.remove_dup(self.guild, self.old_guild)
            print(f'new msg: {new_messages}')
            with open('new_messages.txt', 'w') as m:
                m.write(f"{new_messages}")
                m.write('\n')

            self.old_guild = self.guild
            with open('chat.json', 'w') as f:
                f.write(json.dumps(self.guild))
            time.sleep(0.5)

if __name__ == '__main__':
    recieve = Recieve()
    recieve()