import re

PRIVATE_MODIFIER = 'access modifier: private'
PROTECTED_MODIFIER = 'access modifier: protected'
PUBLIC_MODIFIER = 'access modifier: public'
TYPENAME = 'typename'
ANNOTATION = 'annotation'
ID = 'id'
SEMICOLON = 'semicolon'
NEW_LINE = 'new line'
WHITE_SPACE = 'white space'
NOTE = 'note'
NULL_CHAR = 'null character'

TOKEN_REGULAR = {
    PRIVATE_MODIFIER: r'private',
    PROTECTED_MODIFIER: r'protected',
    PUBLIC_MODIFIER: r'public',
    TYPENAME: r'[a-zA-Z\<\>]+',
    ID: r'[a-zA-Z_][a-zA-Z0-9_]*',
    ANNOTATION: r'@.*\n',
    SEMICOLON: r';',
    NEW_LINE: r'\n',
    WHITE_SPACE: r'\s+',
    NULL_CHAR: r'[\s\n]+',
    NOTE: r'\/\/[^\n]*|\/\*[\s\S]*?\*\/',
}

TOKEN_PATTERN = {name: re.compile(pattern) for name, pattern in TOKEN_REGULAR.items()}

MODIFIER_MAP = {PRIVATE_MODIFIER: '-', PROTECTED_MODIFIER: '#', PUBLIC_MODIFIER: '+'}
ONE = 1

if __name__ == '__main__':
    # long length ============================================================================================================================================================================================================================
    a_b_c = ONE
    a_c_d = None
    b_g_f = 1

    try:
        print(f'param:{param}')
        if param != "" and param.get("chart id") is not None and param.get("chart id") != "":
            self.chart_id = param.get("chart id")
            param = param.get("param")
            print(self.chart_id)
        # 生成查询条件
        self.conditions = self.check_query_condition(param)
        # 查询告警判定推送的告警数据
        new_result = pd.read_excel('2023103014.xlsx', sheet_name = None)
        new_titan_result = new_result.get('新Titan告警数据')  # pd.read_csv('data1.csv') # self.new titan_query()
        # 查询titan推送的告警数据
        old_titan_result = new_result.get('老Titan告警数据')
    except Exception as e:
        log.exception(e)
        contents = {
            "chatid": self.chart_id,
            "msgtype": "text",
            "text": {
                "content": f'出现异常:{e}，请查看详细日志',
                "mentioned list":self.mentioned_list
            }
        }

    CODE = ''
    with open('code.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            CODE += line

    # print(code)
    RESULT = ''

    # print(TOKEN_PATTERN)

    pos = 0
    while pos < len(CODE):
        for token, pattern in TOKEN_PATTERN.items():
            m = pattern.match(CODE[pos:])

            if m is not None:
                # print(m.group(0))
                pos += len(m.group(0))

                if token == PRIVATE_MODIFIER or token == PROTECTED_MODIFIER or token == PUBLIC_MODIFIER:
                    modifier = MODIFIER_MAP[token]

                    m = TOKEN_PATTERN[NULL_CHAR].match(CODE[pos:])
                    pos += len(m.group(0))

                    m = TOKEN_PATTERN[TYPENAME].match(CODE[pos:])
                    typename = m.group(0)
                    pos += len(m.group(0))

                    m = TOKEN_PATTERN[NULL_CHAR].match(CODE[pos:])
                    if m is None:
                        print(CODE[pos:])
                    pos += len(m.group(0))

                    m = TOKEN_PATTERN[ID].match(CODE[pos:])
                    idname = m.group(0)
                    pos += len(m.group(0))

                    m = TOKEN_PATTERN[SEMICOLON].match(CODE[pos:])
                    pos += len(m.group(0))

                    RESULT += modifier + ' ' + idname + ': ' + typename + '\n'
                break

    print(RESULT)
