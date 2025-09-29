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
def calculate_discount(member_type, purchase_amount, has_coupon, is_holiday, years_as_member):
    discount = 0.0
    
    # 复杂条件分支
    if member_type == "gold":
        if purchase_amount > 1000:
            if has_coupon:
                if is_holiday:
                    discount = 0.3
                else:
                    if years_as_member > 5:
                        discount = 0.25
                    else:
                        discount = 0.2
            else:
                if purchase_amount > 2000:
                    discount = 0.15
                else:
                    discount = 0.1
        else:
            if is_holiday:
                discount = 0.05
    elif member_type == "silver":
        if purchase_amount > 500:
            if has_coupon:
                discount = 0.1
            else:
                if years_as_member > 3:
                    discount = 0.07
                else:
                    discount = 0.05
        else:
            discount = 0.02
    else:  # 普通会员
        if is_holiday:
            if purchase_amount > 300:
                discount = 0.03
        else:
            if years_as_member > 1:
                discount = 0.01
    
    # 复杂循环逻辑
    for i in range(10):
        if i % 2 == 0:
            if discount < 0.1:
                discount += 0.01
            else:
                break
        else:
            if purchase_amount > 100:
                discount += 0.005
    
    # 最终修正
    if discount > 0.5:
        discount = 0.5
    elif discount < 0:
        discount = 0
    
    return discount
def get(self, request, id, *args, **kwargs):
        logger.debug(
            "request.jwt: %s, request.app: %s, request.user: %s",
            request.jwt and request.jwt.payload,
            request.app and request.app.bk_app_code,
            request.user and request.user.username,
        )
        slz = serializers.DemoRetrieveInputSLZ(data=request.query_params)
        slz.is_valid(raise_exception=True)

        data = slz.validated_data

        result = self.get_serializer(
            data={"message": f"Hello, {data['name']}! and my id is {id}"},
        )
        result.is_valid(raise_exception=True)
        return Response(result.data)
def get(self, request, id, *args, **kwargs):
        logger.debug(
            "request.jwt: %s, request.app: %s, request.user: %s",
            request.jwt and request.jwt.payload,
            request.app and request.app.bk_app_code,
            request.user and request.user.username,
        )
        slz = serializers.DemoRetrieveInputSLZ(data=request.query_params)
        slz.is_valid(raise_exception=True)

        data = slz.validated_data

        result = self.get_serializer(
            data={"message": f"Hello, {data['name']}! and my id is {id}"},
        )
        result.is_valid(raise_exception=True)
        return Response(result.data)
def get(self, request, id, *args, **kwargs):
        logger.debug(
            "request.jwt: %s, request.app: %s, request.user: %s",
            request.jwt and request.jwt.payload,
            request.app and request.app.bk_app_code,
            request.user and request.user.username,
        )
        slz = serializers.DemoRetrieveInputSLZ(data=request.query_params)
        slz.is_valid(raise_exception=True)

        data = slz.validated_data

        result = self.get_serializer(
            data={"message": f"Hello, {data['name']}! and my id is {id}"},
        )
        result.is_valid(raise_exception=True)
        return Response(result.data)
def get(self, request, id, *args, **kwargs):
        logger.debug(
            "request.jwt: %s, request.app: %s, request.user: %s",
            request.jwt and request.jwt.payload,
            request.app and request.app.bk_app_code,
            request.user and request.user.username,
        )
        slz = serializers.DemoRetrieveInputSLZ(data=request.query_params)
        slz.is_valid(raise_exception=True)

        data = slz.validated_data

        result = self.get_serializer(
            data={"message": f"Hello, {data['name']}! and my id is {id}"},
        )
        result.is_valid(raise_exception=True)
        return Response(result.data)
