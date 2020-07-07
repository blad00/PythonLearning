import sys
import os
#import shutil
from bioblend.galaxy import GalaxyInstance
from bioblend.galaxy.histories import HistoryClient
from bioblend.galaxy.tools import ToolClient
from bioblend.galaxy.workflows import WorkflowClient
from bioblend.galaxy.libraries import LibraryClient
from bioblend.galaxy.datasets import DatasetClient 
from bioblend.galaxy.jobs import JobsClient    #import jobsclient

GALAXY_URL = 'https://galaxy.psb.ugent.be'
API_KEY='30de163cef92bc75fab5f74731979b12'

#dir_name=sys.argv[1]   #output dir (to download files)
name_filter=sys.argv[1]   # CountSecondary, or SortedPosBam , etc.
#ext=sys.argv[3]     #bam tab sam , etc

def main():
        galaxyInstance = GalaxyInstance(url = GALAXY_URL, key=API_KEY)
        toolClient = ToolClient(galaxyInstance)
        historyClient = HistoryClient(galaxyInstance)
	workflowsClient= WorkflowClient(galaxyInstance)
	libraryClient=LibraryClient(galaxyInstance)
        datasetClient=DatasetClient(galaxyInstance)
        jobsClient=JobsClient(galaxyInstance)  ## create client
        histories = historyClient.get_histories(deleted=False)
        for hist in histories:
                hist_id=hist['id']
		countSecondary=historyClient.show_matching_datasets(hist_id, name_filter=name_filter)
                if len(countSecondary)!=0:
			#print(countSecondary)
                	#file_path=dir_name + '/'+hist['name'] +'_'+ name_filter +'.'+ext
                	#print(file_path)
                        #print(countSecondary[0]['dataset_id'])
 			#datasetClient.download_dataset(countSecondary[0]['id'], file_path=file_path, use_default_filename=False)
                        job_id=countSecondary[0]['creating_job']
                        jobs = jobsClient.show_job(job_id, full_details=True)
                        print(hist['name'])
                        print(jobs['stderr'])
        sys.exit()


if __name__ == '__main__':
    main()
