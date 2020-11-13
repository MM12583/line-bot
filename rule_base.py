trigger = input('指定句: ')
reply = input('回應句: ')

class Rule :
    def __init__(self) :
        self.answer = {}
        self.read_data('add_reply.csv')

    def read_data(self, file = 'add_reply.csv') :
        with open ('add_reply.csv' , 'r', encoding = 'utf-8') as f :
            for line in f :
                if '指定句:回應句' in line :
                    continue
                trigger, reply = line.strip().split(':')

                if trigger in self.answer :
                    continue    
                self.answer[trigger] = reply
        return self.answer

    def create_answer(self, trigger, reply) :
        if trigger not in self.answer :
            self.answer[trigger] = reply

        with open ('add_reply.csv' , 'a+', encoding = 'utf-8') as f :
            f.write(trigger + ':' + reply + '\n')

    def response(self) :
        print(self.answer[trigger])

rule = Rule()
if trigger in rule.answer :
    rule.response()
else :
    rule.create_answer(trigger, reply)
    rule.response()