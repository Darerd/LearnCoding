from pypinyin import pinyin, lazy_pinyin


def get_acronym(str_data):
    """
    获取字符串的首字母
    :param str_data: 字符串
    :return: 字符串
    """
    return "".join([i[0][0] for i in pinyin(str_data)])


if __name__ == '__main__':
    #print('拼音', lazy_pinyin('婺城区'))
    #print('拼音', pinyin('䆔'))

    #print("首字母", get_acronym('䆔心坡，你好'))
    game="卡牌,跑酷,塔防守卫,角色扮演,赛车竞速,格斗,射击,冒险,体育,休闲益智,策略经营,棋牌娱乐,MOBA"
    #letter= get_acronym(game)
    print(str(game))
    #m=list(d)
    #m.sort()
    #d="".join(m)
    #print(d)

