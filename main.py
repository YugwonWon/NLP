# -*- coding: utf-8 -*-
# nohup python3 main.py > out.log
from kiwipiepy import Kiwi 
from tqdm import tqdm
import glob
import csv


class NLP():
    """ 
    kiwi 형태소 분석기를 실행합니다.
    형태소 분석에 필요한 메소드를 구현합니다.
    
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
    
    def data_loader(self, path):
        """ 
        txt파일의 문장을 읽어서 리스트로 저장한다.
        """
        sentence = []
        txts = glob.glob(path)
        for txt in txts:
            with open(txt, 'r', encoding='utf-8') as readfile:
                txt_lines = readfile.readlines()
                sentence.append(txt_lines)
        
        return sentence
    

class WordList():
    """ 
    목표 단어 로딩 및 단어 사전 생성 객체
    
    """
    def __init__(self):
        self.verb_wordlist = ["간당간당하", "간드러지", "간질간질하", "갈팡질팡하", "감사하", "감지덕지하", "걸맞", "결리", "궁상맞", "그르", "근질근질하", "글썽글썽하", "기막히", "까끌까글하", "까딱까딱하", "까불까불하", "깜빡깜빡하", "꼼지락꼼지락하", "꽁하", "꾸물꾸물하", "너덜너덜하", "눈부시", "늦", "달랑달랑하", "덜컹덜컹하", "두근두근하", "뒤숭숭하", "들썩하", "들어맞", "따끈따끈하", "따끔따끔하", "떠들썩하", "떨리", "뜨끔뜨끔하", "뜨끔하", "뜨악하", "마르", "말랑말랑하", "맞", "머뭇머뭇하", "멈칫멈칫하", "메슥메슥하", "모자라", "몽글몽글하", "물렁물렁하", "물컹물컹하", "미끌미끌하", "바글바글하", "반짝반짝하", "발그레하", "방정맞", "번들번들하", "번쩍번쩍하", "벙벙하", "부글부글하", "부들부들하", "부치", "부합하", "북적북적하", "삐걱삐걱하", "산뜩하", "새근새근하", "샐쭉하", "섬찟섬찟하", "술렁술렁하", "시끌시끌하", "시리", "시큰시큰하", "쑤시", "쓰리", "아른아른하", "아리까리하", "아리", "아리송하", "아릿아릿하", "안녕하", "안절부절못하", "어둑어둑하", "어질어질하", "엄청나", "오싹하", "오지", "왁자지껄하", "우글우글하", "욱신욱신하", "울렁울렁하", "움푹움푹하", "웃기", "웅성웅성하", "위태위태하", "유별나", "으쓱하", "이글이글하", "잇", "자글자글하", "재미나", "재잘재잘하", "저리", "저릿저릿하", "조마조마하", "졸리", "지끈지끈하", "지나치", "지르르하", "질척거리", "징글징글하", "짜르르하", "쩌렁쩌렁하", "쩌릿쩌릿하", "쩌릿쩌릿하", "쫀득쫀득하", "쫄깃쫄깃하", "쭈글쭈글하", "쭈뼛쭈뼛하", "쭈뼛하", "찌릿찌릿하", "찡하", "찰랑찰랑하", "철렁철렁하", "틀리", "헤롱헤롱하", "화끈화끈하", "후끈후끈하", "힘들"]
        self.mag_wordlist = ["간당간당", "간질간질", "갈팡질팡", "감사", "감지덕지", "근질근질", "글썽글썽", "까끌까글", "까딱까딱", "까불까불", "깜빡깜빡", "꼼지락꼼지락", "꽁", "꾸물꾸물", "너덜너덜", "달랑달랑", "덜컹덜컹", "두근두근", "뒤숭숭", "들썩", "따끈따끈", "따끔따끔", "떠들썩", "뜨끔뜨끔", "뜨끔", "뜨악", "말랑말랑", "머뭇머뭇", "멈칫멈칫", "메슥메슥", "몽글몽글", "물렁물렁", "물컹물컹", "미끌미끌", "바글바글", "반짝반짝", "발그레", "번들번들", "번쩍번쩍", "벙벙", "부글부글", "부들부들", "부합", "북적북적", "삐걱삐걱", "산뜩", "새근새근", "샐쭉", "섬찟섬찟", "술렁술렁", "시끌시끌", "시큰시큰", "아른아른", "아리까리", "아리송", "아릿아릿", "안녕", "안절부절못", "어둑어둑", "어질어질", "오싹", "왁자지껄", "우글우글", "욱신욱신", "울렁울렁", "움푹움푹", "웅성웅성", "위태위태", "으쓱", "이글이글", "자글자글", "재잘재잘", "저릿저릿", "조마조마", "지끈지끈", "지르르", "징글징글", "짜르르", "쩌렁쩌렁", "쩌릿쩌릿", "쩌릿쩌릿", "쫀득쫀득", "쫄깃쫄깃", "쭈글쭈글", "쭈뼛쭈뼛", "쭈뼛", "찌릿찌릿", "찡", "찰랑찰랑", "철렁철렁", "헤롱헤롱", "화끈화끈", "후끈후끈"]
        
    def make_dict(self):
        verb_dict = {string : [] for string in self.verb_wordlist}
        mag_dict = {string : [] for string in self.mag_wordlist}
        return verb_dict, mag_dict

    def save_dict(self, key, verb_list):
        """ 
        최종적으로 저장된 dict의 값을 받아와 tsv파일로 key별로 파일을 저장합니다.
        
        """
        with open(key, 'a', encoding='utf-8') as file:
            tw = csv.writer(file, delimiter='\t')
            for line in verb_list:
                tw.writerow(line)
                
    def save(self, dict, prefix):
        for key in dict.keys():
            if len(dict[key]) != 0:
                self.save_dict(f'./out/{prefix}/{key}.tsv', dict[key])
                
    def save_all_tsv(self, final_lines):
        # 최종적으로 저장된 final_lines 리스트를 탭으로 구분된 tsv 형식으로 저장합니다.
        with open('verb.tsv', 'w', encoding='utf-8') as f:
            tw = csv.writer(f, delimiter='\t')
            for line in final_lines:
                tw.writerow(line)
        
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    nlp = NLP()
    word_list = WordList()
    verb_dict, mag_dict = word_list.make_dict()
    
    data = nlp.data_loader("/Users/yugwon/Desktop/projects/NLP/many_sent/*.txt")

    final_lines = []
    for cp, lines in enumerate(data):
        cp = f'{cp}' # corpus번호(3,418,818문장) : 0 NIA회의음성데이터, 1 NIA한국인대화음성데이터, 2 NIA감정대화말뭉치, 3 NIA자유발화
        for line in tqdm(lines): # tqdm은 남은 진행사항을 표시해주는 패키지(pip install tqdm)
            try:
                line = line.strip()
                res = nlp.analyze(line, 1)
                sent_pos = nlp.get_pos(res)
                
                vv = None
                vv_idx = 0
                vv_content = None
                
                nng = None
                nng_idx = 0
                nng_content = None 
                mag = None
                mag_idx = 0
                mag_content = None
                
                xsv = None
                mag_xsv = None
                nng_xsv = None
                verb_line = [] # final_lines에 넣기 전 단계

                for idx, token in enumerate(sent_pos):
                    token_split = token.split("/")
                    content = token_split[0]
                    tag = token_split[1]

                    if tag == "VV" or tag == "VA":
                        if content in word_list.verb_wordlist:
                            vv = token 
                            vv_content = content
                            vv_idx = idx
                    elif tag == "NNG":
                        if content in word_list.mag_wordlist:
                            nng = content 
                            nng_idx = idx 
                            nng_content = content 
                    elif (tag == "XSV" or tag == "XSA") and idx - 1 == nng_idx and mag == None:
                        nng_xsv = f'{nng}{content}/NNG+{tag}'
                    elif tag == "MAG":
                        if content in word_list.mag_wordlist:
                            mag = content 
                            mag_content = content 
                            mag_idx = idx    
                    elif ( tag == "XSV" or tag == "XSA") and idx - 1 == mag_idx:
                        mag_xsv = f'{mag}{content}/MAG+{tag}'
                    elif (tag == "EF" or  tag == "EC" or tag == "ETM"):
                        # 현재 형태소 분석 형태가 EF, EC, ETM이고 vv가 저장된 경우
                        if idx - vv_idx == 1 and vv != None:                   
                            verb_line.append(vv)
                            verb_line.append(content)
                            verb_line.append(tag)
                            verb_line.append(line)
                            verb_line.append(cp)
                            final_lines.append(verb_line)
                            verb_dict[vv_content].append(verb_line)
                            verb_line = [] 
                            vv = None # vv 변수 초기화
                            vv_idx = 0
                        # MAG+XSV가 저장된 경우    
                        elif idx - 2 == mag_idx and mag != None:
                            verb_line.append(mag_xsv)
                            verb_line.append(content)
                            verb_line.append(tag)
                            verb_line.append(line)
                            verb_line.append(cp)
                            final_lines.append(verb_line)
                            mag_dict[mag_content].append(verb_line)
                            verb_line = [] # 초기화
                            mag = None # mag+xsv 변수 초기화
                            mag_idx = 0
                            xsv = None
                            mag_xsv = None
                        # NNG+XSV가 저장된 경우    
                        elif idx - 2 == nng_idx and nng != None:
                            verb_line.append(nng_xsv)
                            verb_line.append(content)
                            verb_line.append(tag)
                            verb_line.append(line)
                            verb_line.append(cp)
                            final_lines.append(verb_line)
                            mag_dict[nng_content].append(verb_line)
                            verb_line = [] # 초기화
                            nng = None # mag+xsv 변수 초기화
                            nng_idx = 0
                            xsv = None
                            nng_xsv = None     
                
            # 형태소 분석 에러 발생시 이를 예외 처리하고 계속 넘어가도록 한다.
            except Exception as e: 
                print(e)
                print(f'Error line: {line}')
                continue        
            
    # 모든 라인을 하나의 파일에 저장
    word_list.save_all_tsv(final_lines)
    
    # dict에서 각 key에 저장된 verb리스트를 tsv 형식으로 저장합니다.
    word_list.save(verb_dict, "verb")
    word_list.save(mag_dict, "mag")


    