import tkinter as tk
from tkinter import messagebox
import heapq
import copy


class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.moves = [(-1, 0, "上"), (1, 0, "下"), (0, -1, "左"), (0, 1, "右")]

    # 可解性判断（初始状态到目标状态）
    def is_solvable(self):
        def count_inversions(state):
            """计算状态的逆序数（忽略空格0）"""
            flat = [num for row in state for num in row if num != 0]
            inversions = 0
            for i in range(len(flat)):
                for j in range(i + 1, len(flat)):
                    if flat[i] > flat[j]:
                        inversions += 1
            return inversions

        def find_empty_row(state):
            """找到空格所在的行数（0开始）"""
            for i in range(3):
                if 0 in state[i]:
                    return i
            return -1

        # 初始状态和目标状态的逆序数
        initial_inv = count_inversions(self.initial_state)
        goal_inv = count_inversions(self.goal_state)

        # 初始状态和目标状态的空格行数
        initial_empty_row = find_empty_row(self.initial_state)
        goal_empty_row = find_empty_row(self.goal_state)

        # 可解条件：初始和目标的（逆序数奇偶性 + 空格行数奇偶性）必须相同
        return (initial_inv % 2 == goal_inv % 2) and (initial_empty_row % 2 == goal_empty_row % 2)

    # 曼哈顿距离启发函数（适配自定义目标状态）
    def manhattan_distance(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                num = state[i][j]
                if num != 0:
                    # 查找数字在目标状态中的位置
                    for x in range(3):
                        for y in range(3):
                            if self.goal_state[x][y] == num:
                                distance += abs(i - x) + abs(j - y)
                                break
                    else:
                        continue  # 未找到则跳过（理论上不会发生）
                    break
        return distance

    # 查找空格位置
    def find_empty(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
        return -1, -1

    # A*算法求解
    def solve(self):
        if not self.is_solvable():
            return None, "从初始状态到目标状态无解"

        # 优先队列：(f值, g值, 当前状态, 路径)
        heap = []
        initial_g = 0
        initial_h = self.manhattan_distance(self.initial_state)
        heapq.heappush(heap, (initial_g + initial_h, initial_g, self.initial_state, []))

        # 已访问状态集合（避免重复搜索）
        visited = set()

        while heap:
            f, g, current, path = heapq.heappop(heap)

            # 到达目标状态
            if current == self.goal_state:
                return path, f"找到解！总步数：{len(path)}"

            # 标记当前状态为已访问
            state_tuple = tuple(tuple(row) for row in current)
            if state_tuple in visited:
                continue
            visited.add(state_tuple)

            # 生成所有可能的下一步状态
            empty_i, empty_j = self.find_empty(current)
            for di, dj, move_name in self.moves:
                ni, nj = empty_i + di, empty_j + dj  # 新空格位置
                if 0 <= ni < 3 and 0 <= nj < 3:  # 确保在棋盘内
                    # 复制当前状态并移动空格
                    new_state = copy.deepcopy(current)
                    new_state[empty_i][empty_j], new_state[ni][nj] = new_state[ni][nj], new_state[empty_i][empty_j]
                    new_state_tuple = tuple(tuple(row) for row in new_state)

                    # 未访问过的状态加入队列
                    if new_state_tuple not in visited:
                        new_g = g + 1
                        new_h = self.manhattan_distance(new_state)
                        new_path = path + [(new_state, move_name)]
                        heapq.heappush(heap, (new_g + new_h, new_g, new_state, new_path))

        return None, "搜索失败（未找到解）"


class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("八数码状态转换求解器")
        self.root.geometry("600x700")

        # 标题
        tk.Label(root, text="八数码状态转换", font=('Arial', 16, 'bold')).pack(pady=10)

        # 初始状态输入区
        tk.Label(root, text="初始状态", font=('Arial', 12)).pack(anchor=tk.W, padx=50)
        self.initial_frame = tk.Frame(root)
        self.initial_frame.pack(pady=5)
        self.initial_cells = self.create_cell_grid(self.initial_frame)

        # 目标状态输入区
        tk.Label(root, text="目标状态", font=('Arial', 12)).pack(anchor=tk.W, padx=50)
        self.goal_frame = tk.Frame(root)
        self.goal_frame.pack(pady=5)
        self.goal_cells = self.create_cell_grid(self.goal_frame)

        # 预设示例（可解的状态对）
        self.set_example_states()

        # 求解按钮
        self.solve_btn = tk.Button(root, text="求解转换步骤", command=self.solve_puzzle, font=('Arial', 14))
        self.solve_btn.pack(pady=15)

        # 结果展示区
        self.status_label = tk.Label(root, text="", font=('Arial', 12))
        self.status_label.pack(pady=5)

        self.step_label = tk.Label(root, text="步骤：", font=('Arial', 12))
        self.step_label.pack(pady=5)

        self.path_text = tk.Text(root, height=6, width=60, font=('Arial', 10))
        self.path_text.pack(pady=5)

        # 步骤导航按钮
        self.nav_frame = tk.Frame(root)
        self.nav_frame.pack(pady=10)

        self.prev_btn = tk.Button(self.nav_frame, text="上一步", command=self.prev_step, width=10)
        self.prev_btn.pack(side=tk.LEFT, padx=10)

        self.next_btn = tk.Button(self.nav_frame, text="下一步", command=self.next_step, width=10)
        self.next_btn.pack(side=tk.LEFT, padx=10)

        # 求解路径存储
        self.solution_path = []
        self.current_step = 0

    def create_cell_grid(self, parent):
        """创建3x3的输入网格"""
        cells = []
        for i in range(3):
            row = []
            for j in range(3):
                cell = tk.Entry(parent, width=5, font=('Arial', 20), justify='center')
                cell.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell)
            cells.append(row)
        return cells

    def set_example_states(self):
        """预设一个可解的示例状态对"""
        # 初始状态示例
        # initial_example = [
        #     [2, 8, 3],
        #     [1, 0, 4],
        #     [7, 6, 5]
        # ]
        initial_example = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        # 目标状态示例
        goal_example = [
            [1, 2, 3],
            [8, 0, 4],
            [7, 6, 5]
        ]
        # 填充到输入框
        for i in range(3):
            for j in range(3):
                self.initial_cells[i][j].insert(0, str(initial_example[i][j]))
                self.goal_cells[i][j].insert(0, str(goal_example[i][j]))

    def get_state_from_grid(self, cells):
        """从输入网格获取状态（并验证合法性）"""
        try:
            state = []
            for i in range(3):
                row = []
                for j in range(3):
                    val = cells[i][j].get().strip()
                    # 空字符串视为0（空格）
                    row.append(int(val) if val else 0)
                state.append(row)

            # 验证是否包含0-8的所有数字（不重复）
            flat = [num for row in state for num in row]
            if sorted(flat) != [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                raise ValueError("必须包含0-8的所有数字（不重复）")
            return state
        except ValueError as e:
            messagebox.showerror("输入错误", f"输入无效：{str(e)}")
            return None

    def solve_puzzle(self):
        """获取输入状态并求解"""
        # 获取初始状态和目标状态
        initial_state = self.get_state_from_grid(self.initial_cells)
        goal_state = self.get_state_from_grid(self.goal_cells)

        if not initial_state or not goal_state:
            return

        # 初始化求解器
        puzzle = EightPuzzle(initial_state, goal_state)
        path, message = puzzle.solve()

        # 更新界面显示
        self.status_label.config(text=message)
        self.path_text.delete(1.0, tk.END)

        if path:
            # 存储求解路径（包含初始状态）
            self.solution_path = [(initial_state, "初始状态")] + path
            self.current_step = 0
            self.update_display()

            # 显示步骤列表
            steps = [f"{i + 1}. {move}" for i, (_, move) in enumerate(self.solution_path)]
            self.path_text.insert(tk.END, "\n".join(steps))
        else:
            self.solution_path = []
            self.current_step = 0

    def update_display(self):
        """更新当前步骤的状态显示"""
        if not self.solution_path:
            return

        # 获取当前步骤的状态和移动
        current_state, move = self.solution_path[self.current_step]

        # 在初始状态区域显示当前步骤（方便对比目标）
        for i in range(3):
            for j in range(3):
                self.initial_cells[i][j].delete(0, tk.END)
                val = current_state[i][j]
                self.initial_cells[i][j].insert(0, str(val) if val != 0 else "")

        # 更新步骤标签
        self.step_label.config(text=f"当前步骤 {self.current_step}/{len(self.solution_path) - 1}: {move}")

    def prev_step(self):
        """查看上一步"""
        if self.solution_path and self.current_step > 0:
            self.current_step -= 1
            self.update_display()

    def next_step(self):
        """查看下一步"""
        if self.solution_path and self.current_step < len(self.solution_path) - 1:
            self.current_step += 1
            self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()