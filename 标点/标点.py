# -*- coding: utf-8 -*-

import difflib

BIAODIAN_beginning = "([{<❨❴⟨【〔〘《〈“‘「『"
BIAODIAN_ending = "’')]}>❩❵⟩】〕〙：，、‒–—―~─….！。》〉﹏＿～‐?？”』」"
BIAODIAN = BIAODIAN_beginning + BIAODIAN_ending

# to be added
text1 = """夫卿大夫治士庶人貴以臨賤賤以承貴上之使下猶

心腹之運手足根本之制支葉下之事上猶手足之衛

心腹支葉之庇本根然後能上下相保而國家治安故

曰天子之職莫大於禮也文王序易以乾坤爲首孔子

繫之曰天尊地卑乾坤定矣卑高以陳貴賤位矣言君

臣之位猶天地之不可易也春秋抑諸矦尊周室王人

雖微序於諸矦之上以是見聖人於君臣之際未甞不

惓惓也非有桀紂之暴湯武之仁人歸之天命之君臣

之分當守節伏死而已矣是故以微子而代紂則成湯

配天矣以季札而君吳則太伯血食矣然二子寜亡國

而不爲者誠以禮之大節不可亂也故曰禮莫大於分


"""

# source of biaodian
text2 = """诸侯制卿大夫，卿大夫治士庶人。贵以临贱，贱以承贵。上之使下，犹心腹之运手足，根本之制支叶；下之事上，犹手足之卫心腹，支叶之庇本根。然后能上下相保而国家治安。故曰：天子之职莫大于礼也。
文王序《易》，以乾坤为首。孔子系之曰：“天尊地卑，乾坤定矣，卑高以陈，贵贱位矣。”言君臣之位，犹天地之不可易也。《春秋》抑诸侯，尊〔周〕(王)室[3]，王人虽微，序于诸侯之上，以是见圣人于君臣之际，未尝不惓惓也。非有桀、纣之暴，汤、武之仁，人归之，天命之，君臣之分，当守节伏死而已矣。是故以微子而代纣，则成汤配天矣；以季札而君吴，则太伯血食矣。然二子宁亡国而不为者，诚以礼之大节不可乱也。故曰：礼莫大于分也。"""

text2=text2.replace("“","「").replace("‘","『").replace("’","』").replace("”","」")


char_list = []
table = open("related_chars.txt", "r", encoding="utf-8")
for row in table.readlines():
    chars = list(row)
    char_list.append(chars)


def merge_similar_chars(text):
    # 合并类似的字符，可用于比较
    for char in char_list:
        for i in range(1, len(char)):
            text = text.replace(char[i], char[0])
    return text


def add_biaodian(text1, text2, biaodian_positions_1, biaodian_positions_2):
    # 输入：待标点文字，已标点文字，待标点文字标点位置列表，已标点文字标点位置列表
    # 输出：待标点文字变为带标点文字
    biaodian_list = []
    for positions_2 in biaodian_positions_2:
        biaodian_list.append(text2[positions_2])
    biaodian_positions_1.insert(0, 0)
    splited_text = [text1[i:j] for i, j in zip(biaodian_positions_1, biaodian_positions_1[1:] + [None])]
    text1_putout = ""

    for i, sentence in enumerate(splited_text):
        if i < len(splited_text) - 1:
            biaodian_position_2 = biaodian_positions_2[i]
            biaodian = text2[biaodian_position_2]
        else:
            biaodian = ""
        text1_putout = text1_putout + sentence + biaodian
    return text1_putout


def find_biaodian_postisions(text1, text2):
    # 输入：待标点文字，已标点文字
    # 输出：待标点文字标点位置列表，已标点文字标点位置列表
    Matcher = difflib.SequenceMatcher(lambda x: x in BIAODIAN + " \t\n", merge_similar_chars(text1),
                                      merge_similar_chars(text2), )
    biaodian_positions_1 = []
    biaodian_positions_2 = []
    for block in Matcher.get_opcodes():
        behaviour = block[0]
        text1_start = block[1]
        text1_end = block[2]
        text2_start = block[3]
        text2_end = block[4]
        if behaviour == "insert":
            for position in range(text2_start, text2_end):
                if text2[position] in BIAODIAN:
                    if text1_start > 0:
                        biaodian_positions_2.append(position)
                        biaodian_positions_1.append(text1_start)

        if behaviour == "replace":
            for position in range(text2_start, text2_end):
                if text2[position] in BIAODIAN:
                    if text1_start > 0:
                        biaodian_positions_2.append(position)
                        biaodian_positions_1.append(text1_start)

    return (biaodian_positions_1, biaodian_positions_2)


(biaodian_positions_1, biaodian_positions_2) = find_biaodian_postisions(text1, text2)

putout = add_biaodian(text1, text2, biaodian_positions_1, biaodian_positions_2)

print(putout)
