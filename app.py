import matplotlib.pyplot as plt
import io
from fastmcp import FastMCP
from fastmcp.utilities.types import Image
app=FastMCP("My MCP Server")
# 提供一個加法的工具
@app.tool
def add(n1:int, n2:int)->int:
  """Add Two Numbers"""
  return n1+n2
# 提供一個繪製圓餅圖的工具
@app.tool
def draw_pie_chart(numbers:list[int])->Image:
  """Draw Pie Chart"""
  plt.pie(numbers)
  buffer=io.BytesIO()
  plt.savefig(buffer, format="png")
  return Image(data=buffer.getvalue(), format="png")