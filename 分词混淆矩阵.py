# -*- coding: utf-8 -*-
# @Author   :Yangyyz
import pkuseg
import time
import jieba
import thulac
import re
import pip
from snownlp import SnowNLP
import pynlpir

f = open("新增-express.txt",encoding='UTF-8')#读取原始摘要
s = f.read()
# print(s)

# 标准分词
f1 = open("standard_express.txt",encoding='UTF-8')
s1 = ['由于', 'ZrO2', '-', 'C质', '耐火材料', '具有', '优异', '的', '抗', '侵蚀性', '，', '因此', '它', '被', '广泛', '应用', '于', '连铸用', '浸入式', '水口', '渣线', '部位', '以及', '塞棒', '的', '棒头', '部位', '。', '本文', '介绍', '了', 'ZrO2', '-', 'C质', '耐火材料', '的', '主要', '原料', '，', '阐述', '了', 'ZrO2', '-', 'C质', '耐火材料', '的', '蚀损', '机理', '以及', '改进', '抗', '侵蚀性','的', '措施', '。','材料', '化学', '是', '一门', '新兴', '的', '交叉', '学科', '，', '其', '专业', '实践', '课程', '是', '培养', '好', '专门', '人才', '的', '一个', '重要', '途径', '。', '本文', '以', '工科', '应用型', '人才', '培养', '为', '目标', '背景', '，', '根据', '我校', '材料', '化学', '专业', '十一年', '来', '的', '实习', '实践', '教学', '经验', '，', '提出', '了', '当前', '实习', '实践', '教学', '存在', '的', '一些', '普遍性', '问题', '，', '并', '对', '其', '展开', '了', '分析', '与', '讨论', '。', '提出', '构建', '完整', '的', '实践', '教学', '体系', '，', '学校', '应', '建立', '稳固', '的', '实习', '实践', '基地', '，', '加强', '实习', '教学', '管理', '、', '教学', '改革', '以及', '加强', '对', '学生', '实践', '能力', '的', '培养', '。',
'以', 'SR', '、', '纳米','Fe3O4', '和', '纳米','MH','为', '主要原料', '制备','MH／Fe3O4／SR', '磁性', '橡胶', '复合材料', '。', '研究', '纳米', 'Fe3O4', '和', '纳米','MH', '不同', '配比', '时', '，', '复合材料', '的', '物理力学', '性能', '变化', '、', '耐热', '以及', '摩擦', '性能', '变化', '。', '结果', '表明', '：', '纳米粒子', '在','SR', '基体', '中', '分布', '较为', '均匀', '，', '不同', '配比', '的','Fe3O4／MH', '能够', '有效', '改善', '硅', '橡胶', '的', '物理力学', '性能', '。', '当', '配比', '20phrMH／10', 'phrFe3O4', '时', '，', '复合', '的', '拉伸', '强度', '、', '伸长率', '有所', '改善','。',
'本','试验','设计','了','一种','三明治型','的','C/C','刹车材料','的','预制体','结构','，','并','研究','这种','三明治','预制体结构','对','C/C','刹车材料','CVI','工艺','影响','。','结果','表明','，','相对','一般','针刺毡','结构','，','采用','三明治','预制体结构','制备','C/C','复合材料','时','，','增密速率','快','，','可','有效','消除','CVI','瓶颈效应','，','密度','分布','更加','均匀',';','且','可','一次性','致密','，','无需','中间','热处理','等','加工','步骤','，','有效','缩短','了','生产周期','，','降低','了','生产成本','。',
'采用','真空','热压','烧结','工艺','制备','了','SiC','颗粒','体积分数','分别','为','10％','、','20％','、','30％','和','40％','ZL101A','复合材料','，','对','其','硬度','与','室温','干','摩擦','磨损','性能','进行','了','测试','分析','，','同时','对','其','磨损','机理','进行','了','探讨','。','结果','发现','，','复合材料','硬度','随着','SiC','的','增加','而','增加','，','当','SiC','体积','分散','达到','30％','时','，','硬度','达到','最大值','。','基体','ZL101A','的','主要','磨损','机理','为','粘着磨损','，','而','SiCp/ZL101A','复合材料','的','磨损','过程','是','粘着磨损','和','磨粒磨损','两种','机制','共同','作用','的','结果']
# print(s1)

