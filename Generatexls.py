import xlrd
import xlwt
from xlutils.copy import copy

# 文件名变量
filename = 'test.xls'

# 读取文件
book_r = xlrd.open_workbook(filename)

# 复制原表格
book_w = copy(book_r)

# 以编辑方式得到文件的第一个工作表
sheet_1 = book_w.get_sheet(0)

# 定义要输入的内容
text = 'This is a test of Ricky.'

# 定义写入表格的单元格行号，使用下标1
row = 1

# 定义写入表格的单元格列号，使用下标2
col = 2

# 把内容写入表格
sheet_1.write(row, col, text)

# 删除原文件
os.remove(filename)

# 保存修改的文件为原文件
book_w.save(filename)