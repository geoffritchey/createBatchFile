
Create a batch file for executing a python script from taskscheduler.  All paths are absolute.   Copy main.py to createBatch.py and move to a target directory.  In that target directory run 
	
		python createBatch.py main.py >run.bat

to create the batch file to run main.py.  Then in task scheduler set up a task to run 'run.bat' from that target directory.

