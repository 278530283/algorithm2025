#单位时间任务
class Task:
    def __init__(self, task_id: int, t: int, p: int=0, count: int = 0):
        self.id = task_id
        self.t = t
        self.p = p
        self.count = count

    def __repr__(self):
        return f"Task(id={self.id}, t={self.t}, p={self.p}, count={self.count})"

#链表节点
class ListNode:
    def __init__(self, task: Task):
        self.task = task
        self.next = None

#已调度任务列表
class TaskList:
    def __init__(self):
        self.head = None

    def insert_task(self, x: Task) -> bool:
        """
        尝试将任务 x 插入到链表中适当位置，保持独立子集的条件
        返回是否插入成功
        """
        # Step 1: 找到所有满足 a[i].t >= x.t 的节点，并检查是否都未满
        traversal_nodes = []  # 记录所有需要遍历的节点
        dummy = ListNode(Task(-1, float('inf')))  # 虚拟头节点，便于插入
        dummy.next = self.head
        dummy.task.count = self.head.task.count + 1 if self.head else 1

        prev = dummy
        curr = dummy.next

        while curr and curr.task.t >= x.t:
            traversal_nodes.append(curr)
            if curr.task.count >= curr.task.t:
                return False
            prev = curr
            curr = curr.next

        # Step 2: 插入任务 x 到最后一个满足条件的节点之后
        x.count = prev.task.count
        new_node = ListNode(x)
        new_node.next = prev.next
        prev.next = new_node

        # Step 3: 更新前面任务的 count（满足 a[i].t >= x.t 的）
        for node in traversal_nodes:
            node.task.count += 1

        # Step 4: 更新链表头
        self.head = dummy.next
        return True

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.task)
            curr = curr.next

# 按权重快速排序
def quick_sort_tasks(task_list):
    if len(task_list) <= 1:
        return task_list
    else:
        # 选择第一个任务作为基准
        pivot = task_list[0]
        # 小于基准的任务组成的子数组
        left = [task for task in task_list[1:] if task.p >= pivot.p]
        # 大于基准的任务组成的子数组
        right = [task for task in task_list[1:] if task.p < pivot.p]
        # 递归排序左右子数组，并合并结果
        return quick_sort_tasks(left) + [pivot] + quick_sort_tasks(right)

# 对单位时间任务列表进行调度安排，使用贪心算法实现
def greedy_task_scheduling(tasks):
    # 误时惩罚任务列表
    timeout_tasks = []
    print("原始任务列表:")
    for task in tasks:
        print(task)
    # 快速排序
    sorted_tasks = quick_sort_tasks(tasks)
    print("按惩罚权重降序排序后的任务列表:")
    for task in sorted_tasks:
        print(task)
    print("使用贪心算法进行调度安排")
    # 初始化链表任务集合
    task_list = TaskList()
    for x in sorted_tasks:
        print(f"\n准备调度任务id:{x.id},截止时间:{x.t},惩罚权重:{x.p}")
        # 检查任务子集的独立性
        if task_list.insert_task(x):
            print("对于该任务，插入后已调度子集满足独立性（可以及时完成），将其插入已调度列表中。")
            print("插入后的已调度任务列表：")
            task_list.print_list()
        else:
            print("任务插入后不能满足任务子集独立性，将其插入到超时惩罚列表中。")
            timeout_tasks.append(x)
    penalty_weight_sum = sum(task.p for task in timeout_tasks)
    print(f"\n调度结束后，误时惩罚任务列表是：")
    for task in timeout_tasks:
        print(task)
    print(f"最小的惩罚权重之和为{penalty_weight_sum}")

#主函数
if __name__ == "__main__":
    # 原始任务列表
    tasks = [
        Task(1, 3, 13),
        Task(2, 7, 12),
        Task(3, 1, 11),
        Task(4, 3, 10),
        Task(5, 2, 9),
        Task(6, 6, 8),
        Task(7, 4, 14),
        Task(8, 5, 15)
    ]
    greedy_task_scheduling(tasks)
