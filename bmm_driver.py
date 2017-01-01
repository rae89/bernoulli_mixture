############# load data ###################
def load_data():
	#read user to single card reader data
	dat = pd.read_csv("PATH%\\cards_to_reader_grps.csv")
	groups = prep_data(dat)

	#read user to department data
	dat2 = pd.read_csv('PATH%\\depts.csv')
	depts = prep_data(dat2)

	############# join data ###################
	mat = groups.join(depts, how='left')
	mat = mat.fillna(0)

	#returning binary matrix with rows representing users and columns representing
	# categories of readerIDs and departmentIDs
	return mat

####### run iteration parameter initaliztion ###############
kits = 3
subits = 2
scalar = 100
scores = driver(mat, kits, subits, scalar)

############ multiprocessesing ################
def multiproc():
	import multiprocessing as mp
	m = mat.as_matrix().astype(int)
	kits = 3
	subits = 2
	scalar = 100
	runs = iterations(kits, subits, scalar)
	pool = mp.Pool(processes=2)

	results = pool.map(driver, (m, runs))
	pool.close() # No more work

	# tasks progress report
	while (True):
	  if (results.ready()): break
	  remaining = results._number_left
	  print ("Waiting for"+ remaining+ "tasks to complete...")
	  time.sleep(0.5)

	dicresults = dict(results)
	return dicresults

#multiple iteration run
def run(mat, kits, subits, scalar):
	N = mat.shape[0]
	D = mat.shape[1]
	#### run four iteration for each K and increment K by 100 after the four itts #####
	res = {}
	tots = subits*kits
	for i in range(1,kits):
		K = scalar*i
		for j in range(1,subits):
			res['res'+str(K)+'{0}'.format(j)] = bmm(K)
			#print ('Completed iteration: '+str(j*i)+' Out of: '+str(tots) )

	#scores = {}
	#for key, value in res.items():
	#	bayes = save_bmm(res[key])
	#	Zdf = bayes[1]
	#	scores[key] = siljac(mat, Zdf)

	#max_score = scores[max(scores, key=scores.get)]

	#print (str(max(scores, key=scores.get))+' : '+str(max_score))
	return res#scores, res

"""
################# iterations list ##########################
def iterations(kits, subits, scalar):
	#### run four iteration for each K and increment K by 100 after the four itts #####
	runs = []
	for i in range(1,kits+1):
		K = scalar*i
		for j in range(1,subits+1):
			runs.append(('res'+str(K)+str(j), K))
	return runs
############################################
"""
#single iteration run
def run(m, runs):
	N = m.shape[0]
	D = m.shape[1]
	result = bmm(m, runs[1])
	return (runs[0], result)
