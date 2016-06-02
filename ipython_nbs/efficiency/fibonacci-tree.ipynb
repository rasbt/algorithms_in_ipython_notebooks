{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sebastian Raschka \n",
      "last updated: 2016-06-01 \n",
      "\n",
      "CPython 3.5.1\n",
      "IPython 4.2.0\n"
     ]
    }
   ],
   "source": [
    "%load_ext watermark\n",
    "%watermark -a 'Sebastian Raschka' -u -d -v"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# Fibonacci Numbers"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A Fibonacci number F(n) is computed as the sum of the two numbers preceeding it in a Fibonacci sequence\n",
    "\n",
    "(0), 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...,\n",
    "\n",
    "for example, F(10) = 55.\n",
    "\n",
    "More formally, we can define a Fibonacci number F(n) as \n",
    "\n",
    "$F(n) = F(n-1) + F(n-2)$, for integers $n > 1$:\n",
    "\n",
    "$$F(n)=\n",
    "\\begin{cases} \n",
    "      0 & n=0, \\\\\n",
    "      1, & n=1, \\\\\n",
    "      F(n-1) + F(n-2), & n > 1.\n",
    "   \\end{cases}$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The Fibonacci sequence was named after Leanardo Fibonacci, who used the Fibonacci sequence to study rabit populations in the 12th century. I highly recommend reading the excellent articles on [Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number) and [Wolfram](http://mathworld.wolfram.com/FibonacciNumber.html), which discuss the interesting facts about the Fibonacci number in great detail."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The recursive Fibonacci number computation is a typical text book example of a recursive algorithm:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "55\n"
     ]
    }
   ],
   "source": [
    "def fibo_recurse(n):\n",
    "    if n <= 1:\n",
    "        return n\n",
    "    else:\n",
    "        return fibo_recurse(n-1) + fibo_recurse(n-2)\n",
    "    \n",
    "print(fibo_recurse(0))\n",
    "print(fibo_recurse(1))\n",
    "print(fibo_recurse(10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "However, it is unfortunately a terribly inefficient algorithm with an exponential running time of $O(2^n)$. The main problem why it is so slow is that we recompute Fibonacci number $F(n) = F(n-1) + F(n-2)$ repeatedly as shown in the recursive tree below:\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![Fibonacci Number Recursive Tree](../../images/efficiency/fibonacci_tree.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For example, assuming $n \\geq 2$ we have \n",
    "\n",
    "$O(2^{n-1}) + O(2^{n-2}) + O(1) = O(2^n)$\n",
    "\n",
    "for $F(n) = F(n-1) + F(n-2)$, where $O(1)$ is for adding to Fibonacci numbers together.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A more efficient approach to compute a Fibonacci number is a dynamic approach with linear runtime, $O(n)$:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "55\n"
     ]
    }
   ],
   "source": [
    "def fibo_dynamic(n):\n",
    "    f, f_minus_1 = 0, 1\n",
    "    for i in range(n):\n",
    "        f_minus_1, f = f, f + f_minus_1\n",
    "    return f\n",
    "\n",
    "print(fibo_dynamic(0))\n",
    "print(fibo_dynamic(1))\n",
    "print(fibo_dynamic(10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "(If you are interested in other approaches, I recommend you take a look at the pages on [Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number) and [Wolfram](http://mathworld.wolfram.com/FibonacciNumber.html).)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To get a rough idea of the running times of each of our implementations, let's use the `%timeit` magic for F(30)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 loops, best of 3: 499 ms per loop\n"
     ]
    }
   ],
   "source": [
    "%timeit -r 3 -n 10 fibo_recurse(n=30) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 loops, best of 3: 4.05 µs per loop\n"
     ]
    }
   ],
   "source": [
    "%timeit -r 3 -n 10 fibo_dynamic(n=30) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, let's benchmark our implementations for varying sizes of n:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import timeit\n",
    "\n",
    "funcs = ['fibo_recurse', 'fibo_dynamic']\n",
    "orders_n = list(range(0, 50, 10))\n",
    "times_n = {f:[] for f in funcs}\n",
    "\n",
    "for n in orders_n:\n",
    "    for f in funcs:\n",
    "        times_n[f].append(min(timeit.Timer('%s(n)' % f, \n",
    "                'from __main__ import %s, n' % f)\n",
    "                    .repeat(repeat=3, number=5)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "def plot_timing():\n",
    "\n",
    "    labels = [('fibo_recurse', 'fibo_recurse'), \n",
    "              ('fibo_dynamic', 'fibo_dynamic')]\n",
    "\n",
    "    plt.rcParams.update({'font.size': 12})\n",
    "\n",
    "    fig = plt.figure(figsize=(10, 8))\n",
    "    for lb in labels:\n",
    "        plt.plot(orders_n, times_n[lb[0]], \n",
    "             alpha=0.5, label=lb[1], marker='o', lw=3)\n",
    "    plt.xlabel('sample size n')\n",
    "    plt.ylabel('time per computation in milliseconds [ms]')\n",
    "    plt.legend(loc=2)\n",
    "    plt.ylim([-1, 300])\n",
    "    plt.grid()\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\nG8cvfvELmjVrVn0Tw7PPPsu1114LwLHHHsu9997Lt7/9bXr27Ml9993HsmXL9jrJev3113nhhRc4\n7rjj2HfffVm4cCH/+te/uOiiiwC4/PLLmTZtGqeccgo///nP6d69OytWrOC5557jpJNO4rDDDqvz\n31tERGRPtm+HxYtrtgcNyszvagJXZLp27crFF1/M6aefzpo1azjyyCOZMmVK9fsnnHAC06ZN45Zb\nbuHGG2+kY8eOXH755dxwww31Ou65555L69atmTBhAjfffDONGjWiT58+nHrqqdWf+dWvfkWnTp24\n++67GTt2LG3btuWoo46qfv8///M/Wb58OWeddRaNGzfmhz/8IWeeeSaLk/7lhy1U3KZNG15//XXu\nuece1q9fT5cuXTjvvPP4+c9/DgRn9l5//XV++tOfctppp7Fx40a6dOnC8OHD2Xfffev19y5GDblP\nZU+USzjlEk65pGqomSxeDDt3BuPOnSFTF370MHuROtK/JxER2ZuZM+G994LxiBHBK1ni/5foYfYi\nUj8NuU9lT5RLOOUSTrmkaoiZ7NwZ3MBQJVP9b6AJnCRZsWJF9RIbyUtuVO2bMWNGrksUEREpGEuX\nQtUjy9u1g06dMvfbuoQq1SoqKlIeu5Wsc+fOOX/2aj7RvycREdmTJ5+Ed94JxkccAWFLodb1Eqpu\nYpBqpaWl9OnTJ9dliIiIFLzKSpg/v2Y7k5dPQZdQRaSWhtinEoVyCadcwimXVA0tk+XLYfPmYLzP\nPpD0AKOM0AROREREJMNqL94bsgpWvagHTqSO9O9JRETCuMNvfgMbNwbb3/8+JD2mfBdaRkREREQk\nD6xaVTN5a94cevbM/DE0gRORXTS0PpWolEs45RJOuaRqSJkkXz4dNAhKYphtaQJXYK677jq6dOlC\naWkpvXv3ZsCAAdXvjR8/nv79+2e9phdffJGSkpKUB9Hns5KSEv7whz/kugwRESky7jBvXs12pu8+\nraJlRArIm2++yYQJE3jyySf52te+RosWLdhWtUJgQtizQrMhV8etq48//piysrJcl5GXGurzCvdG\nuYRTLuGUS6qGksknn8BnnwXjJk0grtW5NIErIAsXLqS0tJSTTjqpep8W1q2bTplcDltERCQh+fLp\ngAHQKKaZli6hJlm/fj3Tn5jOXTPuYvoT01m/fn3e/OYFF1zA+eefT2VlJSUlJZSWlu72kumMGTPo\n27cvzZs357jjjkt5usKDDz7IkCFDaNq0Kd27d+f666+nsrIyci1333033bt3p2XLlpxwwgksX768\n+r1NmzbRunVrHn300V2+U15eTmlpKa+++ioAvXv35sYbb+QnP/kJ7du3p0uXLowdO3aXOp5//nlG\njhxJ+/btKSsrY8SIEbz11lu7/G5JSQmTJk3irLPOolWrVvTs2ZOZM2eyceNGzj33XFq3bk3fvn35\n85//nPK95EuoX375JT/5yU/o0aMHzZo1o0+fPtxyyy2RMykmDalPJR3KJZxyCadcUjWUTGovHxIX\nTeAS1q9fz62P3cqCFgvYsO8GFrRYwK2P3VqvSVwmf3PixIncddddlJaWsmbNGlavXg2kXrpctWoV\n9957L48//jivvPIKGzdu5LTTTqt+/+mnn2bMmDF8//vfZ+7cudx5551MnjyZ8ePHR6rjiSeeYOzY\nsVx11VXMmTOHM888k6uvvrr6/VatWnH22WczZcqUXb43depU9t9/f4444ojqfZMmTaJr1668+eab\nTJo0iUmTJvHggw9Wv79p0yZ+9KMf8cYbb/D6668zYMAAjj/++JT8br75Zk466ST+9a9/cfLJJ3Pe\neefxve99j+OOO47Zs2czatQozj///D3mPmrUKJ566ikmT57M/PnzmT59us7SiYhIWj77DNasCcaN\nGkG/fvEdS+vAJUx/YjoLWizg5Y9ert5XubOS9uvaM/SwoXWqZc7/zeHTDp9S0qhmnjy823AGbh7I\nud86N+3fe/DBB7nooovYvn07ENy08Mgjj7Bw4cLq7V/+8pcsXryY3okFZxYtWsTAgQN54YUXGDly\nJEcddRTdunXb5cH0EydO5LrrruPzzz+n0V7O9Q4fPpxevXrx8MMPV++7+uqrufPOO1mxYgVdu3bl\n3Xff5dBDD2XhwoX07duXyspKevbsydVXX80VV1wBBGfghg4dyl//+tfq3znxxBNp27YtjzzySOix\nKysr6dChA5MnT+Z73/seEJxJu/LKK7njjjsAWLduHZ06deKKK67grrvuAmDDhg20a9eOp556ihNP\nPLH6e9OnT+fss8/mhRde4LjjjuPtt9/moIMOivifhtaBExGRXb36Kvzv/wbjgQMh8f+q9kjrwNXT\nus3rKG1cusu+kkYlbNmxpc6/uWXHll0mbwCljUtZt3ldnX9zbzp27Fg9eQPo378/HTp0YO7cuQDM\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x10ca86908>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plot_timing()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
