
import numpy as np



genome = raw_input('Genome : ')
Expected_size = raw_input('Expected size : ')


#genome = 'Het_6.contigs.fasta'
#Expected_size = 40000000


fx = open(genome)
ct = fx.read().split('>')
fx.close()

Nb_sca = len(ct) -1  # number of scaffolds

Tots = 0 #Total size of scaffolds
Usef = 0 #Useful amount of scaffold sequences (>= 25K nt)
ls = []
One_k = 0 #Number of scaffolds > 1K nt
Ten_k = 0 #Number of scaffolds > 10K nt
Hund_k = 0 #Number of scaffolds > 100K nt
One_M_k = 0 #Number of scaffolds > 1M nt


full_seq = ''

m = 0
for x in ct[1:]:
    m = m + 1
    if m % 100 == 0:
        print m

    seq = x.split('\n',1)[1].replace('\n','').replace('\r','')
    full_seq = full_seq + seq
    lg = len(seq)
    Tots = Tots + lg
    if len(seq) >= 25000:
        Usef = Usef + lg
    ls.append(lg)
    if lg > 1000:
        One_k = One_k + 1
    if lg > 10000:
        Ten_k = Ten_k + 1
    if lg > 100000:
        Hund_k = Hund_k + 1
    if lg > 1000000:
        One_M_k = One_M_k + 1

half = float(Tots)/2
ls.sort()
ls.reverse()
m, i = 0, 0
while m <= half:

    m = m + ls[i]
    i = i + 1
N50 = ls[i]
L50 = i + 1


half = float(Expected_size)/2
m, i = 0, 0

while m <= half:
    m = m + ls[i]

    i = i + 1
NG50 = ls[i]
LG50 = i + 1

percA = float(full_seq.count('A')) / len(full_seq)
percC = float(full_seq.count('C')) / len(full_seq)
percG = float(full_seq.count('G')) / len(full_seq)
percT = float(full_seq.count('T')) / len(full_seq)
percN = float(full_seq.count('N')) / len(full_seq)



print 'Number of scaffolds'+ '\t' + str(Nb_sca)
print 'Total size of scaffolds'+ '\t' + str(Tots)
print 'Total scaffold length as percentage of assumed genome size'+ '\t' + str((float(Tots)/Expected_size)*100)
print 'Useful amount of scaffold sequences (>= 25K nt)'+ '\t' + str(Usef)
print '% of estimated genome that is useful'+ '\t' + str((float(Usef)/Tots)*100)
print 'Longest scaffold'+ '\t' + str(ls[0])
print 'Shortest scaffold'+ '\t' + str(ls[-1])
print 'Number of scaffolds > 1K nt'+ '\t' + str(One_k)
print 'Percentage of scaffolds > 1K nt'+ '\t' + str((float(One_k)/Nb_sca)*100)
print 'Number of scaffolds > 10K nt'+ '\t' + str(Ten_k)
print 'Percentage of scaffolds > 10K nt'+ '\t' + str((float(Ten_k)/Nb_sca)*100)
print 'Number of scaffolds > 100K nt'+ '\t' + str(Hund_k)
print 'Percentage of scaffolds > 100K nt'+ '\t' + str((float(Hund_k)/Nb_sca)*100)
print 'Number of scaffolds > 1M nt'+ '\t' + str(One_M_k)
print 'Percentage of scaffolds > 1M nt'+ '\t' + str((float(One_M_k)/Nb_sca)*100)
print 'Mean scaffold size'+ '\t' + str(np.mean(ls))
print 'Median scaffold size'+ '\t' + str(np.median(ls))
print 'N50 scaffold length'+ '\t' + str(N50)
print 'L50 scaffold count'+ '\t' + str(L50)
print 'NG50 scaffold length'+ '\t' + str(NG50)
print 'LG50 scaffold count'+ '\t' + str(LG50)

print 'scaffold %A'+ '\t' + str(percA)
print 'scaffold %C'+ '\t' + str(percC)
print 'scaffold %G'+ '\t' + str(percG)
print 'scaffold %T'+ '\t' + str(percT)
print 'scaffold %N'+ '\t' + str(percN)



