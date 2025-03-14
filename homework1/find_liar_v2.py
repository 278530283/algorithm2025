import itertools


def find_liar_and_thief(statements):
    names = [stmt.name for stmt in statements]
    solutions = []

    for liar_candidate in names:
        # 处理每个陈述，说谎者的陈述取反
        processed_statements = []
        for stmt in statements:
            target, value = stmt.statement
            if stmt.name == liar_candidate:
                # 说谎者的陈述取反
                processed_value = 1 - value
            else:
                processed_value = value
            processed_statements.append((target, processed_value))

        # 找出满足所有处理后的陈述的thief候选人
        possible_thieves = []
        for thief_candidate in names:
            valid = True
            for (target, value) in processed_statements:
                if target == thief_candidate:
                    if value != 1:
                        valid = False
                        break
                else:
                    if value != 0:
                        valid = False
                        break
            if valid:
                possible_thieves.append(thief_candidate)

        # 必须唯一确定一个thief
        if len(possible_thieves) != 1:
            continue

        thief = possible_thieves[0]
        solutions.append((liar_candidate, thief))

    # 检查解的唯一性
    if len(solutions) == 1:
        return solutions[0]
    else:
        raise ValueError(f"无法确定唯一的解，找到 {len(solutions)} 个可能解")


class PersonStatement:
    def __init__(self, name, statement_str):
        self.name = name
        self.statement_str = statement_str
        self.statement = self.parse_statement()

    def parse_statement(self):
        import re
        # 使用正则表达式解析陈述内容
        match = re.match(r'^(.*?)(拿|没拿)$', self.statement_str)
        if not match:
            raise ValueError(f"Invalid statement: {self.statement_str}")

        target_part, action = match.groups()
        # 处理"我"的情况，替换为当前对象的名字
        target = self.name if target_part == "我" else target_part
        # 确定是否拿钱（1表示拿了，0表示没拿）
        value = 1 if action == "拿" else 0

        return (target, value)


# 生成每个说话者的所有可能陈述
def generate_statements(name):
    statements = []
    # 自己
    statements.append("我拿")
    statements.append("我没拿")
    # 其他人
    others = [n for n in names if n != name]
    for other in others:
        statements.append(f"{other}拿")
        statements.append(f"{other}没拿")
    return statements


if __name__ == "__main__":

    names = ["大姐", "二姐", "小妹"]

    possible_statements = {name: generate_statements(name) for name in names}

    # 生成所有可能的陈述组合
    all_combinations = itertools.product(
        possible_statements["大姐"],
        possible_statements["二姐"],
        possible_statements["小妹"]
    )

    # 遍历所有组合
    for dajie_stmt, erjie_stmt, xiaomei_stmt in all_combinations:
        # 创建PersonStatement实例
        statements = [
            PersonStatement("大姐", dajie_stmt),
            PersonStatement("二姐", erjie_stmt),
            PersonStatement("小妹", xiaomei_stmt),
        ]

        # 调用find_liar_and_thief函数
        try:
            liar, thief = find_liar_and_thief(statements)
            print(f"当大姐说'{dajie_stmt}'，二姐说'{erjie_stmt}'，小妹说'{xiaomei_stmt}'时：")
            print(f"说谎的人: {liar}")
            print(f"拿钱的人: {thief}\n")
        except Exception as e:
            print(f"错误组合：{dajie_stmt}, {erjie_stmt}, {xiaomei_stmt}，错误信息：{e}")

