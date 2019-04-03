

d_2 = {'rb1':(1,1), 'hb1':(1,2), 'bb1':(1,3), 'qb':(1,4), 'kb':(1,5), 'bb2':(1,6), 'hb2':(1,7), 'rb2':(1,8), 'pb1':(2,1), 'pb2':(2,2), 'pb3':(2,3), 'pb4':(2,4), 'pb5':(2,5), 'pb6':(2,6), 'pb7':(2,7), 'pb8':(2,8)}





###############  WORKING CODE####################
# centroid_1 = centroid
# d_1 = {}
# for i in range(8):
#     for j in range(8):
#         d_1[centroid_1[i*8 + j]] = (i,j) 
# # print 'centroid[3] =',d_1[(210,42)]
# # print 'd_1 =',d_1
# print len(d_1)

# def wat_is_moved(change):
#     global d_2
#     global d_1
#     for i,v in d_2.iteritems():
#         # print 'v =',v
#         if(d_1[change] == d_2[i]):
#             print 'the piece moved is',i

# a = d_2['bb1']
# print type(a)
# print '',a


####################################  ALTERNATIVE ###########################
# # def convert(a,divider):
# # 	b = []
# # 	val = len(a)/divider
# # 	if(len(a)%divider != 0):
# # 		print("WRONG FORMAT")
# # 		return None
# # 	for i in range(val):
# # 		b.append([])
# # 		for j in range(divider):
# # 			n = divider*i+j
# # 			# print("i = "+str(i)+"\tj = "+str(j)+"\tn ="+str(n))
# # 			b[-1].append(a[n])
# # 	return b



####################################  NOT WORKING ###########################

# d = {11:(71.0, 34.5), 12:(123.0, 34.5), 13:(174.5, 34.5), 14:(226.0, 34.5), 15:(277.0, 34.5), 16:(327.5, 34.5), 17:(378.0, 34.5), 18:(428.5, 34.5), 21:(71.0, 80)}
# print d[11]
# d [11] = (71.0, 45.0)
# print d[11], d[12]
# piece = {'r':d[11]}
# print piece['r']
# piece['r'] = d[12]
# print piece['r']
# print d[(71.0, 34.5)]

