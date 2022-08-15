
from kiwipiepy import Kiwi 

class IOHandler:
    def __init__(self, input, output):
        self.input = open(input, encoding='utf-8')
        self.output = open(output, 'w', encoding='utf-8')

    def read(self, sent_id):
        if sent_id == 0:
            self.input.seek(0)
            self.iter = iter(self.input)
        try:
            return next(self.iter)
        except StopIteration:
            return None

    def write(self, sent_id, res):
        print('Analyzed %dth row' % sent_id)
        self.output.write(' '.join(map(lambda x:x[0]+'/'+x[1], res[0][0])) + '\n')

    def __del__(self):
        self.input.close()
        self.output.close()
    
class NLP():
    """ 
    kiwi 형태소 분석기를 실행합니다.
    """
    
    def __init__(self):
        self.kiwi = Kiwi()
        self.kiwi.prepare()
    
    def analyze(self, txt:str, top_n=int):
        """  
        형태소 분석 실행
        :param txt: 분석 대상 텍스트
        :param top_n: 결과 후보 개수 출력
        :return: kiwi Token 객체
        """
        return self.kiwi.analyze(txt,  top_n)
    
    def get_pos(self, res):
        """ 
        형태소 분석의 태깅 리스트 반환
        
        """
        pos = []
        for token in res[0][0]:
            pos.append(token.tagged_form)
        return pos


if __name__ == '__main__':

    kiwi = NLP()
    res = kiwi.analyze("어 그런데에서 빨래 개 봐서 또 잘하나 보다", 1)
    pos = kiwi.get_pos(res)
    