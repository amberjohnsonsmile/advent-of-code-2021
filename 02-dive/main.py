def get_list_from_file(filename):
  with open(filename) as file:
    with open(filename) as file:
      lines = file.readlines()
      return [line.rstrip() for line in lines]


def get_position(command_list):
  horizontal = 0
  depth = 0

  for command in command_list:
    command_as_list = command.split()

    if command_as_list[0] == 'forward':
      horizontal += int(command_as_list[1])
    elif command_as_list[0] == 'up':
      depth -= int(command_as_list[1])
    elif command_as_list[0] == 'down':
      depth += int(command_as_list[1])
  
  print(horizontal, depth)
  print(horizontal * depth)
  return horizontal * depth


sample_command_list = get_list_from_file('sample_command_list.txt')
# get_position(sample_command_list)

full_command_list = get_list_from_file('full_command_list.txt')
# get_position(full_command_list)


def get_position_with_aim(command_list):
  horizontal = 0
  depth = 0
  aim = 0

  for command in command_list:
    command_as_list = command.split()

    if command_as_list[0] == 'forward':
      horizontal += int(command_as_list[1])
      depth += int(command_as_list[1]) * aim
    elif command_as_list[0] == 'up':
      aim -= int(command_as_list[1])
    elif command_as_list[0] == 'down':
      aim += int(command_as_list[1])
  
  print(horizontal, depth)
  print(horizontal * depth)
  return horizontal * depth

get_position_with_aim(sample_command_list)
get_position_with_aim(full_command_list)