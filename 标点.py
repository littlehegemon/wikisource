# -*- coding: utf-8 -*-

import difflib

BIAODIAN_beginning = list("([{<❨❴⟨【〔〘《〈“‘「『")
BIAODIAN_ending = list("’')]}>❩❵⟩】〕〙：，、‒–—―~─….！。》〉﹏＿～‐?？”")
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


""".replace("\n", "").replace("　", "")

# source of biaodian
text2 = """威烈王
威烈王二十三年（戊寅，西元前四〇三年）
1　〔九鼎震〕[1]，初命晋大夫魏斯、赵籍、韩虔为诸侯。

臣光曰：臣闻天子之职莫大于礼，礼莫大于分，分莫大于名。何谓礼？纪纲是也；何谓分？君臣是也；何谓名？公、侯、卿、大夫是也。
夫以四海之广，兆民之众，受制于一人，虽有绝伦之力，高世之智，莫敢不奔走而服役者，岂非以礼为之〔纪〕纲(纪)哉[2]！是故天子统三公，三公率诸侯，诸侯制卿大夫，卿大夫治士庶人。贵以临贱，贱以承贵。上之使下，犹心腹之运手足，根本之制支叶；下之事上，犹手足之卫心腹，支叶之庇本根。然后能上下相保而国家治安。故曰：天子之职莫大于礼也。
文王序《易》，以乾坤为首。孔子系之曰：“天尊地卑，乾坤定矣，卑高以陈，贵贱位矣。”言君臣之位，犹天地之不可易也。《春秋》抑诸侯，尊〔周〕(王)室[3]，王人虽微，序于诸侯之上，以是见圣人于君臣之际，未尝不惓惓也。非有桀、纣之暴，汤、武之仁，人归之，天命之，君臣之分，当守节伏死而已矣。是故以微子而代纣，则成汤配天矣；以季札而君吴，则太伯血食矣。然二子宁亡国而不为者，诚以礼之大节不可乱也。故曰：礼莫大于分也。
夫礼，辨贵贱，序亲疏，裁群物，制庶事。非名不著，非器不形。名以命之，器以别之，然后上下粲然有伦，此礼之大经也。名器既亡，则礼安得独在哉？昔仲叔于奚有功于卫，辞邑而请繁缨，孔子以为不如多与之邑。惟器与名，不可以假人，君之所司也。政亡，则国家从之。卫君待孔子而为政，孔子欲先正名，以为名不正则民无所措手足。夫繁缨，小物也，而孔子惜之；正名，细务也，而孔子先之。诚以名器既乱，则上下无以相有故也。夫事未有不生于微而成于著。圣人之虑远，故能谨其微而治之；众人之识近，故必待其著而后救之。治其微，则用力寡而功多；救其著，则竭力而不能及也。《易》曰：“履霜，坚冰至”，《书》曰：“一日二日万几”，谓此类也。故曰：分莫大于名也。
呜呼！幽、厉失德，周道日衰，纲纪散坏，下陵上替，诸侯专征，大夫擅政。礼之大体，什丧七八矣。然文、武之祀犹绵绵相属者，盖以周之子孙尚能守其名分故也。何以言之？昔晋文公有大功于王室，请隧于襄王，襄王不许，曰：“王章也。未有代德而有二王，亦叔父之所恶也。不然，叔父有地而隧，又何请焉！”文公于是乎惧而不敢违。是故以周之地则不大于曹、滕，以周之民则不众于邾、莒，然历数百年，宗主天下，虽以晋、楚、齐、秦之强，不敢加者，何哉？徒以名分尚存故也。至于季氏之于鲁，田〔恒〕(常)之于齐[4]，，白公之于楚，智伯之于晋，其势皆足以逐君而自为，然而卒不敢者，岂其力不足而心不忍哉？乃畏奸名犯分而天下共诛之也。今晋大夫暴蔑其君，剖分晋国，天子既不能讨，又宠秩之，使列于诸侯，是区区之名分复不能守而并弃之也。先王之礼于斯尽矣。或者以为当是之时，周室微弱，三晋强盛，虽欲勿许，其可得乎？是大不然。夫三晋虽强，苟不顾天下之诛而犯义侵礼，则不请于天子而自立矣。不请于天子而自立，则为悖逆之臣。天下苟有桓、文之君，必奉礼义而征之。今请于天子而天子许之，是受天子之命而为诸侯也，谁得而讨之！故三晋之列于诸侯，非三晋之坏礼，乃天子自坏之也。"""

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
    Matcher = difflib.SequenceMatcher(lambda x: x in BIAODIAN + ["\n"], merge_similar_chars(text1),
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
