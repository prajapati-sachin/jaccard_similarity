There are two makefiles in the folder:-
	1) Makefile.generate_dataset which prepares a test.tsv file in the data folder.
	2) Makefile.run_classifier which uses the test.tsv file and computes jaccard similarity for every pair present in the file and also compute the performance metrics.


Instructions to run the code:-

	make -f Makefile.generate_dataset  

	make -f Makefile.run_classifier