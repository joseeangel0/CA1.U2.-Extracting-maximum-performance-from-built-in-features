import multiprocessing as mp
 
POISON_PILL=None

class ReductionConsumer (mp.Process):
    def __init__(self,task_queue,result_queue):
        super().__init__()
        self.task_queue=task_queue
        self.result_queue=result_queue
    
    def run(self):
        pname = self.name
        print("Using {pname}...")
        while True:
            num1 = self.task_queue.get()

            if num1 == POISON_PILL:
                print(f"Exiting process {pname}...")
                self.task_queue.task_done()
                break
            
            self.task_queue.task_done()
            num2 = self.task_queue.get()
            
            if num2 is POISON_PILL:
                print(f"Reaching the end with process {pname} and number {num1}")
                self.task_queue.task_done()
                self.result_queue.put(num1)

            print(f"Running process {pname} on numbers {num1} and {num2}")
            self.task_queue.task_done()
            self.result_queue.put(num1+num2)

    
def reduce_sum (array, n_consumers = None):
    ctx = mp.get_context("spawn")
    if n_consumers is None: 
     n_consumers = mp.cpu_count()
        
    results = ctx.JoinableQueue()
    result_size = len(array)
        
    for item in array:
        results.put(item)
        
    while result_size > 1:
        task = results
        results = ctx.JoinableQueue()
    
        consumers = [ReductionConsumer(task, results) for _ in range(n_consumers)]
        for c in consumers:
            c.start()
        for _ in range(n_consumers):
            task.put(POISON_PILL)
        task.join()
        
        for c in consumers:
            c.join()
            
        result_size = result_size//2 + (result_size%2)
    return results.get()

if __name__ == "__main__":
    my_array = [ i for i in range(20)]
    result = reduce_sum(my_array)
    print(f"Final result : {result}")
               