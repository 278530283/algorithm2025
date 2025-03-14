names = ["大姐", "二姐", "小妹"]
actions = ["没拿", "拿钱"]


#逻辑判断：
#撒谎的人与其他人应该逻辑矛盾，而诚实的人应该逻辑一致
def logic_check(lie_index, honest_index_1, honest_index_2):
    difference = 0
    #遍历陈述
    for i in range(len(statements[honest_index_1])):
        # 若诚实人的陈述不一致，则矛盾
        if statements[honest_index_1][i] != -1 and statements[honest_index_2][i] != -1 and statements[honest_index_1][i] != statements[honest_index_2][i]:
            print("逻辑矛盾，另外两人陈述的应该相同。")
            return False
        # 若撒谎人与诚实人陈述不一致的次数
        if statements[honest_index_1][i] != -1 and statements[honest_index_2][i] != -1 and statements[lie_index][i] != statements[honest_index_1][i]:
            difference += 1
    # 诚实的人与撒谎人陈述完全一致
    if difference == 0:
        print("逻辑矛盾，撒谎的人与诚实的人应该不同。")
        return False
    print("逻辑正确。")
    return True


#逻辑判断算法题目：考察通过向量表达所有可能情况，再用枚举法逐个判断，若出现矛盾，则推翻建设
if __name__ == "__main__":
    statements = [[1, 0, 0], [0, 1, 0], [0, 1, 0]]
    lie_person_possible = [0, 1, 2]
    for lie_person in lie_person_possible:
        print()
        honest_index_1 = (lie_person + 1) % 3
        honest_index_2 = (lie_person + 2) % 3
        print("假设撒谎的人是", names[lie_person])
        if logic_check(lie_person, honest_index_1, honest_index_2):
            print()
            print("找到答案")
            print("撒谎的人：" + names[lie_person])
            for i in range(len(statements[honest_index_1])):
                if statements[honest_index_1][i] == 1:
                    print("拿钱的人：" + names[i])
            break
