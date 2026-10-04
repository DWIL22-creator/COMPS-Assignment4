"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    duplicates = []
    the_ids = []
    for id in product_ids:
        if id in the_ids:
            duplicates.append(id)
        else:
            the_ids.add(id) #We're adding it because, we've checked to seen it already.
    if len(duplicates) != 0:
        print(True)
    else: 
        print(False)

#I believed lists fit this task because we're iterating through items in our lists to perform comparisons and accessing values by position.
#I use the list, product ids and create two lists within the function called duplicates, where the duplicate ids get added once they're compared to the count and a list called the_ids adds id's from product_ids, if we've already checked them in the lsit.
#So for the id in product_ids, if the id is already in the_ids (meaning we checked this index), then we add the id to our duplicate list. Otherwise, the id gets added to the_ids because we've already checked for it. In the end, we check if duplicates is not empty, comfirming that there were duplicates found in the list.


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.front:
            self.front = new_node
            self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node
        

    def remove_oldest_task(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node
        

#I knew that a queue was the best solution for this problem, because we are keeping track of order and removing tasks from the front of the queue.
#For the add_task I create a node to add the task, which is assigned to become the front of the empty node and the rear, because there's only one value.
#For removing the oldest node, I set the removed_node to the front and then front becomes the next value in the node, returning the removed value.



"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.stream = set()

    def add(self, value):
        if value in self.stream:
            return None
        else:
            self.stream.add(value)

    def get_unique_count(self):
        return len(self.stream)

#I thought a set was most ideal for this problem because  we're chcking if a value is present quickly, values are being added to a collection, and we just want to count how many total values are in the set.
#I create a set called stream. If the added value is already in the stream, return nothing. Otherwise, add the value to the stream.
#Next for the unique count, I get the length of the stream to determine the number of unique values.