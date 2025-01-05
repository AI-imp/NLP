import utils
import FMM
import RMM
import time
sentence = utils.get_sentences('cbfc_test.txt')
# 只有一句
sentence = sentence[0]


t_start=time.perf_counter()
t_fmm1=time.perf_counter()
f_seg=FMM.FMM(sentence)
t_fmm2=time.perf_counter()
T_fmm=t_fmm2-t_fmm1

t_rmm1=time.perf_counter()
r_seg=RMM.RMM(sentence)
t_rmm2=time.perf_counter()
T_rmm=t_rmm2-t_rmm1

fsig_num=0
rsig_num=0
if f_seg==r_seg:
    bm_seg =f_seg
else:
    for i in f_seg:
        if len(i)==1:
            fsig_num+=1
    for i in r_seg:
        if len(i)==1:
            rsig_num+=1
    if fsig_num<rsig_num:
        bm_seg = f_seg
    if fsig_num>rsig_num:
        bm_seg=r_seg
    if fsig_num==rsig_num:
        bm_seg = f_seg
T_end=time.perf_counter()
T_bm=T_end-t_start

def acc(seg):
    corr_num=0
    dict_words = utils.get_result_splited('cbfc_test_gold.txt.txt')[0]
    for i in range(len(seg)-1):
        if seg[i] in dict_words:
            corr_num+=1
    return corr_num

v1=len(f_seg)/T_fmm
v2=len(r_seg)/T_rmm
v3=len(bm_seg)/T_bm
corr_fmm=acc(f_seg)
corr_rmm=acc(r_seg)
corr_bm=acc(bm_seg)
print('v_fmm=',v1,'词/秒')
print('v_rmm=',v2,'词/秒')
print('v_bm=',v3,'词/秒')
print('fmm对的词数为',corr_fmm)
print('rmm对的词数为',corr_rmm)
print('bm对的词数为',corr_bm)




