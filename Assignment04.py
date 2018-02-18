
# Import packages 

try: 
    import numpy as np
except ImportError:
    print("Could not import numpy") 

try:
    import logging 
except ImportError:
    print("Could not import logging")

try:
    import sphinx
except ImportError:
    print("Could not import sphinx")

logging.basicConfig(filename="OuroborosAssignment06log.txt", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


# Create Class
class Number_Calc:
    """This is a Number_Calc class.

    Attributes: sum of list, max min values of list, and max difference in list

    """
    def __init__(self, My_List = [None]):
        self.My_List = My_List #save the list as an attribute
        self.Sum = None
        self.Max_Min = None
        self.Max_Difference = None 

        self.Sum_Method()
        self.Max_Min_Method()
        self.Max_Difference_Method()

    def Sum_Method(self):   #Module Function 1
        """Function add all the numbers in the list

        :param my_list: list containing real numbers to be summed
        :raises: TypeError if list cannot be summed
        :raises: ValueError if no elements in given list
        :returns: sum of all elements in the list

        """
        logging.info("Calculating sum")
        try:
            np.sum(self.My_List)
        except TypeError:
            print('Input list should be numbers')        
            logging.debug('Given list does not contain summable elements')
        if len(self.My_List) == 0:
            raise ValueError('No elements in list to be summed')
            logging.warning('No elements present to be summed')
        sum = 0
        for elem in self.My_List:
            sum += elem
        logging.info('Elements have been summed')
        self.Sum = sum

    def Max_Min_Method(self):   #Module Function 2
        """ Function returns the max and min value of the input list

        :param my_list: a list of numbers
        :returns max_min: the max and min values in the list of numbers
        :raises TypeError: can only input a list of numbers
        :raises ValueError: can not input an empty list

        """
        logging.info("Calculating max and min")
        if np.iscomplexobj(self.My_List) is True:
            logging.warning('There are imaginary numbers in your list')

        try:
            np.max(self.My_List)
        except TypeError:
            logging.debug('List is {}'.format(self.My_List))
            print("You did not input a list of numbers")
            self.Max_Min = None
        except ValueError:
            print("The input type is correct but inappropriate")
            self.Max_Min = None

        self.Max_Min = ((np.max(self.My_List), np.min(self.My_List)))
	
    def Max_Difference_Method(self):  #Module Function 3

        """Function will return maximum difference between adjacent numbers.

        Function takes in the inputted list of values, splits it into two arrays to calculate the difference between
        adjacent values, takes the absolute values of the differences to disregard positioning, and then outputs the
        maximum value.

        :param input_list: List of numbers
        :return: Maximum difference
        :raises ImportError: Check if numpy is installed or virtual env is established
        :raises TypeError: Input not given as a list of values
        :raises ValueError: Can occur when only 1 number is given in the list
        """
       
        logging.info("Calculating max difference")

        try:
            if any(self.My_List) < 0:  #included to use warning
                logging.warning('Negative values in list')
                logging.debug('Values {}'.format(self.My_List))
            input_list = np.array(self.My_List)
            diffs = abs(np.diff(self.My_List))
            max_val = max(diffs)

            self.Max_Difference = max_val

        except ImportError:  # redundancy
            logging.debug('Values {}'.format(self.My_List))
            logging.error('ImportError: Check if numpy is in virtualenv')
        except TypeError:
            logging.debug('Values {}'.format(self.My_List))
            logging.debug(self.My_List)
            logging.error('TypeError: Check if input is a list of values')
        except ValueError:
            logging.debug('Values {}'.format(self.My_List))
            logging.error('ValueError: Add more numbers to the list')