'''
1.jieba分词
'''
# l_jieba = jieba.lcut(s, cut_all=False)
# print("标准分割: ", s1)
# print('jieba分词：',l_jieba)
# for i in range(len(s1)):
#     #print(s1[i])
#     a = len(s1[i])
#     if s1[i] is not '\n':
#       print('0'*(a-1),'1',end='')
# print('****')
# for i in range(len(l_jieba)):
#     a = len(l_jieba[i])
#     if l_jieba[i] is not '\n':
#         print('0'*(a-1),'1',end='')

'''
2.thulac分词
'''
# print("标准分割: ", s1)
# thu = thulac.thulac(seg_only=True)
# s_thu = thu.cut(s,text=True)
# print(s_thu)
# #把字符串里的关键信息转换成列表
# l_thu = s_thu.split(' ')
#
# print("thulac分词：", l_thu)
#
# for i in range(len(s1)):
#     #print(s1[i])
#     a = len(s1[i])
#     if s1[i] is not '\n':
#       print('0'*(a-1),'1',end='')
# print('****')
# for i in range(len(l_thu)):
#     a = len(l_thu[i])
#     if l_thu[i] is not '\n':
#         print('0'*(a-1),'1',end='')
'''
3.pkuseg分词
'''
# seg = pkuseg.pkuseg()
# pkuseg = seg.cut(s)  # 进行分词
# # print("标准分割: ", s1)
# print('pkuseg分割:',pkuseg)
#
# for i in range(len(s1)):
#     #print(s1[i])
#     a = len(s1[i])
#     if s1[i] != '\n':
#       print('0'*(a-1),'1',end='')
# print('****')
# for i in range(len(pkuseg)):
#     a = len(pkuseg[i])
#     if pkuseg[i] != '\n':
#         print('0'*(a-1),'1',end='')

'''
4.snownlp分词
'''
# print("标准分割: ", s1)
# a = SnowNLP(s)
# snownlp_token = a.words
# print('snownlp分词：',snownlp_token)
# for i in range(len(s1)):
#     #print(s1[i])
#     a = len(s1[i])
#     if s1[i] != '\n':
#       print('0'*(a-1),'1',end='')
# print('****')
# for i in range(len(snownlp_token)):
#     a = len(snownlp_token[i])
#     if snownlp_token[i] != '\n':
#         print('0'*(a-1),'1',end='')

'''
5.pynlpir
'''
# print("标准分割: ", s1)
# pynlpir.open()
# pynlpir_token = pynlpir.segment(s,pos_tagging=False)
# print('pynlpir分词：',pynlpir_token)
# for i in range(len(s1)):
#     #print(s1[i])
#     a = len(s1[i])
#     if s1[i] != '\n':
#       print('0'*(a-1),'1',end='')
# print('****')
# for i in range(len(pynlpir_token)):
#     a = len(pynlpir_token[i])
#     if pynlpir_token[i] != '\n':
#         print('0'*(a-1),'1',end='')



'''
计算混淆矩阵(通用jieba、thulac、pkuseg、snownlp、pynlpir,只需替换当前使用的2分类文件即可)
'''
# f2 = open("jieba-分类.txt",encoding='UTF-8') # 只需替换这行文件
# ss = f2.readlines()
# biaozhun = list(ss[0])
# tokenize = list(ss[1])
#
# a = 0
# b = 0
# c = 0
# d = 0
# for i in range(len(biaozhun)-1):
#     if biaozhun[i] == '0':
#         if tokenize[i] == '0':
#             a = a + 1
#
# for i in range(len(biaozhun)-1):
#     if biaozhun[i] == '0':
#         if tokenize[i] == '1':
#             b = b + 1
#
# for i in range(len(biaozhun)-1):
#     if biaozhun[i] == '1':
#         if tokenize[i] == '0':
#             c = c + 1
#
# for i in range(len(biaozhun)-1):
#     if biaozhun[i] == '1':
#         if tokenize[i] == '1':
#             d = d + 1
#
# Accuracy = (d+a)/(a+b+c+d)
# Precision = d/(d+b)
# Recall = d/(d+c)
# F1_score = 2*Precision*Recall/(Precision+Recall)
#
# print('TP:',d)
# print('TN:',a)
# print('FN:',c)
# print('FP:',b)
# print('sum:',len(ss[1]))
# print('Accuracy:',Accuracy)
# print('Precision:',Precision)
# print('Recall:',Recall)
# print('F1_score:',F1_score)