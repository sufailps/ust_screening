class CircularQueue:
    def __init__(self, max_size):
        self.queue = {}
        self.max_size = max_size
        self.first = 0
        self.current_size = 0

    def enqueue(self, item):
        if self.current_size == self.max_size:
            # Remove the latest added item
            latest_index = self.first + self.current_size - 1
            print(f"Queue is full. Removing item: {self.queue[latest_index]}")
            del self.queue[latest_index]  # Remove the latest added item
            self.current_size -= 1  # Decrease the size after removal

        # Calculate the new rear index
        rear = self.first + self.current_size  # Simple index calculation
        self.queue[rear] = item  # Add the new item
        self.current_size += 1
        print(f"Adding item: {item} at position {rear}")


    def display(self):
        print("Queue contents:")
        for i in range(self.first, self.first + self.current_size):
            if i in self.queue:
                print(f"Index {i}: {self.queue[i]}")


# Create a CircularQueue object
queue = CircularQueue(5)

entries = [1, 2, 3, 4, 5, 6]

for i in entries:
    queue.enqueue(i)

queue.display()
