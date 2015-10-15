# CS4341 Final Project
Course assignments in CS4341 at WPI.

### Work Split
    Nicholas Bradford:  framework, NN
    Thomas Grimshaw:    SVM
    Lucas Lebrao:       SVM
    Tim Petri:          Naive Bayes

### Testing Instructions

For NN:

    $ python runner.py -n 1

For SVM:

    $ python runner.py -n 2

For Naive Bayes:

    $ python runner.py -n 3

Detailed Usage: 

    runner.py   [-h] 
                [-n {1,2,3}] 
                [-t {0,1,2,3,4,5,6,7,8,9,10,11,12,13}]
                [-b {0,1,2,3,4,5,6,7,8,9,10,11,12,13}] 
                [-e EPOCHS]
                [-z]

    optional arguments:
      -h, --help            show this help message and exit
      -n {1,2,3}, --strategy_num {1,2,3}
      -t {0,1,2,3,4,5,6,7,8,9,10,11,12,13}, --training_time {0,1,2,3,4,5,6,7,8,9,10,11,12,13}
      -b {0,1,2,3,4,5,6,7,8,9,10,11,12,13}, --backtest_time {0,1,2,3,4,5,6,7,8,9,10,11,12,13}
      -e EPOCHS, --epochs EPOCHS
      -z, --normalize       Turn normalization off.

### Dependencies

* NumPy, SciPy, scikit-learn (use Anaconda): http://docs.continuum.io/anaconda/install
* Lasagne (requires Theano): http://lasagne.readthedocs.org/en/latest/user/installation.html
* Quantopian Zipline (backtesting): https://github.com/quantopian/zipline

Verify Quantopian Zipline framework:

    ./backtest $ run_algo.py -f movingAverages.py --start 2000-1-1 --end 2014-1-1 --symbols AAPL -o movingAverages_out.pickle
    ./backtest $ python readfile.py

EOF
