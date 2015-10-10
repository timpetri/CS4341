# CS4341 Final Project
Course assignments in CS4341 at WPI.

### Work Split
	Nicholas Bradford:	
	Thomas Grimshaw:	
	Lucas Lebrao:		
	Tim Petri:			

### Testing Instructions

Test Quantopian Zipline framework:

	./backtest $ run_algo.py -f movingAverages.py --start 2000-1-1 --end 2014-1-1 --symbols AAPL -o movingAverages_out.pickle
	./backtest $ python readfile.py

Test neural nets are installed (and see my currently broken neural network test):

	$ python test_nick.py

### Dependencies

* NumPy, SciPy, scikit-learn (use Anaconda): http://docs.continuum.io/anaconda/install
* Lasagne (requires Theano): http://lasagne.readthedocs.org/en/latest/user/installation.html
* Quantopian Zipline (backtesting): https://github.com/quantopian/zipline
* Pylearn2 (SVM and NN): http://deeplearning.net/software/pylearn2/

### Results
	TODO.