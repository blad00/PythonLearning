import sys
import os
#import shutil
from bioblend.galaxy import GalaxyInstance
from bioblend.galaxy.histories import HistoryClient
from bioblend.galaxy.tools import ToolClient
from bioblend.galaxy.workflows import WorkflowClient
from bioblend.galaxy.libraries import LibraryClient
#from bioblend.galaxy.datasets import DatasetClient


#GALAXY_URL = 'https://192.168.66.13'
GALAXY_URL = 'https://galaxy.psb.ugent.be'
#API_KEY = '978218cdf5e6d829d4cd4c0c5d0e3c40'
API_KEY='30de163cef92bc75fab5f74731979b12'

#param 1=dir name to iterate
#dir_name=sys.argv[1]


def main():
	galaxyInstance = GalaxyInstance(url = GALAXY_URL, key=API_KEY)
	toolClient = ToolClient(galaxyInstance)
	histories = HistoryClient(galaxyInstance)
	workflowsClient= WorkflowClient(galaxyInstance)
	libraryClient=LibraryClient(galaxyInstance)

	brassica_library = libraryClient.get_libraries(name = ' Evolutionary Systems Biology')
	files = libraryClient.show_library(brassica_library[0]['id'], contents=True)
	#print(files)
	itemp = 0
	for f in files:
		if f['type'] == 'folder':
			continue # do nothing, try next
		#initial set
		#if itemp == 31:
		#	break

		#print ("Name " + f['name'])

		replicate=f['name'].split('_')[-1].split('.')[0]
		#print replicate
		if replicate == '1':
			itemp = itemp+1
			if not (itemp >= 71 and itemp <= 92):
				continue
			base=f['name'].split('_')[:-1]
			#print base
			forward_name=f['name']
			reverse_name='_'.join(base) + '_2.fastq.bz2'
			forward_id= f['id']
			files2 = libraryClient.show_library(brassica_library[0]['id'], contents=True)
			for f2 in files2:
				if f2['name'] == reverse_name:
					reverse_id=f2['id']
			print forward_name
			print reverse_name
			new_history_name=f['name'].split('_')[7]+"_"+f['name'].split('_')[-3]+"_"+f['name'].split('_')[-2]
			print new_history_name
			hist = histories.create_history(name=new_history_name)
			dataset_F = histories.upload_dataset_from_library(hist['id'], forward_id)
			dataset_R = histories.upload_dataset_from_library(hist['id'], reverse_id)
			datamap = {}
			datamap['0'] = { 'src':'hda', 'id':dataset_F['id'] }
			datamap['1'] = { 'src':'hda', 'id':dataset_R['id'] }
			workflows = workflowsClient.get_workflows(name = "Maize HISAT 2.1")
			workflow = workflows[0]
			try:
				w = workflowsClient.run_workflow(workflow['id'], datamap, history_id=hist['id'])
			except:
				print('Next')
		#workflowClient.show_workflow(workflow['id'])
		#sys.exit()
#sys.exit()
#	brassica_lib= libraryClient.get_libraries(name='Brassica', deleted=False)
#        print(brassica_lib)
#        brassica_datasets=libraryClient.show_dataset(brassica_lib[0]['id'])
#        print(brassica_datasets)
#        sys.exit()



if __name__ == '__main__':
	main()
