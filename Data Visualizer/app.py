import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename): #same folder
  print("""Load CSV data into a DataFrame""")
  return pd.read_csv(filename)

def plot_bar(data):
  print("""Create a bar chart from data""")
  plt.figure(figsize= (8,6))
  plt.bar(data['Category'], data['Amount'], color = 'skyblue')
  plt.title("Expenses")
  plt.xlabel("Category")
  plt.ylabel("Amount")
  plt.savefig("bar_chart.png")
  plt.show()

def plot_pie(data):
  print("""Create a pie chart from data""")
  plt.figure(figsize = (8,6))
  plt.pie(data['Amount'], labels = data['Category'], autopct = '%1.1f%%', startangle = 140)
  plt.title("Expenses Pie Chart")
  plt.savefig("pie_chart.png")
  plt.show()

def main():
  filename = "data.csv"
  data = load_data(filename)
  print("Choose chart type")
  print("1.Bar Chart")
  print("2.Pie Chart")
  print("3.Exit")
  
while True:
choice = int(input("Enter choice: "))
  if choice == 1:
    plot_bar(data)
  elif choice == 2:
    plot_pie(data)
  elif choice == 3:
    print("Goodbye")
    break
  else : 
    print("invalid choice")

if __name__== "__main__":
  main()
  
