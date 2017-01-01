import pandas as pd
from sklearn.metrics import silhouette_samples, silhouette_score
from bayespy.nodes import Categorical, Dirichlet
from bayespy.nodes import Beta


def prep_data(dat):
	#process data into binary matrix
	#input parameter pandas read_csv object
	row_lvls = pd.unique(dat.iloc[:,0].values.ravel())
	row_lvls.sort()
	col_lvls = pd.unique(dat.iloc[:,1].values.ravel())
	col_lvls.sort()
	mat = pd.DataFrame(0,index=row_lvls, columns=col_lvls)
	mat = mat.fillna(0)

	for i in range(dat.shape[0]):
		mat.loc[dat.iloc[i,0],dat.iloc[i,1]] = 1

	return mat

#bernoulli mixture model
def bmm(mat, K):
	######### BMM ################

	R = Dirichlet(K*[1e-5], name='R'+str(K))
	Z = Categorical(R, plates=(N,1), name='Z'+str(K))


	P = Beta([0.5, 0.5], plates=(D,K), name='P'+str(K))

	from bayespy.nodes import Mixture, Bernoulli
	X = Mixture(Z, Bernoulli, P)

	from bayespy.inference import VB
	Q = VB(Z, R, X, P)

	P.initialize_from_random()
	#mat.as_matrix().astype(int)
	X.observe(mat)

	Q.update(repeat=1000)

	result = [R, Z, P, Q]
	return result

def save_bmm(res):
	####### save objects ##########
	Rdf = pd.DataFrame(res[0].random())
	Zdf = pd.DataFrame(res[1].random())
	Pdf = pd.DataFrame(res[2].random())
	K = Rdf.size
	Rdf.to_csv("file"+R.name+str(K)+".csv")
	Zdf.to_csv("file"+Z.name+str(K)+".csv")
	Pdf.to_csv("file"+P.name+str(K)+"+.csv")

	bayes = [Rdf, Zdf, Pdf]

	return bayes

def siljac(dat, Zdf):
	### silhouette score ######
	return silhouette_score(numpy.asmatrix(dat), numpy.reshape(Zdf.values, Zdf.shape[0]), metric='jaccard')

####### bmm plots #############
def graph_results():
	import bayespy.plot as bpplt

	bpplt.hinton(R)

	bpplt.hinton(P)

	bpplt.hinton(Z)

	bpplt.pyplot.show()
