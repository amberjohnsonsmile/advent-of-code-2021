sample_depth_list = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def get_number_of_increases(depth_list):
  counter = 0
  list_length = len(depth_list)
  enum_depth_list = enumerate(depth_list)

  for i, depth in enum_depth_list:
    if i + 1 == list_length:
      break
    if depth < depth_list[i+1]:
      counter += 1
  return counter


def get_list_from_file(filename):
  with open(filename) as file:
    with open(filename) as file:
      lines = file.readlines()
      return [int(line.rstrip()) for line in lines]


full_depth_list = get_list_from_file('full_depth_list.txt')
# print(get_number_of_increases(full_depth_list))

def get_window_increases(depth_list):
  counter = 0
  list_length = len(depth_list)
  enum_depth_list = enumerate(depth_list)

  for i, depth in enum_depth_list:
    if i + 3 == list_length:
      break

    first_window = depth + depth_list[i+1] + depth_list[i+2]
    second_window = depth_list[i+1] + depth_list[i+2] + depth_list[i+3]
    if first_window < second_window:
      counter += 1
  return counter

print(get_window_increases(full_depth_list))