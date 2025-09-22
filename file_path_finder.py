import os
def find_file(filename, search_path="/"):
  found_paths = []


  for root, dirs,files in os.walk(search_path):
    if filename in files:
      full_path = os.path.join(root, filename)
      found_paths.append(full_path)
  return found_paths



if __name__ == "__main__":
  filename = input("Enter the filename to search for: ").strip()
  start_path = input("Enter the starding directory(Leave blank for '/'): ").strip()

  if not start_path:
    start_path = "/"
  print(f"\nSearching for '{filename}' in '{start_path}'......\n")

  results = find_file(filename, start_path)
  if results:
    print("File found at:")
    for path in results:
      print(path)
  else:
    print("File not found.")



