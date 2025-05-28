with open("log_file.txt","r") as f:
  for line_num,line in enumerate(f,start = 1):
    if "python" in line.lower():
      print(f"Python found in line_no: {line_num}")